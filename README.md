# WebScraping-FlaskProject
# Project Documentation

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Usage](#usage)
- [File Overview](#file-overview)

---

## Introduction
This project is a Flask web application designed for form submission handling. It includes routes for rendering pages, form submissions, and basic spam detection using a honeypot field. The app is designed for easy customization and extension.

## Features
- A home route that welcomes users.
- A form submission endpoint with spam detection using a honeypot field.
- Input sanitization to prevent XSS attacks.
- Email validation for form inputs.
- Thank-you page rendering after successful form submission.


## Usage
1. Run the Flask application:
   ```bash
   python app.py
   ```
2. Access the application in your web browser at `http://127.0.0.1:5000`.
3. Use the form to submit details and see the thank-you page upon successful submission.

## File Overview

### app.py
The main Flask application file:
- `/home`: Displays a welcome message.
- `/`: Renders the form page (`index.html`).
- `/submit`: Handles form submissions, including sanitization, validation, and spam detection.

### Templates
- `index.html`: The main HTML form for user input.
- `thank_you.html`: A page rendered upon successful form submission.

### Static
Contains any static files such as CSS or JavaScript if needed.

### Requirements
- Flask: Required for running the application.
- Additional libraries can be added as needed.


