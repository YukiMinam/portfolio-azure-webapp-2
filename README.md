# Deploy Your Website with Microsoft Azure

This repository contains a simple Python portfolio website that you can run locally and customize. It is intended for workshop attendees who want to learn how to set up a basic web app and test it before deploying it to Azure App Service.

## What you will need

Before you begin, make sure you have:

- Python 3.10 or newer
- pip
- Git
- VS Code or another code editor

## Setup after cloning the repository

Open a terminal in the project folder and run the following commands:

```bash
git clone <your-repository-url>
cd "Deploy Your Website with Microsoft Azure"
python -m venv .venv
```

### Activate the virtual environment

On Windows:

```bash
.venv\Scripts\activate
```

On macOS or Linux:

```bash
source .venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Run the website locally

Start the app with:

```bash
python app.py
```

Then open the website in your browser at:

```text
http://127.0.0.1:5000
```

If the app uses a different port, follow the port shown in the terminal output.

## Customize the portfolio

You can update the following files to personalize the site:

- app.py for the page content and app logic
- templates/index.html for the page layout and text
- static/style.css for colors and design

## Optional: run tests

If you want to verify the app is working, run:

```bash
pytest -q
```

## Helpful notes

- Keep the terminal open while the website is running.
- Use Ctrl+C in the terminal to stop the local server.
- After the app works locally, you can deploy it to Azure App Service.
