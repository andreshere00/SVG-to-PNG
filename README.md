# SVG to PNG Conversion Application

This application provides a basic framework for converting SVG files to PNG format using multiple conversion methods. It is designed with scalability, traceability, and flexibility in mind, allowing developers to use various methods for conversion while maintaining a clean and organized codebase.


## Features

- **Multiple Conversion Methods:**
  - PDF-based (using svglib, reportlab, and pdf2image)
  - CairoSVG (direct conversion with cairosvg)
  - Inkscape (leveraging Inkscape CLI for conversion)
  - ReportLab (direct PDF generation with reportlab)

- **Traceability:**
  - Logs execution times for input processing and output conversion.
  -  Logs are stored in a configurable directory.

- **Configurable:**
  - Easy configuration using [`config.yaml`](./src/config/config.yaml).
  - Control logging levels, tracing, and output directories.

Detailed documentation available in the /docs directory.


## Installation


### Prerequisites

- [Python](https://www.python.org/) 3.12 or higher.
- [Pipenv](https://pipenv.pypa.io/en/latest/) (for dependency management).
- [Inkscape](https://wiki.inkscape.org/wiki/Installing_Inkscape) (optional, for Inkscape-based conversion).


### Steps

Clone the repository:

```bash
git clone <repository_url>
cd <repository_name>
```

Install dependencies:

```bash
pipenv install
```

Install Inkscape (if required):

```bash
brew install --cask inkscape  # macOS
sudo apt install inkscape     # Ubuntu/Debian
```


## Usage


### Command-Line Interface (CLI)

```bash
pipenv run python src/interfaces/cli/main.py --input <input_file.svg> --output <output_file.png>
```


### Application Program Interface (API)

Coming soon!!


## Configuration

Edit the [`config.yaml`](./src/config/config.yaml) file to adjust application settings. In docs explain all the available settings. But the script can be executed with the default configuration.


## Project Structure

```
.
├── src/
│   ├── config/
│   │   ├── config.yaml      # Configuration file
│   │   ├── logs/            # Logger configuration
│   │   └── __init__.py
│   ├── interfaces/
│   │   └── cli/             # Command-line interface
│   │       └── main.py
│   ├── services/
│   │   ├── processor/       # Main processing logic
│   │   │   └── svg_processor.py
│   │   ├── converter/       # Conversion logic
│   │   │   ├── factory.py
│   │   │   ├── svg2pdf2png.py
│   │   │   ├── svg2png_cairo.py
│   │   │   └── svg2png_inkscape.py
│   ├── utils/
│   │   ├── tracer.py        # Tracing utilities
│   │   ├── validator.py     # Input validation
│   │   └── config_loader.py # Config loader
├── tests/                   # Unit tests
│   ├── methods/
│   └── services/
├── docs/                    # Documentation
└── Pipfile                  # Dependency management
```


## Logs & Tracing

- Logs and traces are saved in the `./logs/application.log` file (if `enable_logging` is set to `true`).
- The output folder for these files can be configured on `config.yaml`.


## Contributing

1. Fork the repository.
2. Create a feature branch: git checkout -b feature-name.
3. Commit your changes: git commit -m 'Add new feature'.
4. Push to the branch: git push origin feature-name.
5. Open a pull request.


## Next steps

1. Dockerize the application (based on Linux).
2. Add `.gitignore`, `hooks` and `pre-commit` configurations.
3. Aggregate support to process multiple files by console.
4. Add an API interface.
4. Incorporate an e2e (end-to-end) feature to use several conversion methods at once.
5. Add mechanisms to CI/CD (Continuous Integration & Continuous Deployment), if needed.