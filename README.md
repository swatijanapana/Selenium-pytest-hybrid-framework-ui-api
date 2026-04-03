# Selenium Pytest Hybrid Automation Framework

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pytest](https://img.shields.io/badge/Pytest-testing-green)
![Selenium](https://img.shields.io/badge/Selenium-WebDriver-brightgreen)
![Allure](https://img.shields.io/badge/Reporting-Allure-orange)

A scalable UI + API automation framework built using Python, Selenium, Pytest, and Requests following the Page Object Model (POM) design pattern with data-driven testing and Allure reporting.

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
- Requests (API Testing)

### Framework Design:
- Page Object Model (POM)
- Hybrid Framework (UI + API + Integration)
- Data Driven Testing (Excel)

### Reporting & Execution:
- Allure Reporting
- Pytest Fixtures & Markers
- Cross Browser Testing (Chrome, Firefox, Edge)

##  🚀 Framework Highlights
	•	Page Object Model (POM) architecture
	•	Data-driven testing using Excel
	•	Cross-browser execution (Chrome, Firefox, Edge)
	•	Allure reporting with test analytics
	•	Screenshot capture during test execution
	•	Clean and modular project structure 
	•	Pytest fixtures and parametrization

## 🔗 API Testing Capabilities

    • Implemented API automation using Python requests and Pytest  
    • CRUD operations: GET, POST, PUT, DELETE  
    • Validated status codes, response structure, and data integrity  
    • Implemented positive and negative API test scenarios
    • Built reusable API client layer for scalable test design
    • Dynamic test data generation (avoids duplicate failures)
    • API + UI workflow validation (integration tests)

## 🔄 Integration Testing (Key Differentiator)

This framework supports end-to-end flows:

👉 Example:
	1.	Create user via API
	2.	Login via UI using same credentials
	3.	Validate user session

## 🏗️ Framework Architecture
```
Tests (Pytest)
│
├── API Tests
├── UI Tests
├── Integration Tests
▼
Page Objects (POM)
│
▼
Utilities / Helpers
│
├── Excel Reader
├── Config Reader
├── File Utils
└── API Client
│
▼
Selenium WebDriver/Requests
│
▼
Browser (Chrome / Firefox / Edge)
```

## 📂 Project Structure

```
Selenium_Hybrid_Framework_Pytest
│
├── Pages               # Page Object classes
├── Tests
│   ├── API                 # API test cases
│   ├── UI                  # UI test cases
│   ├── API_UI_Integration  # API + UI integration tests
│   └── conftest.py         # Fixtures (driver, setup, etc.)
├── Utilities           # Helpers (Excel reader, config reader, file utils, API client)
├── Constants           # Static UI/API constants
├── Config              # Configuration files (env, URLs, credentials)
├── TestData            # Excel test data
├── TestFiles           # Files used for upload testing
├── Reports             # Screenshots / Allure results
├── assets              # Images used in README
├── venv                # Virtual environment
├── pytest.ini          # Pytest markers configuration
├── requirements.txt    # Python dependencies
├── .gitignore          # Ignored files for Git
└── README.md
```


## 📊 Test Reporting (Allure)

![Allure Report](assets/allure-report.png)

The framework generates interactive test reports using Allure.

Features include:

	• Test execution summary
	• Pass / Fail statistics
	• Test timeline
	• Suite breakdown
	• Failure analysis

“Achieved ~96% pass rate across 140+ test cases with UI, API, and integration coverage”

## 🧪 Test Categorization (Pytest Markers)
    

  - `@pytest.mark.api`  
  - `@pytest.mark.ui`  
  - `@pytest.mark.integration`


## 🔧 Installation

Clone the repository
```bash
git clone https://github.com/swatijanapana/Selenium_Hybrid_Framework_Pytest.git
cd Selenium_Hybrid_Framework_Pytest
```
Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate
```
Install dependencies
```bash
pip install -r requirements.txt
```

## ▶️ Running Tests

Run all tests
```bash
pytest
```

Run specific folder:
```bash
pytest Tests/API
pytest Tests/UI
pytest Tests/API_UI_Integration
```

Run parallel execution
```bash
pytest -n auto
```

Run tests with Allure results
```bash
pytest --alluredir=Reports/allure-results
```

Open the Allure report
```bash
allure serve Reports/allure-results
```

### Run specific test types:

Run only API tests:
```bash
pytest -m api -v -s
```
Run only UI tests:
```bash
pytest -m ui -v -s
```
Run only Integration tests:
```bash
pytest -m integration -v -s
```

## 🧪 Example Test Scenarios

	•	Login with valid credentials
	•	Login with invalid credentials
	•	Login with blank username/password
	•	Admin search functionality
	•	Reset filters verification
	•	Dropdown selection validation

## 🚧 Future Enhancements

- CI/CD integration (GitHub Actions / Jenkins)  
- API schema validation  
- Database validation  
- Test retry mechanism for flaky tests  
 

## 👩‍💻 Author

Swati J – QA Analyst | Test Automation Engineer

• 6+ years of experience in banking and financial services.
• Designed and developed a Selenium Pytest automation framework. 
• Implemented POM architecture, data-driven testing (Excel), and Allure reporting. 
• Experienced in API validation, database testing, and cross-browser execution.

⭐ If you find this project useful, consider starring the repository or connecting with me on LinkedIn.