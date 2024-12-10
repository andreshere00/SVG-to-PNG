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
  - Logs are stored in a configurable directory.

- **Configurable:**
  - Easy configuration using [`config.yaml`](./src/config/config.yaml).
  - Control logging levels, tracing, and output directories.

Detailed documentation available in the [/docs](./docs) directory.


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
git clone https://github.com/andreshere00/SVG-to-PNG.git
cd SVG-to-PNG
```

Create an `.env` file or rename the `env.template`.

```bash
cp .env.template .env
```

If you will not be used the application via CLI or without docker, it is not mandatory to follow the next steps.

#### For non-dockerized environments

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

### API (Application Program Interface)

#### Makefile

You can build and serve the application using `make`:

```bash
make serve
```

This will build the docker images for the backend and frontend services and launch the application. Frontend application will be launched on port 8051 and backend application on port 8000. These values can be configured via the `.env` file (modify [`.env.template`](./.env.template)).

Access through the browser in the IP address [`http://0.0.0.0:8501`](`http://0.0.0.0:8501`).

#### Docker & Compose

```bash
docker compose up --build
```

Access through the browser in the IP [`http://0.0.0.0:8501`](`http://0.0.0.0:8501`).

#### Vanilla

Launch both services relying solely on local machine:

Backend service:

```bash
pipenv shell
pipenv run uvicorn src.interfaces.api.main:app --reload --host 0.0.0.0 --port 8000
```

Frontend service:

```bash
pipenv shell
pipenv run streamlit run src.interfaces.api.frontend.app.py --server.port=8501 --server.address=0.0.0.0
```

Access through the browser in the IP [`http://0.0.0.0:8501`](`http://0.0.0.0:8501`).

### Command-Line Interface (CLI)

```bash
pipenv shell
pipenv install
pipenv run python src/interfaces/cli/main.py --input <input_file.svg> --output <output_file.png>
```

NOTE: you may need some of the external dependencies listed previously (see [Pre-requisites section](#pre-requisites)).

**Example:**

```bash
pipenv run python src/interfaces/cli/main.py --input static/input/input.svg --output static/output/output.svg
```

## Configuration

Edit the [`config.yaml`](./src/config/config.yaml) file to adjust application settings. In docs explain all the available settings. But the script can be executed with the default configuration.

## Project Structure

```
.
├── tests/
│   ├── assets/
│   │   ├── output.png
│   │   └── sample.svg
│   ├── methods/
│   │   ├── __init__.py
│   │   ├── test_svg2pdf2png.py
│   │   ├── test_svg2png_cairo.py
│   │   ├── test_svg2png_inkscape.py
│   │   └── test_svg2png_reportlab.py
│   ├── services/
│   │   ├── converter/
│   │   │   ├── __init__.py
│   │   │   └── test_factory.py
│   │   └── processor/
│   │       ├── __init__.py
│   │       └── test_svg_processor.py
│   └── utils/
│       ├── __init__.py
│       └── test_validator.py
├── docs/
│   ├── config.md
│   └── main.md
├── logs/
├── src/
│   ├── config/
│   │   ├── logs/
│   │   │   ├── logger.py
│   │   │   └── __init__.py
│   │   └── config.yaml
│   ├── interfaces/
│   │   ├── api/
│   │   │   ├── frontend/
│   │   │   │   └── app.py
│   │   │   ├── routes/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── convert.py
│   │   │   │   ├── download.py
│   │   │   │   └── upload.py
│   │   │   └── main.py
│   │   └── cli/
│   │       ├── __init__.py
│   │       └── main.py
│   ├── methods/
│   │   ├── svg2pdf2png.py
│   │   ├── svg2png_cairo.py
│   │   ├── svg2png_inkscape.py
│   │   ├── svg2png_reportlab.py
│   │   └── __init__.py
│   ├── services/
│   │   ├── converter/
│   │   │   ├── __init__.py
│   │   │   └── svg_factory.py
│   │   └── processor/
│   │       ├── __init__.py
│   │       └── svg_processor.py
│   └── utils/
│       ├── __init__.py
│       ├── config_loader.py
│       ├── tracer.py
│       └── validator.py
├── static/
│   ├── input/
│   │   └── input.svg
│   ├── output/
│   │   ├── output.png
│   │   └── uploads/
├── Pipfile
├── Pipfile.lock
├── Dockerfile
├── docker-compose.yaml
├── .env
└── README.md
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

> ⚠️ **Warning**:
> Please, before committing, ensure that `pre-commit` is installed, along with their hooks and all the features have the appropriate documentation and tests.
> Any feature without tests or documentation will not be approved to be merged, or in some cases, it will be deleted.

### Install hooks and pre-commit

You can simply use Make:

```bash
make pre-commit
```

Or manually execute:

```bash
pipenv install -d
pipenv run pre-commit install
pipenv run pre-commit autoupdate
pipenv run pre-commit run --all-files
```

## Next steps

1. Aggregate support to process multiple files by console.
2. Incorporate an e2e (end-to-end) feature to use several conversion methods at once.
3. Add mechanisms to CI/CD (Continuous Integration & Continuous Deployment), if needed.
