# Configuration Guide

This document explains the available configurations for the application, their purpose, and possible values. The configuration file is located at `./src/config/config.yaml`.

## Configurations

### 1. `svg_conversion`
#### Description:
Defines the default conversion method for transforming SVG files into PNG format. Also lists all supported methods and the output directory for converted files.

#### Keys:
- **`default`**:
  - **Description**: Specifies the default method for SVG-to-PNG conversion.
  - **Values**:
    - `"pdf"` (default): Converts SVG to PNG by generating a PDF and then converting it to PNG (`svglib`, `reportlab`, `pdf2image`).
    - `"cairo"`: Direct conversion using the `cairosvg` library.
    - `"inkscape"`: Uses Inkscape CLI for conversion.
    - `"reportlab"`: Converts SVG to PDF directly using `svglib` and `reportlab`.
- **`methods`**:
  - **Description**: Lists all supported methods for conversion.
  - **Values**:
    - A list including any combination of supported methods (`pdf`, `cairo`, `reportlab`, `inkscape`).
- **`output_folder`**:
  - **Description**: Directory for storing the generated PNG files.
  - **Values**:
    - `"./static/output/"` (default): Default directory for output files.
    - Any custom directory path, for example: `"./custom_output/"`.

---

### 2. `logging`
#### Description:
Defines logging configuration, including log levels, output folders, and enabling or disabling logging.

#### Keys:
- **`level`**:
  - **Description**: Sets the verbosity level of logs.
  - **Values**:
    - `"DEBUG"`: Logs detailed debugging information.
    - `"INFO"` (default): Logs general informational messages.
    - `"WARNING"`: Logs potential issues.
    - `"ERROR"`: Logs error messages.
    - `"CRITICAL"`: Logs only critical errors.
- **`enable`**:
  - **Description**: Enables or disables logging for the application.
  - **Values**:
    - `true` (default): Enables logging to both the console and log files.
    - `false`: Disables all logging.
- **`output_folder`**:
  - **Description**: Directory where log files are stored.
  - **Values**:
    - `"./logs"` (default): Default directory for log files.
    - Any valid directory path, for example: `"./custom_logs/"`.

---

### 3. `enable_tracing`
#### Description:
Enables or disables tracing to record execution times for performance analysis.

#### Values:
- `true`: Enables tracing and writes execution times to trace files.
- `false` (default): Disables tracing.

---

## Notes

### Filling the `.env` File
If you are using the application with CLI, ensure that the `.env` file is properly filled with the `PYTHONPATH` variable:

**Example `.env` File**:
```env
PYTHONPATH='.'

This ensures that Python can locate the src directory and its modules correctly.

## Warnings

1. Ensure that the output_folder and logging.output_folder directories are valid and writable.
2. Tracing and logging should not be enabled (`true`) simultaneously in production environments unless debugging or performance analysis is required.
