from financial_health.models import User, Calculations


def calculate(us: User):

    if us.salary <= 0:
        raise ValueError("Salary must be greater than zero.")

    savings = us.salary - (us.essential_expense + us.emi)

    saving_ratio = round(
        (savings / us.salary) * 100,
        2
    )

    expense_ratio = round(
        (us.essential_expense / us.salary) * 100,
        2
    )

    # Monthly debt burden, not total outstanding debt
    debt_ratio = round(
        (us.emi / us.salary) * 100,
        2
    )

    return Calculations(
        savingratio=saving_ratio,
        expenseratio=expense_ratio,
        debtratio=debt_ratio
    )