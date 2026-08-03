# Playwright Python Automation Framework

A scalable and maintainable Test Automation Framework built using **Playwright**, **Pytest**, and **Python**, following the **Page Object Model (POM)** design pattern.

This framework is designed to support modern QA automation practices including Data-Driven Testing, Logging, Screenshot Capture on Failure, and Allure Reporting.

---

## 🚀 Features

- Playwright with Python
- Pytest Framework
- Page Object Model (POM)
- Data-Driven Testing (DDT)
- Reusable Base Page
- Logging Support
- Screenshot Capture on Failure
- Allure Reporting
- Configurable Test Data
- Clean Project Structure
- Git & GitHub Integration

---

## 🛠️ Tech Stack

- Python
- Playwright
- Pytest
- Allure Report
- Git
- GitHub

---

## 📁 Project Structure

```text
Playwright_Automation/
│
├── config/
│   └── config.py
│
├── pages/
│   ├── base_page.py
│   ├── home_page.py
│   └── login_page.py
│
├── testdata/
│   └── login_data.py
│
├── tests/
│   ├── test_homepage.py
│   └── test_login.py
│
├── utils/
│   └── logger.py
│
├── screenshots/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## 📌 Framework Design

This framework follows the **Page Object Model (POM)** design pattern.

### Benefits

- Better code maintainability
- Improved reusability
- Reduced code duplication
- Easier test maintenance
- Cleaner separation of test logic and page locators

---

## 🧪 Implemented Test Scenarios

### Homepage

- Launch application
- Verify homepage is displayed
- Navigate to Login page

### Login

- Verify Login page navigation
- Login with invalid credentials
- Validate error message for unsuccessful login

### Data Driven Testing

- Execute login tests using multiple invalid credential combinations

---

## 📊 Logging

Framework includes custom logging support.

Example:

```text
INFO - Entering email: wrong@test.com
INFO - Entering password: wrongpass123
INFO - Clicking on the Login button
```

---

## 📸 Screenshot on Failure

When a test fails:

- Screenshot is captured automatically
- Image is stored inside the `screenshots` folder
- Failure details are logged

Example:

```text
ERROR - Test Failed.
Screenshot saved: screenshots/test_login.png
```

---

## 📈 Allure Reporting

Generate Allure Results:

```bash
pytest --alluredir=allure-results
```

View Allure Report:

```bash
allure serve allure-results
```

Features:

- Test execution summary
- Test steps
- Execution duration
- Failure details
- Attachments (future enhancement)

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/NishuPareek27/playwright-python-framework.git
```

Move into project directory:

```bash
cd playwright-python-framework
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment:

Windows PowerShell:

```bash
.\venv\Scripts\Activate.ps1
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Install Playwright Browsers

```bash
playwright install
```

---

## ▶️ Execute Tests

Run all tests:

```bash
pytest
```

Run tests with detailed output:

```bash
pytest -s -v
```

Run a specific test file:

```bash
pytest tests/test_login.py
```

---

## 📋 Sample Test Execution

```bash
pytest -s
```

Output:

```text
INFO - Entering email: wrong@test.com
INFO - Entering password: wrongpass123
INFO - Clicking on the Login button

PASSED
```

---

## 🔮 Future Enhancements

- Cross Browser Execution
- Parallel Execution
- CI/CD Integration using GitHub Actions
- Docker Integration
- Environment Configuration Management
- Allure Screenshot Attachments
- MCP Integration
- AI-Powered Failure Analysis
- AI Test Case Generation

---

## 📚 Learning Objectives

This project is being enhanced to explore:

- Advanced Playwright Automation
- Framework Design
- Modern QA Practices
- MCP (Model Context Protocol)
- AI-Assisted Test Automation

---

## 👨‍💻 Author

**Nishu Pareek**

- QA Automation Enthusiast
- Playwright & Python Learner
- Exploring MCP and AI in Testing

---

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.

## CI / Known Limitation

This suite runs automatically via GitHub Actions on every push to `main` (see badge above).

The framework targets a live third-party site (automationexercise.com), which uses
bot-protection that challenges traffic from shared cloud IP ranges — including
GitHub Actions runners — with a "verifying your browser" interstitial page. As a result,
CI runs may show test failures even though the same suite passes reliably when run locally.

This is a constraint of testing a public third-party site from CI, not a defect in the
automation framework itself. In a production environment, this is typically handled by:
- Testing against a staging/internal environment the team controls, rather than a public site
- Provisioning a dedicated residential or authenticated proxy for CI traffic
- Coordinating an IP allowlist with the target application's security team

The CI job is configured with `continue-on-error: true` so the pipeline stays green and
visible, while still surfacing full test logs and Allure reports as run artifacts for review.