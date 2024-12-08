# Configuration Guide

This document explains the available configurations for the application, their purpose, and possible values. The configuration file is located at `./src/config/config.yaml`.

## Configurations

### 1. `svg_conversion_method`
- **Description**: The default method used to convert an SVG file to a PNG. This determines the processing pipeline.
- **Values**:
  - `"pdf"` (default): Converts SVG to PNG by first generating a PDF and then converting it to PNG (uses `svglib`, `reportlab`, and `pdf2image`).
  - `"cairo"` (optional): Direct conversion using the `cairosvg` library.
  - `"inkscape"` (optional): Uses Inkscape as an external tool for conversion.
  - `"reportlab"` (optional): Uses `svglib` and `reportlab` for direct PDF generation.

---

### 2. `output_folder`
- **Description**: The directory where the generated PNG files are stored after processing.
- **Values**:
  - `"./static/output/"` (default): Default directory for storing PNG files.
  - Any custom path, for example: `"./custom_output/"`.

---

### 3. `logging_level`
- **Description**: The level of logging output for the application. Controls the verbosity of logs.
- **Values**:
  - `"DEBUG"`: Detailed logs for debugging purposes.
  - `"INFO"` (default): General informational messages.
  - `"WARNING"`: Alerts for potential issues.
  - `"ERROR"`: Logs only error messages.
  - `"CRITICAL"`: Logs only critical errors.

---

### 4. `enable_logging`
- **Description**: Enables or disables logging for the application.
- **Values**:
  - `true` (default): Enables logging to both console and log files.
  - `false`: Disables logging entirely.

---

### 5. `trace_folder`
- **Description**: Directory to store trace logs containing execution time details for performance analysis.
- **Values**:
  - A valid path to an existing or new directory. For example:
    - `"./logs"` (default): Default folder for trace logs.
    - `"./trace_files/"`: Custom folder for performance logs.

---

### 6. `enable_tracing`
- **Description**: Enables or disables tracing for recording execution times.
- **Values**:
  - `true`: Records execution times for key processes and saves them in trace files.
  - `false` (default): Disables tracing and does not generate trace files.
