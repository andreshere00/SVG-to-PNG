# SVG to PNG Converter Application

## Description

This application provides two main interfaces for converting SVG files to PNG format:
1. **Command-Line Interface (CLI)**: For processing SVG files via terminal commands.
2. **RESTful API**: For uploading, converting, and downloading SVG files via HTTP endpoints.

The application is robust and extensible, allowing multiple conversion methods (`pdf`, `cairo`, `reportlab`, `inkscape`) and supports modularized configuration for logging and tracing.

## Features
1. **CLI for quick conversion**.
2. **API for remote interaction**:
   - Upload SVG files.
   - Convert uploaded SVG files to PNG format.
   - Download the converted PNG files.
3. **Dockerized for easy deployment**.

---

## Usage

### Command-Line Interface (CLI)

#### Parameters

| Argument    | Required | Description                                   | Example                        |
|-------------|----------|-----------------------------------------------|--------------------------------|
| `--input`   | Yes      | The path to the input SVG file.              | `--input ./static/input.svg`  |
| `--output`  | Yes      | The path to save the resulting PNG file.     | `--output ./static/output.png`|

#### Execution

```bash
pipenv run python src/interfaces/cli/main.py --input ./static/input/input.svg --output ./static/output/output.png
```
Output if success:
```bash
PNG saved at: ./static/output.png
```

Output if fails:
```
Invalid input file. Please provide a valid SVG file.
```

### Application Programming Interface (API)

#### Endpoints

1. Upload an SVG File

- **Endpoint**: /upload-svg/
- **Method**: POST
- **Description**: Uploads an SVG file to the server.
- **Parameters**:
  - **file**: The SVG file to upload.

2. **Convert an SVG File**

- **Endpoint**: `/convert-svg/`
- **Method**: POST
- **Description**: Converts an uploaded SVG file to PNG format.
- **Parameters**:
  - **`file_id`**: ID of the uploaded SVG file.
  - **`output_format`**: Desired output format (`png`).

3. **Download Converted File**

- **Endpoint**: `/download-png/`
- **Method**: GET
- **Description**: Downloads the converted PNG file.
- **Parameters**:
  - **`file_path`**: Path to the file on the server.

#### Execution

Note that port 8000 should be accessible through the machine executing the application.

##### With docker

Build the docker container:

```bash
sudo docker compose build -t svg-to-png .
```

Start the API server using docker compose:

```bash
sudo docker-compose up
```

Or a docker container directly:

```bash
sudo docker run --env-file .env svg-to-png 
```

##### Without docker

```bash
uvicorn src.interfaces.api.main:app --reload
```

##### Example API requests

**Upload**

```bash
curl -X POST -F "file=@./static/input/input.svg" http://localhost:8000/upload-svg/
```

**Convert**

```bash
curl -X POST -F "file_id=<file_id>" -F "output_format=png" http://localhost:8000/convert-svg/
```

**Download**

```bash
curl -X GET "http://localhost:8000/download-png/?file_path=<file_path>" -o output.png
```

These requests should be launched from the machine which is executing the application, either the Docker itself or the local machine. For entering into the docker machine and execute the commands, see the following (guide)[https://docs.docker.com/reference/cli/docker/container/exec/]. 

## Configuration

The application uses a [`config.yaml`](src/config/config.yaml) file for customization.

Example:
```yaml
svg_conversion:
  default: pdf
  methods:
    - pdf
    - cairo
    - reportlab
    - inkscape
  output_folder: "./static/output"

logging:
  level: INFO
  enable: true
  output_folder: ./logs
```

Some **Key Parameters** are:

**Conversion Method:**

- `default`: The default method for SVG to PNG conversion.
- `methods`: Supported conversion methods.

**Logging:**

- `level`: Logging verbosity (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).
- `enable`: Enable (`true`) or disable (`false`) logging.
- `output_folder`: Directory for logs.

## Notes

- Use `pipenv` for dependency management.
- Ensure **Poppler** and **Inkscape** are installed if running locally.
- API runs on [http://localhost:8000](http://localhost:8000) by default.