# Sales Data Automation & Excel Reporting System

A Python-based business automation tool that reads sales data from a CSV file, cleans and analyzes the data, and automatically generates a structured Excel sales report.

## 🚀 Features

* Reads sales data from CSV files
* Detects missing data
* Automatically handles missing quantities
* Converts data into numeric values
* Calculates individual sales totals
* Calculates total revenue
* Analyzes revenue by product
* Identifies the top-performing product
* Analyzes revenue by customer
* Generates an automated Excel report
* Creates a revenue chart
* Applies professional Excel formatting

## 🛠️ Technologies Used

* Python
* CSV
* OpenPyXL
* Excel automation

## 📂 Project Structure

```text
01_python_automation/
│
├── main.py
├── sales_data.csv
├── sales_report.xlsx
└── README.md
```

## ⚙️ How It Works

```text
Sales CSV File
      ↓
Read Data
      ↓
Detect Missing Data
      ↓
Clean Data
      ↓
Calculate Sales
      ↓
Analyze Products & Customers
      ↓
Generate Excel Report
```

## 📊 Business Analysis

The system calculates:

* Total revenue
* Revenue by product
* Top product by revenue
* Revenue by customer
* Individual order totals

## 🧹 Data Cleaning

The program checks for missing quantities before performing calculations.

For this demonstration dataset, a missing quantity is automatically assigned a value of `1`.

In a real client project, the rule for handling missing information would be agreed upon with the client before automation is implemented.

## 📈 Excel Report

The generated Excel report includes:

* Total revenue
* Top product
* Product revenue breakdown
* Customer revenue breakdown
* Revenue chart
* Currency formatting
* Filters
* Frozen headers
* Report timestamp

## ▶️ How to Run

Make sure OpenPyXL is installed:

```bash
pip install openpyxl
```

Then run:

```bash
python main.py
```

The program reads:

```text
sales_data.csv
```

and automatically generates:

```text
sales_report.xlsx
```

## 💼 Business Use Case

This type of automation can help businesses turn raw sales data into useful reports without manually calculating totals or preparing spreadsheets.

Possible applications include:

* Sales reporting
* E-commerce data processing
* Small business analytics
* Monthly sales reports
* Product performance analysis
* Customer revenue analysis

## 👨‍💻 Project Purpose

This project demonstrates how Python can automate repetitive spreadsheet and data-analysis tasks, transforming raw CSV data into structured business insights and an Excel report.
