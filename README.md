# Playwright Python Automation Framework

[![Playwright Tests](https://github.com/NishuPareek27/playwright-python-framework/actions/workflows/playwright-tests.yml/badge.svg)](https://github.com/NishuPareek27/playwright-python-framework/actions/workflows/playwright-tests.yml)

A test automation framework for **UI and API testing**, built with **Playwright (Python)** and **Pytest**, using the **Page Object Model (POM)**. It targets the public practice site [automationexercise.com](https://automationexercise.com) and produces **Allure reports** with screenshots, traces and logs for every failed UI test.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Test Coverage](#test-coverage)
- [Getting Started](#getting-started)
- [Running Tests](#running-tests)
- [Configuration](#configuration)
- [Reports and Failure Evidence](#reports-and-failure-evidence)
- [CI/CD](#cicd)
- [Design Notes](#design-notes)
- [Roadmap](#roadmap)
- [Author](#author)

---

## Features

- **UI automation** with Playwright (sync API) and the **Page Object Model**, with a shared `BasePage`
- **API automation** with `requests`: positive and negative scenarios, using a small reusable API client and an endpoints module
- **Data-driven tests** using `pytest.mark.parametrize` with data kept in `testdata/`
- **Multi-browser support**: Chromium, Firefox or WebKit, selected in one config file
- **Automatic failure evidence** for UI tests: full-page screenshot, current URL and a Playwright trace, all attached to the Allure report
- **Video recording** for UI test runs
- **Allure reporting** with feature and story labels and step-level detail
- **Console logging** with timestamps and levels
- **GitHub Actions CI** that runs the suite on every push and pull request to `main`

---

## Tech Stack

| Area | Tools |
|---|---|
| Language | Python 3.11 |
| UI automation | Playwright for Python |
| Test runner | Pytest |
| API testing | Requests |
| Reporting | Allure (`allure-pytest`) |
| CI | GitHub Actions |

Exact versions are pinned in `requirements.txt`.

---

## Project Structure

```
playwright-python-framework/
├── .github/workflows/
│   └── playwright-tests.yml      # CI pipeline
├── api/
│   ├── clients/
│   │   └── api_clients.py        # Thin wrapper around requests (GET / POST)
│   ├── endpoints.py              # Base URL and endpoint paths
│   └── tests/                    # API test suites
├── config/
│   └── config.py                 # BASE_URL, BROWSER, HEADLESS
├── pages/
│   ├── base_page.py              # Shared base class
│   ├── home_page.py              # Home page object
│   └── login_page.py             # Login page object
├── testdata/
│   └── login_data.py             # Data sets for data-driven login tests
├── tests/                        # UI test suites
│   ├── test_homepage.py
│   └── test_login.py
├── utils/
│   └── logger.py                 # Shared logger
├── conftest.py                   # Browser fixture and failure-evidence hook
├── pytest.ini                    # Pytest and Allure settings
├── requirements.txt
└── README.md
```

Folders created at run time and ignored by Git: `allure-results/`, `screenshots/`, `traces/`, `videos/`.

---

## Test Coverage

**14 tests in total: 6 UI and 8 API.**

### UI tests (`tests/`)

| Area | Scenario |
|---|---|
| Homepage | Application loads and the homepage is displayed |
| Login | Navigate to the Signup / Login page and verify the URL and login section |
| Login (data-driven) | Login with 3 invalid credential combinations shows the error message |
| Logout | Log in with a valid account, log out and verify the user is returned to the login link |

### API tests (`api/tests/`)

| Area | Scenario |
|---|---|
| Products list | GET all products: status code, response code, product fields and nested category data |
| Products list (negative) | Invalid endpoint and invalid HTTP method |
| Brands list | GET all brands |
| Brands list (negative) | Invalid endpoint and invalid HTTP method |
| Search product | Search with a valid term |
| Search product (negative) | Search with an empty search term |

---

## Getting Started

### Prerequisites

- Python 3.11 or newer
- Git

### Setup

```bash
git clone https://github.com/NishuPareek27/playwright-python-framework.git
cd playwright-python-framework

python -m venv venv
```

Activate the virtual environment:

```powershell
# Windows (PowerShell)
.\venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source venv/bin/activate
```

Install dependencies and the Playwright browsers:

```bash
pip install -r requirements.txt
playwright install
```

To view Allure reports locally you also need the [Allure command-line tool](https://allurereport.org/docs/install/).

---

## Running Tests

`pytest.ini` already enables verbose output, live logging and Allure results, so a plain `pytest` is enough.

```bash
# Everything (UI + API)
pytest

# UI tests only
pytest tests/

# API tests only
pytest api/tests/

# One file
pytest tests/test_login.py

# Tests whose name contains a keyword
pytest -k "invalid"
```

---

## Configuration

Settings live in `config/config.py`:

| Setting | Default | Meaning |
|---|---|---|
| `BASE_URL` | `https://automationexercise.com` | Application under test |
| `BROWSER` | `chromium` | `chromium`, `firefox` or `webkit` |
| `HEADLESS` | `True` | Set to `False` to watch the browser while debugging locally |

API endpoint paths are defined in `api/endpoints.py`. Login test data is defined in `testdata/login_data.py`.

---

## Reports and Failure Evidence

### Allure report

```bash
pytest
allure serve allure-results
```

Each result includes the feature and story labels, test steps, durations and failure details. API tests attach the JSON response.

### What a failed UI test produces

| Evidence | Location | Also in Allure |
|---|---|---|
| Full-page screenshot | `screenshots/<test_name>.png` | Yes |
| Page URL at failure | log output | Yes |
| Playwright trace | `traces/<test_name>.zip` | Yes |

Open a trace to step through the test with DOM snapshots, network calls and console output:

```bash
playwright show-trace traces/<test_name>.zip
```

Videos of UI runs are written to `videos/`.

---

## CI/CD

The workflow in `.github/workflows/playwright-tests.yml` runs on every push and pull request to `main`:

1. Check out the code
2. Set up Python 3.11
3. Install dependencies and Playwright browsers
4. Run `pytest` with Allure results
5. Upload `allure-results` as a build artifact (even when tests fail)

### Known limitation

The suite targets a live third-party site. Its bot protection can show a "verifying your browser" page to traffic from shared cloud IP ranges, including GitHub Actions runners, so UI tests may fail in CI even when they pass locally. This comes from testing a public site from CI rather than from the test code. In a real project this is avoided by testing against a staging environment the team controls, or by allowlisting the CI runners' IP addresses.

---

## Design Notes

- **Page Object Model**: locators and page actions live in `pages/`; tests only describe the scenario.
- **Single browser fixture**: `conftest.py` creates the browser and context, starts tracing, and a pytest hook collects the failure evidence.
- **API layer**: `APIClient` and `endpoints.py` keep request code and URLs out of the tests.
- **Test data is separate** from test logic, so a new data set needs no code change in the test.

---

## Roadmap

- [x] Page Object Model and Pytest framework
- [x] UI and API test suites
- [x] Allure reporting with screenshot and trace attachments
- [x] GitHub Actions pipeline
- [ ] Read credentials from environment variables instead of test data files
- [ ] Parallel execution (`pytest-xdist`)
- [ ] Cross-browser matrix in CI
- [ ] Docker support
- [ ] MCP server for running tests and summarizing failures from an AI client
- [ ] AI-assisted failure analysis

---

## Author

**Nishu Pareek**, QA Automation Engineer

GitHub: [@NishuPareek27](https://github.com/NishuPareek27)

If this project is useful to you, a star on the repository is appreciated.