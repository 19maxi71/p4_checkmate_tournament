# Tournament Application

## Project Overview

This project is a tournament management application that allows users to create and manage chess tournaments. 
Created using Python.

## Installation Instructions

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/tournament.git
    cd tournament
    ```

2. **Create a Virtual Environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

To run the application, execute the following command:
    ```sh
    cd controllers
    python main_controller.py
    ```

## Generating flake8 Reports

To generate a flake8 text report, run:
    ```sh
    flake8 --max-line-length=119 > flake8_report.txt
    ```

To generate HTML report run the following command to generate the HTML report:
    ```sh
    flake8 --max-line-length=119 --format=html --htmldir=flake8_report_html
    ```