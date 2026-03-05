# Selenium Pytest Hybrid Automation Framework

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pytest](https://img.shields.io/badge/Pytest-testing-green)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-brightgreen)
![Allure](https://img.shields.io/badge/Reporting-Allure-orange)

A scalable UI automation framework built using Python, Selenium, and Pytest following the Page Object Model (POM) design pattern with data-driven testing and Allure reporting.

## Table of Contents

- Tech Stack
- Framework Highlights
- Project Structure
- Test Reporting (Allure)
- Running Tests
- Example Test Scenarios

##  ⚙️ Tech Stack

### Core Tools:
- Python 3.11
- Selenium WebDriver
- Pytest

### Framework Design:
- Page Object Model (POM)
- Data Driven Testing (Excel)

### Reporting:
- Allure Reporting

### Test Execution:
- Cross Browser Testing (Chrome, Firefox, Edge)

##  🚀 Framework Highlights
	•	Page Object Model (POM) architecture
	•	Data-driven testing using Excel
	•	Cross-browser execution (Chrome, Firefox, Edge)
	•	Allure reporting with test analytics
	•	Screenshot capture during test execution
	•	Clean project structure
	•	Pytest fixtures and parametrization

## 📂 Project Structure

```
Selenium_Pytest_Hybrid
│
├── Pages               # Page Object classes
├── Tests               # Test cases
├── Utilities           # Helpers (Excel reader, config reader, logger)
├── Constants           # UI text / default values
├── Config              # Configuration files
├── TestData            # Excel test data
├── Reports             # Screenshots / Allure results
├── assets              # Images used in README
├── Tests/conftest.py   # Pytest fixtures
└── README.md
```

# 📊 Test Reporting (Allure)

![Allure Report](assets/allure-report.png)

The framework generates interactive test reports using Allure.

Features include:

	•	Test execution summary
	•	Pass / Fail statistics
	•	Test timeline
	•	Suite breakdown
	•	Failure analysis

# Running Tests:

Run all tests
```bash
pytest
```
Run tests with Allure results

```bash
pytest --alluredir=Reports/allure-results
```

Open the Allure report
```bash
allure serve Reports/allure-results
```

##  🧪 Example Test Scenarios

	•	Login with valid credentials
	•	Login with invalid credentials
	•	Login with blank username/password
	•	Admin search functionality
	•	Reset filters verification
	•	Dropdown selection validation