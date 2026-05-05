# Selenium Pytest Automation Framework

## 📖 Project Overview

This project is an automation testing framework built using **Selenium WebDriver, Python, and Pytest**.

It follows the **Page Object Model (POM)** design pattern to create reusable, maintainable, and scalable test scripts.

The framework automates an e-commerce workflow including product search, product selection, and cart validation.

---

## 🛠️ Tech Stack

* Python
* Selenium WebDriver
* Pytest
* JSON (Test Data Handling)

---

## 📂 Project Structure

```
tests/        -> Contains test cases  
pages/        -> Page Object Model classes  
utils/        -> Reusable helper methods  
data/         -> Test data (JSON)  
conftest.py   -> Pytest fixtures  
pytest.ini    -> Configuration  
```

---

## 🚀 How to Run the Project

1. Clone the repository:

```
git clone https://github.com/Code1993-Coder/selenium-pytest-framework-projects.git
```

2. Navigate to project folder:

```
cd selenium-pytest-framework-projects
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Execute tests:

```
pytest
```

---

## 🧪 Test Scenario Covered

* Search for a product
* Open product details page
* Add product to cart
* Validate:

  * Product Name
  * Price
  * Quantity
  * Total Price

---

## ⚙️ Framework Features

* Page Object Model (POM)
* Data-driven testing using JSON
* Reusable methods and utilities
* Dynamic XPath handling for tables
* Clean separation of test logic and page objects

---

## 💡 Key Implementation Highlights

* Dynamic locator handling using Python f-strings
* Table data extraction using XPath logic
* Validation between product page and cart page

---

## 👤 Author

Manju Mohan
