# API Business Automation & Excel Reporting System

A Python-based automation tool that retrieves data from an API, processes and analyzes the information, and automatically generates a structured Excel report.

## 🚀 Features

* Connects to a REST API
* Retrieves JSON data
* Handles API request errors
* Handles request timeouts
* Extracts relevant information from JSON
* Organizes raw API data into structured records
* Calculates total users
* Identifies unique companies
* Groups users by city
* Identifies the largest user group
* Exports API data to Excel
* Generates a structured business report
* Applies Excel formatting

## 🛠️ Technologies Used

* Python
* Requests
* REST API
* JSON
* OpenPyXL
* Excel automation

## 📂 Project Structure

```text id="2cl7nq"
03_api_automation/
│
├── main.py
├── api_business_report.xlsx
└── README.md
```

## ⚙️ How It Works

```text id="jz8d5a"
REST API
   ↓
HTTP Request
   ↓
JSON Response
   ↓
Data Extraction
   ↓
Data Organization
   ↓
Business Analysis
   ↓
Excel Report
```

## 🔌 API Integration

The project uses a public demonstration API to retrieve sample user and company information.

The data is converted from JSON into structured Python dictionaries containing:

* Name
* Email
* Company
* City

## 📊 Business Analysis

The system calculates:

* Total number of users
* Total number of unique companies
* Number of users by city
* Largest user group by city

## 🛡️ Error Handling

The API request includes:

* Request timeout protection
* HTTP error handling
* Connection/request error handling

This prevents common API failures from causing an uncontrolled program crash.

## 📈 Excel Report

The generated Excel report contains:

* API user data
* Names
* Email addresses
* Companies
* Cities
* Total user count
* Total company count
* Formatted headers
* Frozen table headers

## ▶️ How to Run

Install the required packages:

```bash id="2x9r8k"
pip install requests openpyxl
```

Then run:

```bash id="y7m5p3"
python main.py
```

The program retrieves the API data and automatically generates:

```text id="8v0f2d"
api_business_report.xlsx
```

## 💼 Business Use Case

API automation can help businesses retrieve information from external services and turn it into structured reports automatically.

Possible applications include:

* CRM data extraction
* Business reporting
* Customer data processing
* API-to-Excel automation
* Data synchronization
* Internal reporting tools

## 👨‍💻 Project Purpose

This project demonstrates how Python can connect to external APIs, process JSON data, perform business analysis, and automatically generate a structured Excel report.
