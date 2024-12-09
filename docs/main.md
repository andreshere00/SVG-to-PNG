
# SVG to PNG converter application

## Description

This script serves as the **entry point** for an application that converts SVG files to PNG format. It uses a command-line interface (CLI) to accept input and output file paths, validates the input SVG file, ensures the output directory exists, and processes the conversion using a specified method (currently, PDF-to-PNG via `PDFToPNGConverter`). The goal is to provide a robust, extensible, and user-friendly solution for SVG-to-PNG conversion.

The main steps include:
1. Parsing input and output file paths using CLI arguments.
2. Validating the input SVG file format and ensuring the output directory exists.
3. Processing the SVG file to produce a PNG output.

## Parameters

### Command-line Arguments
| Name      | Required | Description                                    | Example                        |
|-----------|----------|------------------------------------------------|--------------------------------|
| `--input` | Yes      | The path to the input SVG file to be converted.| `--input ./static/input.svg`  |
| `--output`| Yes      | The path to save the resulting PNG file.       | `--output ./static/output.png`|

### Internal Parameters
- **`args.input`**: The input SVG file path provided via the `--input` argument.
- **`args.output`**: The output PNG file path provided via the `--output` argument.

## Outputs

### Console Output
- If successful:

  ```bash
  PNG saved at: <output_path>
  ```

- If validation fails:

  ```bash
  Invalid input file. Please provide a valid SVG file.
  ```

- If conversion fails:

  ```bash
  Conversion failed.
  ```

### File output

A PNG file is created at the specified `--output` path if the conversion is successful.

## Execution example

### CLI without docker

```bash
pipenv run python src/interfaces/cli/main.py --input ./static/input/input.svg --output ./static/output/output.png
```

### CLI with docker

```bash
sudo docker build -t svg-to-png .
sudo docker run -it -v $(pwd):/app --env-file .env svg-to-png --input /app/static/input/input.svg --output /app/static/output/output.png
```

### Outputs

#### Success

```bash
PNG saved at: ./static/output.png
```

#### Failure

```bash
Invalid input file. Please provide a valid SVG file.
```

## Notes

- Ensure that you are working inside a virtual environment.
- Ensure all dependencies (svglib, reportlab, pdf2image) are installed in the environment. 