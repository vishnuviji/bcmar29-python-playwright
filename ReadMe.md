# Python Playwright Project

This project demonstrates how to use Playwright with Python for end-to-end testing.

## Setup

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd python-playwright
    ```

2. Create a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Install Playwright browsers:
    ```bash
    playwright install
    ```

## Usage

To run the tests, use the following command:
```bash
pytest
```

## Reports

To generate the report, run the following command:
```bash
pytest --html=reports/index.html
```
