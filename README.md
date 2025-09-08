# 🎭 Playwright Pytest Framework

[![CI](https://github.com/LuisVu1999/playwright-pytest-framework/actions/workflows/playwright.yml/badge.svg)](https://github.com/LuisVu1999/playwright-pytest-framework/actions/workflows/playwright.yml)
[![Allure Report](https://img.shields.io/badge/Allure-Report-ED1C24?logo=allure&logoColor=white)](https://luisvu1999.github.io/playwright-pytest-framework/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/vu-luis-b434b21b2/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> A **scalable Playwright + Pytest automation framework** for **UI & API testing** with **CI/CD integration** and **Allure reporting**.

---

## 📖 Overview
This repository contains a **modular automation framework** built with **Python, Playwright, and Pytest**.  

✨ Key features:
- Page Object Model (POM) for UI tests
- Parallel execution, retries, and multi-browser support
- API testing with Playwright
- Rich **Allure Reports** with screenshots & logs
- CI/CD via **GitHub Actions** + auto-published reports  

🔗 **Live Demo Report** → [Allure Report on GitHub Pages](https://luisvu1999.github.io/playwright-pytest-framework/)

---

## ⚙️ Tech Stack
- 🐍 **Python** 3.10+  
- 🧪 **Pytest** (test framework)  
- 🎭 **Playwright** (UI & API automation)  
- 📊 **Allure** (reporting)  
- ⚡ **GitHub Actions** (CI/CD)  
- 🗂️ **Page Object Model (POM)**  

---

## 🚀 Getting Started

### 1️⃣ Clone repo
```bash
git clone https://github.com/LuisVu1999/playwright-pytest-framework.git
cd playwright-pytest-framework
```

### 2️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Install Playwright browsers
```bash
playwright install
```

---

## 🧪 Running Tests

- ▶️ **Default (Chromium)**  
  ```bash
  pytest --env=dev --browser=chromium
  ```

- 🌍 **All browsers**  
  ```bash
  pytest --env=dev --browser=all
  ```

- 🔄 **With retries (2 times)**  
  ```bash
  pytest --env=dev --browser=chromium --reruns 2
  ```

- ⚡ **Parallel (3 workers)**  
  ```bash
  pytest -n 3 --env=dev --browser=chromium
  ```

---

## 📊 Reporting

- **Generate local Allure Report**  
  ```bash
  allure generate allure-results --clean -o allure-report
  allure open allure-report
  ```

- **GitHub Pages (CI/CD)**  
  Auto-published after each pipeline run → 👉 [Latest Allure Report](https://luisvu1999.github.io/playwright-pytest-framework/)

---

## 🔗 CI/CD Integration

This project integrates with **GitHub Actions**:  
- ✅ Run tests on push/PR  
- ✅ Multi-browser execution  
- ✅ Auto-generate & publish Allure Report  

Workflow file:  
```text
.github/workflows/ci.yml
```


## 📂 Project Structure

```text
playwright-pytest-framework/
├── pages/              # Page Object Models (POM)
├── tests/              # Test cases (UI & API)
│   ├── ui/             # UI test cases
│   └── api/            # API test cases
├── helpers/            # Utility functions & common modules
├── .github/workflows/  # CI/CD configurations
├── config.py           # Environment & config management
├── conftest.py         # Pytest fixtures setup
├── requirements.txt    # Project dependencies
├── pytest.ini          # Pytest configurations
└── README.md           # Project documentation

```

---

## 👤 Author

- **Name:** Luis Vu  
- **📧 Email:** Quyvuduc123456@gmail.com  
- **🔗 LinkedIn:** [Profile](https://www.linkedin.com/in/vu-luis-b434b21b2/)  
- **💻 GitHub:** [LuisVu1999](https://github.com/LuisVu1999)  

---

## 🏆 Highlights

- ✅ Built with **best practices** in automation testing  
- ✅ **Scalable design** ready for CI/CD pipelines  
- ✅ **Portfolio-ready** framework for freelance & enterprise projects 
