from financial_health.models import User, Calculations


from financial_health.models import User, Calculations


def calculate(us: User):

    if us.salary <= 0:
        raise ValueError("Salary must be greater than zero.")

    # Total monthly financial outflow
    total_monthly_outflow = (
        us.essential_expense
        + us.emi
    )

    # Money remaining after expenses + EMI
    savings = (
        us.salary
        - total_monthly_outflow
    )

    saving_ratio = round(
        (savings / us.salary) * 100,
        2
    )

    # Expense ratio = regular expenses excluding EMI
    expense_ratio = round(
        (us.essential_expense / us.salary) * 100,
        2
    )

    # EMI ratio
    debt_ratio = round(
        (us.emi / us.salary) * 100,
        2
    )

    return Calculations(
        savingratio=saving_ratio,
        expenseratio=expense_ratio,
        debtratio=debt_ratio
    )