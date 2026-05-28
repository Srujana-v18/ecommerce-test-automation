# E-Commerce Automation Framework

Automation testing framework built using:

* Python
* Selenium
* PyTest
* Page Object Model (POM)

---

## Features

* Login automation
* Positive & negative test scenarios
* HTML test reports
* Reusable framework structure

---

## Website Tested

https://www.saucedemo.com/

---

## Project Structure

```text
ecommerce-automation-framework/
│
├── tests/
│   └── test_login.py
│
├── pages/
│   └── login_page.py
│
├── utils/
│   └── driver_factory.py
│
├── reports/
│
├── conftest.py
├── requirements.txt
├── pytest.ini
├── README.md
└── .gitignore
```

---

## Setup Instructions

### Clone Repository

```bash
git clone <your-github-url>
```

---

### Create Virtual Environment

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run Tests

```bash
pytest
```

---

## Generate HTML Report

```bash
pytest --html=reports/report.html --self-contained-html
```

---

## Tech Stack

* Python
* Selenium WebDriver
* PyTest
* webdriver-manager


