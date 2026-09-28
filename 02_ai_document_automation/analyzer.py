CATEGORY_RULES = {
    "Refund/Return": [
        "refund",
        "return",
        "money back",
        "exchange"
    ],

    "Complaint": [
        "complaint",
        "problem",
        "issue",
        "wrong"
    ],

    "Delivery/Shipping": [
        "delivery",
        "shipping",
        "shipment",
        "courier",
        "arrived"
    ],

    "Product Quality": [
        "product",
        "quality",
        "damaged",
        "broken",
        "defective"
    ],

    "Payment/Billing": [
        "payment",
        "billing",
        "paid",
        "transaction",
        "charge",
        "invoice"
    ],

    "Technical Support": [
        "technical",
        "support",
        "error",
        "bug",
        "crash",
        "not working"
    ],

    "Feedback/Suggestion": [
        "feedback",
        "suggestion",
        "recommend",
        "improve"
    ],

    "Account/Login": [
        "account",
        "login",
        "password",
        "sign in",
        "username"
    ]
}


PRIORITY_RULES = {
    "High": [
        "urgent",
        "asap",
        "emergency",
        "immediately",
        "critical"
    ]
}


NEGATIVE_WORDS = [
    "bad",
    "terrible",
    "angry",
    "hate",
    "worst",
    "awful",
    "horrible",
    "disappointed"
]


POSITIVE_WORDS = [
    "good",
    "great",
    "happy",
    "excellent",
    "amazing",
    "love",
    "perfect"
]


def analyze_message(message):

    text = message.lower()

    # ---------------- CATEGORY ----------------

    category = "General"
    intent = "General customer inquiry"
    action = "Review message and respond"

    category_matches = {}

    for category_name, keywords in CATEGORY_RULES.items():

        matches = []

        for keyword in keywords:

            if keyword in text:
                matches.append(keyword)

        if matches:
            category_matches[category_name] = matches

    if category_matches:

        category = max(
            category_matches,
            key=lambda x: len(category_matches[x])
        )

        matched_keywords = category_matches[category]

    else:

        matched_keywords = []


    # ---------------- INTENT + ACTION ----------------

    if category == "Refund/Return":
        intent = "Requesting a refund or return"
        action = "Review refund/return eligibility"

    elif category == "Complaint":
        intent = "Reporting a problem"
        action = "Review complaint and contact customer"

    elif category == "Delivery/Shipping":
        intent = "Asking about delivery or shipping"
        action = "Check delivery status"

    elif category == "Product Quality":
        intent = "Discussing product quality"
        action = "Review product issue"

    elif category == "Payment/Billing":
        intent = "Reporting a payment or billing issue"
        action = "Check payment or billing records"

    elif category == "Technical Support":
        intent = "Requesting technical assistance"
        action = "Investigate technical issue"

    elif category == "Feedback/Suggestion":
        intent = "Providing feedback or suggestion"
        action = "Review customer feedback"

    elif category == "Account/Login":
        intent = "Having an account or login issue"
        action = "Check account access"


    # ---------------- PRIORITY ----------------

    priority = "Normal"

    priority_matches = []

    for keyword in PRIORITY_RULES["High"]:

        if keyword in text:
            priority_matches.append(keyword)

    if priority_matches:
        priority = "High"


    # ---------------- SENTIMENT ----------------

    negative_matches = [
        word for word in NEGATIVE_WORDS
        if word in text
    ]

    positive_matches = [
        word for word in POSITIVE_WORDS
        if word in text
    ]

    if negative_matches:
        sentiment = "Negative"

    elif positive_matches:
        sentiment = "Positive"

    else:
        sentiment = "Neutral"


    # ---------------- CONFIDENCE ----------------

    confidence_score = 0

    confidence_score += len(matched_keywords) * 20

    if priority_matches:
        confidence_score += 10

    if negative_matches or positive_matches:
        confidence_score += 10

    confidence_score = min(confidence_score, 100)


    if confidence_score >= 70:
        confidence = "High"

    elif confidence_score >= 40:
        confidence = "Medium"

    else:
        confidence = "Low"


    return (
        category,
        sentiment,
        priority,
        intent,
        action,
        confidence,
        confidence_score
    )

'''
# ---------------- TEST ----------------

message = input("Enter a customer message: ")

(
    category,
    sentiment,
    priority,
    intent,
    action,
    confidence,
    confidence_score
) = analyze_message(message)

print("\n===== ANALYSIS =====")
print("Category:", category)
print("Sentiment:", sentiment)
print("Priority:", priority)
print("Intent:", intent)
print("Recommended Action:", action)
print("Confidence:", confidence)
print("Confidence Score:", confidence_score)
'''