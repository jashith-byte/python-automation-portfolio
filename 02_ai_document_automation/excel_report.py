import os
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.chart import BarChart, PieChart, Reference

from analyzer import analyze_message


# ==========================================
# GET CUSTOMER MESSAGES
# ==========================================

messages = []

print("Enter customer messages.")
print("Type 'done' when finished.\n")

while True:

    message = input("Customer message: ")

    if message.strip().lower() == "done":
        break

    if message.strip() == "":
        print("Please enter a message.")
        continue

    messages.append(message)


if not messages:
    print("No messages were entered.")
    exit()


# ==========================================
# CREATE EXCEL WORKBOOK
# ==========================================

workbook = Workbook()

sheet = workbook.active
sheet.title = "Customer Analysis"
summary = workbook.create_sheet("Summary")


# ==========================================
# HEADERS
# ==========================================

headers = [
    "Customer ID",
    "Message",
    "Category",
    "Sentiment",
    "Priority",
    "Customer Intent",
    "Recommended Action",
    "Confidence",
    "Confidence Score"
]

sheet.append(headers)


# Make headers bold

for cell in sheet[1]:
    cell.font = Font(bold=True)
    cell.alignment = Alignment(horizontal="center")


# ==========================================
# ANALYZE MESSAGES
# ==========================================

for index, message in enumerate(messages, start=1):

    (
    category,
    sentiment,
    priority,
    intent,
    action,
    confidence,
    confidence_score
    ) = analyze_message(message)
    
    customer_id = f"C{index:03d}"

    sheet.append([
    customer_id,
    message,
    category,
    sentiment,
    priority,
    intent,
    action,
    confidence,
    confidence_score
    ])


# ==========================================
# PROFESSIONAL FORMATTING
# ==========================================

# Header formatting

header_fill = PatternFill(
    fill_type="solid",
    fgColor="D9EAF7"
)

thin_border = Border(
    left=Side(style="thin"),
    right=Side(style="thin"),
    top=Side(style="thin"),
    bottom=Side(style="thin")
)


for cell in sheet[1]:

    cell.font = Font(
        bold=True
    )

    cell.alignment = Alignment(
        horizontal="center",
        vertical="center"
    )

    cell.fill = header_fill
    cell.border = thin_border


# Freeze header row

sheet.freeze_panes = "A2"


# Enable filters

sheet.auto_filter.ref = sheet.dimensions


# Wrap text

for row in sheet.iter_rows():

    for cell in row:

        cell.alignment = Alignment(
            vertical="top",
            wrap_text=True
        )


# Column widths

column_widths = {
    "A": 15,
    "B": 50,
    "C": 25,
    "D": 15,
    "E": 15,
    "F": 40,
    "G": 45,
    "H": 15,
    "I": 18
}

for column, width in column_widths.items():

    sheet.column_dimensions[column].width = width


# Row height

sheet.row_dimensions[1].height = 25


# ==========================================
# SUMMARY DASHBOARD
# ==========================================

summary["A1"] = "CUSTOMER ANALYSIS SUMMARY"

summary["A1"].font = Font(
    bold=True,
    size=18
)

summary["A3"] = "Total Messages"
summary["B3"] = len(messages)

summary["A5"] = "SENTIMENT"
summary["A6"] = "Positive"
summary["A7"] = "Neutral"
summary["A8"] = "Negative"

positive_count = 0
neutral_count = 0
negative_count = 0

high_priority_count = 0
normal_priority_count = 0

category_counts = {}


for row in sheet.iter_rows(min_row=2, values_only=True):

    category = row[2]
    sentiment = row[3]
    priority = row[4]

    # Sentiment
    if sentiment == "Positive":
        positive_count += 1

    elif sentiment == "Negative":
        negative_count += 1

    else:
        neutral_count += 1

    # Priority
    if priority == "High":
        high_priority_count += 1

    else:
        normal_priority_count += 1

    # Category
    category_counts[category] = (
        category_counts.get(category, 0) + 1
    )


summary["B6"] = positive_count
summary["B7"] = neutral_count
summary["B8"] = negative_count


summary["A10"] = "PRIORITY"
summary["A11"] = "High"
summary["A12"] = "Normal"

summary["B11"] = high_priority_count
summary["B12"] = normal_priority_count


summary["A14"] = "CATEGORY BREAKDOWN"

row_number = 15

for category, count in category_counts.items():

    summary.cell(row=row_number, column=1).value = category
    summary.cell(row=row_number, column=2).value = count

    row_number += 1


# ==========================================
# SUMMARY FORMATTING
# ==========================================

summary["A1"].font = Font(
    bold=True,
    size=20
)

summary["A1"].alignment = Alignment(
    horizontal="center"
)

summary.merge_cells("A1:B1")


for cell in ["A5", "A10", "A14"]:

    summary[cell].font = Font(
        bold=True,
        size=14
    )


summary.column_dimensions["A"].width = 32
summary.column_dimensions["B"].width = 20


# Center numerical values

for row in summary.iter_rows():

    for cell in row:

        cell.alignment = Alignment(
            vertical="center"
        )


# ==========================================
# SENTIMENT CHART
# ==========================================

sentiment_chart = PieChart()

sentiment_labels = Reference(
    summary,
    min_col=1,
    min_row=6,
    max_row=8
)

sentiment_data = Reference(
    summary,
    min_col=2,
    min_row=5,
    max_row=8
)

sentiment_chart.add_data(
    sentiment_data,
    titles_from_data=True
)

sentiment_chart.set_categories(sentiment_labels)

sentiment_chart.title = "Customer Sentiment"

summary.add_chart(
    sentiment_chart,
    "D3"
)


# ==========================================
# PRIORITY CHART
# ==========================================

priority_chart = BarChart()

priority_labels = Reference(
    summary,
    min_col=1,
    min_row=11,
    max_row=12
)

priority_data = Reference(
    summary,
    min_col=2,
    min_row=10,
    max_row=12
)

priority_chart.add_data(
    priority_data,
    titles_from_data=True
)

priority_chart.set_categories(priority_labels)

priority_chart.title = "Customer Priority"

summary.add_chart(
    priority_chart,
    "D18"
)

# ==========================================
# ADD FILTERS
# ==========================================

sheet.auto_filter.ref = sheet.dimensions


# ==========================================
# SAVE FILE
# ==========================================


folder = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(
    folder,
    "customer_analysis_report.xlsx"
)

workbook.save(file_path)

print("\n======================================")
print("Excel report created successfully!")
print("Messages processed:", len(messages))
print("File saved to:")
print(file_path)
print("======================================")