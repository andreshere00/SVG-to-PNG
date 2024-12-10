import streamlit as st
import requests
import os

from src.services.converter.svg_factory import ConverterFactory

API_PORT = os.getenv("API_PORT", "8000")
API_HOST = os.getenv("API_HOST", "localhost")
API_STRING = os.getenv("API_STRING", "api")
API_BASE_URL = f"http://{API_HOST}:{API_PORT}/{API_STRING}"


def validate_file(file_path: str) -> None:
    """
    Validate that the file exists and is not empty.

    Args:
        file_path (str): The path to the file to validate.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is empty.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' does not exist.")
    if os.path.getsize(file_path) == 0:
        raise ValueError(f"File '{file_path}' is empty.")


def cleanup_file(file_path: str) -> None:
    """
    Delete the specified file if it exists.

    Args:
        file_path (str): The path to the file to delete.
    """
    try:
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception as e:
        st.warning(f"Failed to clean up file '{file_path}': {e}")


def upload_svg(file) -> str:
    """
    Upload the SVG file to the API.

    Args:
        file: The uploaded file.

    Returns:
        str: The file ID of the uploaded SVG.
    """
    url = f"{API_BASE_URL}/upload-svg/"
    files = {"file": (file.name, file.read(), file.type)}
    response = requests.post(url, files=files)

    response.raise_for_status()
    if response.status_code == 200:
        return response.json()["file_id"]
    else:
        raise RuntimeError(
            f"Failed to upload SVG: {response.json().get('detail', 'Unknown error')}"
        )


def convert_svg(file_id: str, conversion_method: str) -> str:
    """
    Convert the uploaded SVG to PNG using the selected conversion method.

    Args:
        file_id (str): The file ID of the uploaded SVG.
        conversion_method (str): The conversion method to use.

    Returns:
        str: Path to the converted PNG file on the server.
    """
    url = f"{API_BASE_URL}/convert-svg/"
    response = requests.post(
        url, data={"file_id": file_id, "output_format": "png", "method": conversion_method}
    )
    if response.status_code == 200:
        return response.json()["output_file"]
    else:
        raise RuntimeError(
            f"Failed to convert SVG: {response.json().get('detail', 'Unknown error')}"
        )


def download_png(output_file: str):
    """
    Download the converted PNG from the API.

    Args:
        output_file (str): Path to the PNG file on the server.

    Returns:
        bytes: The content of the PNG file.
    """
    url = f"{API_BASE_URL}/download-png/"
    response = requests.get(url, params={"file_path": output_file}, stream=True)
    if response.status_code == 200:
        return response.content
    else:
        raise RuntimeError(
            f"Failed to download PNG: {response.json().get('detail', 'Unknown error')}"
        )


# Streamlit Interface
st.set_page_config(page_title="SVG to PNG", page_icon="🖼️", layout="centered")
st.title("SVG to PNG Converter")
st.write("Upload an SVG file, choose a conversion method, and get a PNG version of it.")
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: black;
        text-align: center;
        padding: 10px;
        font-size: 14px;
    }
    </style>
    <div class="footer">
        <p><b>Credits:</b> Andrés Herencia López-Menchero | <a href="https://linkedin.com/in/andres-herencia" target="_blank">LinkedIn Profile</a></p>
    </div>
    """,
    unsafe_allow_html=True,
)

# Dynamically fetch the available conversion methods from the factory
conversion_methods = list(ConverterFactory.get_supported_methods())

# Initialize session state for tracking the state of the app
if "conversion_method" not in st.session_state:
    st.session_state.conversion_method = conversion_methods[0]
if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None
if "output_file" not in st.session_state:
    st.session_state.output_file = None

# Select conversion method
selected_method = st.selectbox(
    "Select Conversion Method",
    conversion_methods,
    index=conversion_methods.index(st.session_state.conversion_method),
    key="conversion_method",
)

# Reset logic: Clear uploaded and output file if the conversion method changes
if selected_method != st.session_state.conversion_method:
    st.session_state.conversion_method = selected_method
    st.session_state.uploaded_file = None
    st.session_state.output_file = None
    st.rerun()

# File uploader for user input
uploaded_file = st.file_uploader("Upload SVG file", type=["svg"])

# Check if the file has been detached (reset to None)
if uploaded_file is None and st.session_state.uploaded_file is not None:
    # Reset the app to its original state
    st.session_state.uploaded_file = None
    st.session_state.output_file = None
    st.rerun()

# Handle uploaded file
if uploaded_file is not None:
    st.session_state.uploaded_file = uploaded_file

if st.session_state.uploaded_file is not None:
    # Create a placeholder for dynamic status updates
    status_placeholder = st.empty()
    try:
        # Save the file locally for validation (Streamlit does not expose file path)
        with open("./temp_uploaded.svg", "wb") as temp_file:
            temp_file.write(st.session_state.uploaded_file.getbuffer())

        # Validate the uploaded file
        validate_file("./temp_uploaded.svg")

        # Upload the SVG file
        status_placeholder.write("Uploading your file...")
        file_id = upload_svg(st.session_state.uploaded_file)
        status_placeholder.success(f"File uploaded successfully. File ID: {file_id}")

        # Convert the SVG to PNG
        status_placeholder.write("Converting SVG to PNG...")
        output_file = convert_svg(file_id, st.session_state.conversion_method)
        st.session_state.output_file = output_file
        status_placeholder.success("Conversion successful!")

        # Prepare PNG for download
        status_placeholder.write("Preparing your PNG file for download...")
        png_content = download_png(output_file)
        status_placeholder.success("PNG file ready!")

        # Allow the user to download the PNG file
        st.download_button(
            label="Download PNG",
            data=png_content,
            file_name=f"{file_id}.png",
            mime="image/png",
        )

        # Cleanup uploaded and output files
        cleanup_file("./temp_uploaded.svg")
    except Exception as e:
        status_placeholder.error(f"An error occurred: {e}")
        cleanup_file("./temp_uploaded.svg")
