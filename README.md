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


### Pre-requisites

The following packages and programs should be installed before launching the application:

- [Python](https://www.python.org/) 3.12 or higher.
- [Pipenv](https://pipenv.pypa.io/en/latest/) (for dependency management).
- [Inkscape](https://wiki.inkscape.org/wiki/Installing_Inkscape) (Optional).
- [Docker](https://docs.docker.com/engine/install/) (Optional).
- [WSL](https://learn.microsoft.com/en-us/windows/wsl/install) (Optional, but strongly recommended for Windows users, since the instructions are the same as the Ubuntu users showed in this guide).


### Steps

Clone the repository:

```bash
git clone <repository_url>
cd <repository_name>
```

Activate virtual environment:
```bash
pipenv shell
```

Install dependencies:

```bash
pipenv install
```

Install Inkscape (if required, **only needed in non-dockerized** environments):

```bash
brew install --cask inkscape  # macOS
sudo apt install inkscape     # Ubuntu/Debian
```

## Usage

The application can be used either in CLI or API. Configurations must be provided beforehand in the [`config.yaml`](./src/config/config.yaml) file. Additionally, `PYTHONPATH` must be defined in an environment file (can be created as follows):

```bash
mv .env.template .env
```

### Command-Line Interface (CLI)

```bash
pipenv run python src/interfaces/cli/main.py --input <input_file.svg> --output <output_file.png>
```

Following the assets provided in the repository as example:

```bash
pipenv run python src/interfaces/cli/main.py --input static/input/input.svg --output static/output/output.svg
```

### Application Program Interface (API)

#### Without docker

```bash
uvicorn src.interfaces.api.main:app --reload --host 0.0.0.0 --port 8000
```

#### With docker

```bash
sudo docker build -t svg-to-png .
sudo docker run --env-file .env svg-to-png
```

Default methods can be found on `http://localhost:8000/docs`. Note that port 8000 should be opened in order to access to the API through the browser.

## Configuration

Edit the [`config.yaml`](./src/config/config.yaml) file to adjust application settings. In docs explain all the available settings. But the script can be executed with the default configuration.

## Project Structure

```
.
├── src/
│   ├── config/
│   │   ├── config.yaml        # Configuration file
│   │   ├── logs/              # Logger configuration
│   │   │   └── logger.py      # Logger setup
│   │   └── __init__.py
│   ├── interfaces/
│   │   ├── cli/               # Command-line interface
│   │   │   ├── __init__.py
│   │   │   └── main.py        # CLI entrypoint
│   │   ├── api/ 
│   │   │   ├── routes/            # API endpoints
│   │   │   │   ├──__init__.py
│   │   │   │   ├── upload.py      # Upload API
│   │   │   │   ├── convert.py     # Convert API
│   │   │   │   └── download.py    # Download API   
│   │   │   ├── __init__.py
│   │   │   └── main.py            # API entrypoint
│   │   └── __init__.py
│   ├── services/
│   │   ├── processor/         # Main processing logic
│   │   │   ├── __init__.py
│   │   │   └── svg_processor.py
│   │   ├── converter/         # Conversion logic
│   │   │   ├── __init__.py
│   │   │   ├── factory.py
│   │   │   ├── svg2pdf2png.py
│   │   │   ├── svg2png_cairo.py
│   │   │   ├── svg2png_inkscape.py
│   │   │   └── svg2png_reportlab.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── tracer.py          # Tracing utilities
│   │   ├── validator.py       # Input validation
│   │   └── config_loader.py   # Config loader
├── tests/                     # Unit tests
│   ├── methods/
│   │   ├── test_svg2pdf2png.py
│   │   ├── test_svg2png_cairo.py
│   │   ├── test_svg2png_inkscape.py
│   │   └── test_svg2png_reportlab.py
│   ├── services/
│   │   ├── test_factory.py
│   │   └── test_svg_processor.py
│   └── api/
│       ├── test_upload.py
│       ├── test_convert.py
│       └── test_download.py
├── docs/                      # Documentation
│   ├── main.md                # User guide for CLI and API
│   └── config.md              # Configuration details
├── static/                    # Static files
│   ├── input/                 # Sample input files
│   └── output/                # Generated output files
├── Pipfile                    # Dependency management
├── Pipfile.lock               # Locked dependencies
├── Dockerfile                 # Docker setup
├── docker-compose.yaml        # Docker Compose setup
├── .env                       # Environment variables
└── README.md                  # Project overview
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

1. Add hooks and pre-commit configurations.
2. Aggregate support to process multiple files by console.
3. Incorporate an e2e (end-to-end) feature to use several conversion methods at once.
4. Add mechanisms to CI/CD (Continuous Integration & Continuous Deployment), if needed.