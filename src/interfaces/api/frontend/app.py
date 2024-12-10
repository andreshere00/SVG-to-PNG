import streamlit as st
import requests
import os

API_PORT = os.getenv("API_PORT", "8000")
API_HOST = os.getenv("API_HOST", "localhost")
API_BASE_URL = f"http://{API_HOST}:{API_PORT}"


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


def convert_svg(file_id: str) -> str:
    """
    Convert the uploaded SVG to PNG.

    Args:
        file_id (str): The file ID of the uploaded SVG.

    Returns:
        str: Path to the converted PNG file on the server.
    """
    url = f"{API_BASE_URL}/convert-svg/"
    response = requests.post(url, data={"file_id": file_id, "output_format": "png"})
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
st.title("SVG to PNG Converter")
st.write("Upload an SVG file, and get a PNG version of it.")

uploaded_file = st.file_uploader("Upload SVG file", type=["svg"])

if uploaded_file is not None:
    try:
        st.write("Processing your file...")
        # Upload the SVG file
        file_id = upload_svg(uploaded_file)
        st.success(f"File uploaded successfully. File ID: {file_id}")

        # Convert the SVG to PNG
        st.write("Converting SVG to PNG...")
        output_file = convert_svg(file_id)
        st.success("Conversion successful!")

        # Download the PNG
        st.write("Preparing your PNG file for download...")
        png_content = download_png(output_file)
        st.success("PNG file ready!")

        # Allow the user to download the PNG file
        st.download_button(
            label="Download PNG",
            data=png_content,
            file_name="converted_image.png",
            mime="image/png",
        )
    except Exception as e:
        st.error(f"An error occurred: {e}")
