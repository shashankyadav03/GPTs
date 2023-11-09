# Simple Web Scraper Flask Application

This is a simple web scraper application built with Flask. It provides a basic interface to input a URL, which it then scrapes to return the page title.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have a `Linux/Unix` like operating system.
- You have installed `Python 3`.
- You have installed `pip`, the Python package installer.

## Installation

To install the required Python packages, run the following command:

```sh
pip install Flask BeautifulSoup4 requests
```

## Setting Up the Application

To set up the application, you need to create the directory structure and initial files. You can use the provided `setup_flask_app.sh` shell script to do this automatically. Follow these steps:

1. Save the `setup_flask_app.sh` script to your local machine.
2. Make the script executable with the following command:

```sh
chmod +x setup_flask_app.sh
```

3. Run the script:

```sh
./setup_flask_app.sh
```

## Running the Application

To run the application, navigate to the `flask_app` directory and execute the `scraper.py` script:

```sh
cd flask_app
python scraper.py
```

The web server should start, and you will see output indicating that it is running. By default, it will be available at `http://localhost:5000`.

Open your web browser and go to `http://localhost:5000` to use the application.

## Contributing to the Application

If you have suggestions for improvements or encounter any issues, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you need to contact me, you can reach out.