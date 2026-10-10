
# agents.py
# Simulated banking data for educational use only
import ollama

CUSTOMER = {
    "customer_id": "C101",
    "name": "Demo Customer",
    "balance": 25000.00,
    "monthly_income": 30000.00,
}

TRANSACTIONS = [
    {"id": "TXN001", "amount": 500, "type": "UPI"},
    {"id": "TXN002", "amount": 1200, "type": "Shopping"},
    {"id": "TXN003", "amount": 45000, "type": "Transfer"},
]


def banking_agent(question):
    q = question.lower()

    if "balance" in q or "money" in q:
        return f"Your demo balance is ₹{CUSTOMER['balance']:,.2f}"

    if any(word in q for word in ["transaction", "history", "payment"]):
        return "\n".join(
            f"{t['id']} | ₹{t['amount']:,} | {t['type']}"
            for t in TRANSACTIONS
        )

    return "Please ask about balance or transaction history."


def fraud_agent(question):
    suspicious = [
        t for t in TRANSACTIONS
        if t["amount"] >= 10000
    ]

    if not suspicious:
        return "No transactions flagged by the demo rule."

    return "Transactions flagged for review:\n" + "\n".join(
        f"{t['id']} | ₹{t['amount']:,} | {t['type']}"
        for t in suspicious
    ) + "\nNote: This is a simple rule-based demo, not real fraud detection."


def loan_agent(question, income=None):
    if income is None:
        income = CUSTOMER["monthly_income"]

    if income < 0:
        return "Income cannot be negative."

    if income >= 25000:
        return (
            f"Monthly income: ₹{income:,.0f}\n"
            "You meet this demo's basic income threshold. "
            "This is not a real loan approval."
        )

    return (
        f"Monthly income: ₹{income:,.0f}\n"
        "You are below this demo's income threshold. "
        "A real lender would assess additional factors."
    )


def help_agent(question):
    return (
        "Welcome to the AI Banking Assistant!\n"
        "You can ask me about:\n"
        "1. Account balance\n"
        "2. Transaction history\n"
        "3. Suspicious transactions\n"
        "4. Loan eligibility"
    )


def supervisor_agent(question, income=None):
    q = question.lower()

    # 1. Fraud agent
    if any(word in q for word in [
        "fraud", "suspicious", "scam", "risk"
    ]):
        agent = "Risk / Fraud Agent"
        response = fraud_agent(question)

    # 2. Loan agent
    elif any(word in q for word in [
        "loan", "credit", "eligibility", "borrow"
    ]):
        agent = "Credit / Loan Agent"
        response = loan_agent(question, income)

    # 3. Banking agent
    elif any(word in q for word in [
        "balance", "money", "transaction",
        "history", "payment"
    ]):
        agent = "Customer / Banking Agent"
        response = banking_agent(question)

    # 4. Other questions use LLM
    else:
        agent = "LLM Banking Assistant"
        response = llm_agent(question)

    return {
        "agent": agent,
        "response": response,
    }

def llm_agent(question):
    try:
        response = ollama.chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful banking assistant. "
                        "Answer general banking questions clearly. "
                        "Never claim to perform real bank transactions "
                        "or approve real loans."
                    ),
                },
                {
                    "role": "user",
                    "content": question,
                },
            ],
        )

        return response["message"]["content"]

    except Exception as e:
        return f"LLM connection error: {e}"