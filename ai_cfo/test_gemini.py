from ai_cfo.client import AICFOClient


client = AICFOClient()

response = client.generate_advice(
    system_prompt="""
You are MoneyBuddy AI, an AI Chief Financial Officer
for individuals.

Give concise, practical and personalized financial guidance.
Always explain why your recommendation is being made.
Do not invent financial data.
""",

    user_prompt="""
The user earns ₹50,000 per month.

Monthly expenses: ₹45,000
Debt: ₹2,00,000
Debt interest: 15%
Emergency fund: ₹20,000
Financial health score: 75/100

Explain what the user's highest financial priority should be
and why.
"""
)

print("\n==============================")
print("GEMINI TEST")
print("==============================")
print(response)
print("==============================")