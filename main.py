from moneybuddy_state import intelligence
import json
import sys
from investment_planner.analyzer import analyze_portfolio
from user_profile.debt_analyzer import (
    analyze_debts
)
from scenario_engine.engine import run_scenario

from user_profile.goal_analyzer import (
    analyze_goals
)

from investment_planner.analyzer import (
    analyze_portfolio
)

from decision_engine.profile_engine import (
    make_profile_decisions
)

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from user_profile import (
    Debt,
    Investment,
    FinancialGoal,
    FinancialProfile,
    validate_profile,
    profile_to_user
)
from financial_health.models import User, Advice
from financial_health.metrics import calculate
from financial_health.score import healthscore
from financial_health.recommendation import Recommendations
from financial_health.explanation import Explanation

from salary_planner.allocator import create_salary_plan

from goal_planner.calculator import calculate_goal

from decision_engine.engine import make_decisions

from action_plan.generator import generate_action_plan

from market.client import TwelveDataClient
from market.analyzer import analyze_market

from ai_cfo.advisor import generate_cfo_advice
from moneybuddy_state.intelligence import (
    build_intelligence
)

from investment_planner.advisor import (
    analyze_investment_opportunity
)

from risk_engine.profiler import (
    calculate_risk_profile
)

from goal_engine.prioritizer import (
    prioritize_goals
)

from portfolio_engine.recommender import (
    recommend_portfolio_action
)

from scenario_engine.engine import (
    run_scenario,
    rank_scenarios
)


# =========================================================
# LOAD KNOWLEDGE BASE
# =========================================================

def load_knowledge_base():

    with open(
        "financial_health/knowledge_base.json",
        "r",
        encoding="utf-8"
    ) as file:

        return json.load(file)


# =========================================================
# MAIN MONEYBUDDY PIPELINE
# =========================================================

def run_moneybuddy(profile: FinancialProfile, user: User = None):

    if user is None:
        user = profile_to_user(profile)

        
    # =========================================
    # PROFILE INTELLIGENCE
    # =========================================

    debt_analysis = analyze_debts(
        profile
    )

    goals_analysis = analyze_goals(
        profile
    )

    portfolio_analysis = analyze_portfolio(
        profile
    )

    profile_decisions = make_profile_decisions(
        profile,
        debt_analysis,
        goals_analysis,
        portfolio_analysis
    )

    # =====================================================
    # 1. LOAD KNOWLEDGE BASE
    # =====================================================

    knowledge_base = load_knowledge_base()


    # =====================================================
    # 2. FINANCIAL HEALTH
    # =====================================================

    metrics = calculate(user)

    score = healthscore(
        metrics,
        knowledge_base
    )

    recommendations = Recommendations(
        metrics,
        knowledge_base
    )

    explanations = Explanation(
        recommendations,
        knowledge_base
    )

    health_advice = Advice(
        metrics=metrics,
        score=score,
        recommendation=recommendations,
        explanation=explanations
    )


    # =====================================================
    # 3. SALARY PLANNER
    # =====================================================

    salary_plan = create_salary_plan(
        user,
        health_advice
    )

    goals_analysis = analyze_goals(
        profile,
        monthly_available_for_goal=salary_plan.goal_savings
    )


    # =====================================================
    # 4. GOAL PLANNER
    # =====================================================

    goal_analysis = calculate_goal(
        target_amount=user.goal,
        current_amount=user.goal_current_amount,
        time_period_years=user.goal_time_period,
        monthly_available_for_goal=salary_plan.goal_savings
    )


    # =====================================================
    # HIGH-LEVEL FINANCIAL INTELLIGENCE
    # =====================================================

    intelligence = build_intelligence(
        user=user,
        health_advice=health_advice,
        goal_analysis=goal_analysis,
        portfolio_analysis=portfolio_analysis
    )

    risk_profile = intelligence[
        "risk_profile"
    ]

    goal_priorities = intelligence[
        "goal_priorities"
    ]

    portfolio_recommendation = intelligence[
        "portfolio_recommendation"
    ]

    scenario = intelligence[
        "scenario"
    ]


    # =====================================================
    # 5. MARKET ANALYSIS
    # =====================================================

    market_client = TwelveDataClient()

    market_data = market_client.get_daily_prices(
        symbol="INFY",
        exchange="NSE",
        outputsize=30
    )

    market_analysis = analyze_market(
        market_data
    )


    # =====================================================
    # 6. INVESTMENT ANALYSIS
    # =====================================================

    portfolio_analysis = analyze_portfolio(profile)

    investment_decision = analyze_investment_opportunity(
        user=user,
        health_advice=health_advice,
        salary_plan=salary_plan,
        goal_analysis=goal_analysis,
        market_analysis=market_analysis,
        portfolio_analysis=portfolio_analysis
    )


    # =====================================================
    # 7. DECISION ENGINE
    # =====================================================

    decisions = make_decisions(
        user,
        health_advice,
        salary_plan,
        goal_analysis,
        investment_decision
    )


    # =====================================================
    # SCENARIO BASE ALLOCATIONS
    # =====================================================

    emergency_allocation = sum(
        decision.allocated_amount
        for decision in decisions
        if decision.category == "EMERGENCY_FUND"
    )

    debt_allocation = sum(
        decision.allocated_amount
        for decision in decisions
        if decision.category == "DEBT"
    )

    goal_allocation = sum(
        decision.allocated_amount
        for decision in decisions
        if decision.category == "GOAL"
    )

    investment_allocation = sum(
        decision.allocated_amount
        for decision in decisions
        if decision.category == "INVESTMENT"
    )

    intelligence = build_intelligence(
        user=user,
        health_advice=health_advice,
        goal_analysis=goal_analysis,
        portfolio_analysis=portfolio_analysis
    )

    risk_profile = intelligence["risk_profile"]

    goal_priorities = intelligence["goal_priorities"]

    portfolio_recommendation = (
        intelligence["portfolio_recommendation"]
    )

    scenario = intelligence["scenario"]

    # =====================================================
    # WHAT-IF SCENARIO ANALYSIS
    # =====================================================

    salary_scenario = run_scenario(
        scenario_name="Salary Increase",

        current_income=user.salary,
        current_expenses=user.essential_expense,
        current_emi=user.emi,

        current_debt=user.debt,

        emergency_fund=user.emergency_fund,

        goal_required_monthly=goal_analysis.required_monthly_saving,

        income_change=10000,

        emergency_allocation=emergency_allocation,

        goal_allocation=goal_allocation
    )


    expense_scenario = run_scenario(
        scenario_name="Expense Reduction",

        current_income=user.salary,
        current_expenses=user.essential_expense,
        current_emi=user.emi,

        current_debt=user.debt,

        emergency_fund=user.emergency_fund,

        goal_required_monthly=goal_analysis.required_monthly_saving,

        expense_change=-5000,

        emergency_allocation=emergency_allocation,

        goal_allocation=goal_allocation
    )


    debt_scenario = run_scenario(
        scenario_name="Extra Debt Payment",

        current_income=user.salary,
        current_expenses=user.essential_expense,
        current_emi=user.emi,

        current_debt=user.debt,

        emergency_fund=user.emergency_fund,

        goal_required_monthly=goal_analysis.required_monthly_saving,

        extra_debt_payment=3000,

        emergency_allocation=emergency_allocation,

        goal_allocation=goal_allocation
    )


    investment_scenario = run_scenario(
        scenario_name="Additional Investment",

        current_income=user.salary,
        current_expenses=user.essential_expense,
        current_emi=user.emi,

        current_debt=user.debt,

        emergency_fund=user.emergency_fund,

        goal_required_monthly=goal_analysis.required_monthly_saving,

        additional_investment=2000,

        emergency_allocation=emergency_allocation,

        goal_allocation=goal_allocation
    )


    what_if_scenarios = [
        salary_scenario,
        expense_scenario,
        debt_scenario,
        investment_scenario
    ]

    # =====================================================
    # WHAT-IF SCENARIO RANKING
    # =====================================================

    ranked_scenarios = rank_scenarios(
        what_if_scenarios
    )

    # Rank 1 is selected by the Python scenario engine.
    # The AI CFO only explains this result.
    best_scenario = (
        ranked_scenarios[0]["scenario"]
        if ranked_scenarios
        else scenario
    )


    ai_advice = generate_cfo_advice(
        user=user,

        health_advice=health_advice,

        salary_plan=salary_plan,

        goal_analysis=goal_analysis,

        market_analysis=market_analysis,

        investment_decision=investment_decision,

        decisions=decisions,

        risk_profile=risk_profile,

        goal_priorities=goal_priorities,

        portfolio_recommendation=(
            portfolio_recommendation
        ),

        scenario=scenario,

        what_if_scenarios=ranked_scenarios
    )




    
    # =====================================================
    # 8. ACTION PLAN
    # =====================================================

    action_plan = generate_action_plan(
        user,
        decisions,
        salary_plan,
        goal_analysis,
        investment_decision
    )


    # =====================================================
    # RETURN COMPLETE MONEYBUDDY RESULT
    # =====================================================

    return {
        "health_advice": health_advice,

        "salary_plan": salary_plan,

        "goal_analysis": goal_analysis,

        "debt_analysis": debt_analysis,

        "goals_analysis": goals_analysis,

        "profile_decisions": profile_decisions,

        "market_analysis": market_analysis,

        "portfolio_analysis": portfolio_analysis,

        "investment_decision": investment_decision,

        "decisions": decisions,

        "action_plan": action_plan,

        "risk_profile": risk_profile,

        "goal_priorities": goal_priorities,

        "portfolio_recommendation": portfolio_recommendation,

        "scenario": scenario,

        "ai_advice": ai_advice,

        "what_if_scenarios": what_if_scenarios,

        "ranked_scenarios": ranked_scenarios,

        "best_scenario": best_scenario
        
    }


# =========================================================
# DEMO
# =========================================================

if __name__ == "__main__":

    # -----------------------------------------------------
    # SAMPLE USER
    # -----------------------------------------------------

    profile = FinancialProfile(

    monthly_income=50000,

    essential_expenses=35000,

    discretionary_expenses=1000,

    emergency_fund=20000,

    debts=[
        Debt(
            name="Personal Loan",
            outstanding=200000,
            interest_rate=15,
            emi=10000,
            remaining_months=36
        ),

        Debt(
            name="Credit Card",
            outstanding=50000,
            interest_rate=24,
            emi=3000,
            remaining_months=24
        )
    ],

    investments=[
        Investment(
            name="INFY",
            asset_type="STOCK",
            current_value=25000,
            invested_amount=22000
        )
    ],

    goals=[
        FinancialGoal(
            name="House Goal",
            target_amount=500000,
            current_amount=100000,
            target_months=60,
            priority=1
        )
    ]
    )

    validate_profile(profile)

    user = profile_to_user(profile)


    # -----------------------------------------------------
    # RUN MONEYBUDDY
    # -----------------------------------------------------

    result = run_moneybuddy(profile, user)


    # -----------------------------------------------------
    # EXTRACT RESULTS
    # -----------------------------------------------------

    health = result["health_advice"]

    salary_plan = result["salary_plan"]

    goal = result["goal_analysis"]

    debt_analysis = result["debt_analysis"]

    goals_analysis = result["goals_analysis"]

    market_analysis = result["market_analysis"]

    portfolio_analysis = result["portfolio_analysis"]

    profile_decisions = result["profile_decisions"]

    investment_decision = result["investment_decision"]

    action_plan = result["action_plan"]

    risk_profile = result["risk_profile"]

    goal_priorities = result["goal_priorities"]

    portfolio_recommendation = result["portfolio_recommendation"]

    scenario = result["scenario"]

    ranked_scenarios = result.get(
        "ranked_scenarios",
        []
    )

    best_scenario = result.get(
        "best_scenario",
        scenario
    )

    ai_advice = result.get("ai_advice", "")


    # =====================================================
    # DISPLAY
    # =====================================================

    print("\n========================================")
    print("          MONEYBUDDY AI")
    print("========================================")


    # =====================================================
    # FINANCIAL HEALTH
    # =====================================================

    print("\nFINANCIAL HEALTH")
    print("----------------------------------------")

    print(
        f"Health Score : "
        f"{health.score:.1f}/100"
    )

    print(
        f"Savings Ratio : "
        f"{health.metrics.savingratio:.1f}%"
    )

    print(
        f"Expense Ratio : "
        f"{health.metrics.expenseratio:.1f}%"
    )

    print(
        f"Debt Ratio : "
        f"{health.metrics.debtratio:.1f}%"
    )


    # =====================================================
    # GOAL ANALYSIS
    # =====================================================

    print("\nGOAL ANALYSIS")
    print("----------------------------------------")

    print(
        f"Target Amount : "
        f"₹{goal.target_amount:.2f}"
    )

    print(
        f"Current Amount : "
        f"₹{goal.current_amount:.2f}"
    )

    print(
        f"Remaining Amount : "
        f"₹{goal.remaining_amount:.2f}"
    )

    print(
        f"Required Monthly Saving : "
        f"₹{goal.required_monthly_saving:.2f}"
    )

    print(
        f"Status : "
        f"{goal.status}"
    )


    # =====================================================
    # MARKET INTELLIGENCE
    # =====================================================

    print("\nMARKET INTELLIGENCE")
    print("----------------------------------------")

    print(
        f"Asset : "
        f"{market_analysis.symbol}"
    )

    print(
        f"Current Price : "
        f"₹{market_analysis.current_price:.2f}"
    )

    print(
        f"30-Day Return : "
        f"{market_analysis.return_percent:.2f}%"
    )

    print(
        f"Volatility : "
        f"{market_analysis.volatility_percent:.2f}%"
    )

    print(
        f"Trend : "
        f"{market_analysis.trend}"
    )

    print(
        f"Risk Level : "
        f"{market_analysis.risk_level}"
    )

    print(
        f"Market Signal : "
        f"{market_analysis.momentum}"
    )


    print("\nPORTFOLIO ANALYSIS")
    print("----------------------------------------")

    print(
        f"Total Portfolio Value : "
        f"₹{portfolio_analysis.total_value:.2f}"
    )

    print(
        f"Total Invested : "
        f"₹{portfolio_analysis.total_invested:.2f}"
    )

    print(
        f"Total Gain : "
        f"₹{portfolio_analysis.total_gain:.2f}"
    )

    print(
        f"Gain % : "
        f"{portfolio_analysis.total_gain_percent:.2f}%"
    )

    print(
        f"Holdings : "
        f"{portfolio_analysis.number_of_investments}"
    )

    print(
        f"Largest Holding : "
        f"{portfolio_analysis.largest_holding}"
    )

    print(
        f"Concentration : "
        f"{portfolio_analysis.concentration_percent:.2f}%"
    )

    print(
        f"Portfolio Risk : "
        f"{portfolio_analysis.portfolio_risk}"
    )

    print(
        f"Diversification : "
        f"{portfolio_analysis.diversification_status}"
    )


    # =====================================================
    # INVESTMENT DECISION
    # =====================================================

    print("\nINVESTMENT DECISION")
    print("----------------------------------------")

    print(
        f"Action : "
        f"{investment_decision.action}"
    )

    print(
        f"Recommended Amount : "
        f"₹{investment_decision.recommended_amount:.2f}"
    )

    print(
        f"Reason : "
        f"{investment_decision.reason}"
    )

    print(
        f"Confidence : "
        f"{investment_decision.confidence:.1f}%"
    )


    print("\nDEBT INTELLIGENCE")
    print("----------------------------------------")

    print(
        f"Total Debt : "
        f"₹{debt_analysis.total_debt:.2f}"
    )

    print(
        f"Total EMI : "
        f"₹{debt_analysis.total_emi:.2f}"
    )

    print(
        f"Highest Interest Debt : "
        f"{debt_analysis.highest_interest_debt}"
    )

    print(
        f"Highest Interest Rate : "
        f"{debt_analysis.highest_interest_rate:.2f}%"
    )

    print(
        f"Estimated Monthly Interest : "
        f"₹{debt_analysis.estimated_monthly_interest:.2f}"
    )

    print(
        f"Debt To Income Ratio : "
        f"{debt_analysis.debt_to_income_ratio:.2f}%"
    )


    print("\nGOAL INTELLIGENCE")
    print("----------------------------------------")

    print(
        f"Number Of Goals : "
        f"{goals_analysis.total_goals}"
    )

    print(
        f"Highest Priority Goal : "
        f"{goals_analysis.highest_priority_goal}"
    )


    for goal in goals_analysis.goals:

        print(
            f"\n{goal.name}"
        )

        print(
            f"Priority : {goal.priority}"
        )

        print(
            f"Required Monthly : "
            f"₹{goal.required_monthly_saving:.2f}"
        )

        print(
            f"Status : {goal.status}"
        )


    print("\nPORTFOLIO INTELLIGENCE")
    print("----------------------------------------")

    print(
        f"Portfolio Value : "
        f"₹{portfolio_analysis.total_value:.2f}"
    )

    print(
        f"Portfolio Gain : "
        f"₹{portfolio_analysis.total_gain:.2f}"
    )

    print(
    f"Portfolio Gain % : "
    f"{portfolio_analysis.total_gain_percent:.2f}%"
    )

    print(
        f"Concentration : "
        f"{portfolio_analysis.concentration_percent:.2f}%"
    )

    print(
        f"Risk : "
        f"{portfolio_analysis.portfolio_risk}"
    )

    print(
        f"Diversification : "
        f"{portfolio_analysis.diversification_status}"
    )



    print("\nRISK PROFILE")
    print("----------------------------------------")

    print(
        f"Risk Capacity : "
        f"{risk_profile.risk_capacity}"
    )

    print(
        f"Risk Tolerance : "
        f"{risk_profile.risk_tolerance}"
    )

    print(
        f"Overall Profile : "
        f"{risk_profile.overall_profile}"
    )

    print(
        f"Emergency Coverage : "
        f"{risk_profile.emergency_months:.2f} months"
    )

    print(
        f"Explanation : "
        f"{risk_profile.explanation}"
    )



    print("\nGOAL PRIORITIES")
    print("----------------------------------------")

    for goal_priority in goal_priorities:

        print(
            f"\nGoal : "
            f"{goal_priority.name}"
        )

        print(
            f"Priority Score : "
            f"{goal_priority.priority_score:.2f}"
        )

        print(
            f"Urgency : "
            f"{goal_priority.urgency}"
        )

        print(
            f"Recommended Focus : "
            f"{goal_priority.recommended_focus}"
        )

        print(
            f"Reason : "
            f"{goal_priority.reason}"
        )


    print("\nPORTFOLIO RECOMMENDATION")
    print("----------------------------------------")

    print(
        f"Action : "
        f"{portfolio_recommendation.action}"
    )

    print(
        f"Priority : "
        f"{portfolio_recommendation.priority}"
    )

    print(
        f"Reason : "
        f"{portfolio_recommendation.reason}"
    )







    print("\nCURRENT SCENARIO")
    print("----------------------------------------")

    print(
        f"Monthly Surplus : "
        f"₹{scenario.monthly_surplus:.2f}"
    )

    print(
        f"Debt Payment : "
        f"₹{scenario.debt_payment:.2f}"
    )

    print(
        f"Investment Capacity : "
        f"₹{scenario.investment_capacity:.2f}"
    )

    print(
        f"Emergency Coverage : "
        f"{scenario.emergency_months:.2f} months"
    )

    print(
        f"Projected Debt : "
        f"₹{getattr(scenario, 'remaining_debt', getattr(scenario, 'debt_remaining', 0.0)):.2f}"
    )

    print(
        f"Goal Status : "
        f"{scenario.goal_status}"
    )

    print(
        f"Explanation : "
        f"{scenario.explanation}"
    )


    # =====================================================
    # WHAT-IF SCENARIO RANKING
    # =====================================================

    print("\nMONEYBUDDY SCENARIO RANKING")
    print("----------------------------------------")

    for item in ranked_scenarios:

        ranked_result = item["scenario"]

        print(
            f"\nRank : {item['rank']}"
        )

        print(
            f"Score : {item['score']:.2f}"
        )

        print(
            f"Scenario : "
            f"{ranked_result.scenario_name}"
        )

        print(
            f"Monthly Surplus : "
            f"₹{ranked_result.monthly_surplus:.2f}"
        )

        print(
            f"Investment Capacity : "
            f"₹{ranked_result.investment_capacity:.2f}"
        )

        print(
            f"Goal Status : "
            f"{ranked_result.goal_status}"
        )

        print(
            f"Surplus Change : "
            f"₹{ranked_result.surplus_change:.2f}"
        )


    print("\nBEST WHAT-IF SCENARIO")
    print("----------------------------------------")

    if ranked_scenarios:

        best_item = ranked_scenarios[0]

        print(
            f"Scenario : "
            f"{best_scenario.scenario_name}"
        )

        print(
            f"Score : "
            f"{best_item['score']:.2f}"
        )

        print(
            f"Monthly Surplus : "
            f"₹{best_scenario.monthly_surplus:.2f}"
        )

        print(
            f"Goal Status : "
            f"{best_scenario.goal_status}"
        )

        print(
            f"Explanation : "
            f"{best_scenario.explanation}"
        )

    else:

        print("No ranked What-If scenarios available.")


    print("\nPROFILE DECISION ENGINE")
    print("----------------------------------------")

    for decision in profile_decisions:

        print(
            f"\nPriority : {decision.priority}"
        )

        print(
            f"Category : {decision.category}"
        )

        print(
            f"Action : {decision.action}"
        )

        print(
            f"Recommended : "
            f"₹{decision.recommended_amount:.2f}"
        )

        print(
            f"Reason : {decision.reason}"
        )

        print(
            f"Confidence : "
            f"{decision.confidence:.1f}%"
        )


    # =====================================================
    # ACTION PLAN
    # =====================================================

    print("\nACTION PLAN")
    print("----------------------------------------")

    print(
        f"Monthly Income : "
        f"₹{action_plan.monthly_income:.2f}"
    )

    print(
        f"Monthly Expenses : "
        f"₹{action_plan.monthly_expenses:.2f}"
    )

    print(
        f"Monthly Surplus : "
        f"₹{action_plan.monthly_surplus:.2f}"
    )


    # =====================================================
    # SUMMARY
    # =====================================================

    print("\nSUMMARY")
    print("----------------------------------------")

    print(
        action_plan.summary
    )


    # =====================================================
    # PRIORITY ACTIONS
    # =====================================================

    print("\nPRIORITY ACTIONS")
    print("----------------------------------------")

    for action in action_plan.actions:

        print(
            f"\nPriority : "
            f"{action.priority}"
        )

        print(
            f"Category : "
            f"{action.category}"
        )

        print(
            f"Action : "
            f"{action.action}"
        )

        print(
            f"Recommended : "
            f"₹{action.recommended_amount:.2f}"
        )

        print(
            f"Allocated : "
            f"₹{action.allocated_amount:.2f}"
        )

        print(
            f"Reason : "
            f"{action.reason}"
        )

        print(
            f"Confidence : "
            f"{action.confidence:.1f}%"
        )


    # =====================================================
    # MONEYBUDDY MESSAGE
    # =====================================================

    print("\nMONEYBUDDY MESSAGE")
    print("----------------------------------------")

    print(
        action_plan.overall_message
    )


    # =====================================================
    # AI CFO ADVICE
    # =====================================================

    print("\nAI CFO ADVICE")
    print("----------------------------------------")

    print(
        f"\n{ai_advice.headline}"
    )

    print(
        f"\nFinancial Status:"
    )

    print(
        ai_advice.financial_status
    )


    print("\nTOP PRIORITY")
    print("----------------------------------------")

    print(
        f"Category : "
        f"{ai_advice.top_priority.category}"
    )

    print(
        f"Action   : "
        f"{ai_advice.top_priority.action}"
    )

    print(
        f"Amount   : "
        f"₹{ai_advice.top_priority.amount:.2f}"
    )

    print(
        f"Why      : "
        f"{ai_advice.top_priority.reason}"
    )


    print("\nOTHER PRIORITIES")
    print("----------------------------------------")

    for priority in ai_advice.secondary_priorities:

        print(
            f"\n{priority.category}"
        )

        print(
            f"Action : {priority.action}"
        )

        print(
            f"Amount : ₹{priority.amount:.2f}"
        )

        print(
            f"Reason : {priority.reason}"
        )


    print("\nINVESTMENT")
    print("----------------------------------------")

    print(
        f"Status : "
        f"{ai_advice.investment_status}"
    )

    print(
        f"Amount : "
        f"₹{ai_advice.investment_amount:.2f}"
    )

    print(
        f"Reason : "
        f"{ai_advice.investment_reason}"
    )


    print("\nGOAL")
    print("----------------------------------------")

    print(
        f"Status : "
        f"{ai_advice.goal_status}"
    )

    print(
        f"Monthly Shortfall : "
        f"₹{ai_advice.goal_shortfall:.2f}"
    )


    print("\nWHY")
    print("----------------------------------------")

    for reason in ai_advice.why:

        print(
            f"• {reason}"
        )


    print("\nNEXT STEPS")
    print("----------------------------------------")

    for index, step in enumerate(
        ai_advice.next_steps,
        start=1
    ):

        print(
            f"{index}. {step}"
        )


    print("\nREASSESS WHEN")
    print("----------------------------------------")

    for trigger in ai_advice.reassessment_triggers:

        print(
            f"• {trigger}"
        )


    print("\nPERSONAL MONEYBUDDY MESSAGE")
    print("----------------------------------------")

    print(
        ai_advice.personal_message
    )


    # =====================================================
    # END
    # =====================================================

    print("\n========================================")