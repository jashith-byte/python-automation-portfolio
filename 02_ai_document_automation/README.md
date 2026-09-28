# Customer Support Automation & Excel Reporting System

A Python-based customer support automation tool that analyzes customer messages and generates a structured Excel report.

## 🚀 Features

* Automatically analyzes customer messages
* Categorizes customer requests
* Detects sentiment
* Identifies priority
* Determines customer intent
* Suggests a recommended action
* Generates a confidence level and confidence score
* Assigns unique Customer IDs
* Processes multiple customer messages
* Generates an automated Excel report
* Creates summary statistics and charts
* Applies professional Excel formatting

## 🛠️ Technologies Used

* Python
* Rule-based text analysis
* OpenPyXL
* Excel automation

## 📂 Project Structure

```text
02_ai_document_automation/
│
├── analyzer.py
├── excel_report.py
├── customer_analysis_report.xlsx
└── README.md
```

## ⚙️ How It Works

```text
Customer Messages
        ↓
Text Analysis
        ↓
Category Detection
        ↓
Sentiment Detection
        ↓
Priority Detection
        ↓
Intent & Recommended Action
        ↓
Confidence Analysis
        ↓
Excel Report
```

## 📊 Example Analysis

The system can identify categories such as:

* Refund/Return
* Complaint
* Delivery/Shipping
* Product Quality
* Payment/Billing
* Technical Support
* Feedback/Suggestion
* Account/Login

It can also classify messages by:

* Positive / Neutral / Negative sentiment
* Normal / High priority
* High / Medium / Low confidence

## 📈 Excel Report

The generated Excel report contains:

* Customer IDs
* Original customer messages
* Categories
* Sentiment
* Priority
* Customer intent
* Recommended actions
* Confidence levels
* Confidence scores
* Summary statistics
* Charts

## ▶️ How to Run

Make sure Python and OpenPyXL are installed.

```bash
pip install openpyxl
```

Then run:

```bash
python excel_report.py
```

The program will ask for customer messages and generate:

```text
customer_analysis_report.xlsx
```

## 💼 Business Use Case

This type of automation can help businesses process large numbers of customer messages and organize them into structured information for support teams.

Possible applications include:

* Customer support teams
* E-commerce businesses
* Small businesses
* Internal support systems
* Customer feedback analysis

## ⚠️ Note

The message analysis uses a rule-based approach rather than a machine-learning model. The confidence score represents the strength of the matching rules and should not be interpreted as an AI probability.

## 👨‍💻 Project Purpose

This project was built as a practical Python automation project demonstrating how unstructured customer messages can be transformed into structured business information and automated reports.
