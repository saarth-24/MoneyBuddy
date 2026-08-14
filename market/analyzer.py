from market.models import MarketData, MarketAnalysis


def calculate_return(prices: MarketData) -> float:
    """
    Calculates percentage change between
    the oldest and newest available price.
    """

    if len(prices.prices) < 2:
        return 0.0

    newest = prices.prices[0].close
    oldest = prices.prices[-1].close

    return ((newest - oldest) / oldest) * 100


def calculate_average(values: list[float]) -> float:
    """
    Calculates the average of a list of numbers.
    """

    if not values:
        return 0.0

    return sum(values) / len(values)


def calculate_volatility(prices: MarketData) -> float:
    """
    Calculates a simple volatility measure based
    on daily percentage changes.
    """

    if len(prices.prices) < 2:
        return 0.0

    daily_returns = []

    for i in range(len(prices.prices) - 1):

        current_price = prices.prices[i].close
        previous_price = prices.prices[i + 1].close

        daily_return = (
            (current_price - previous_price)
            / previous_price
        ) * 100

        daily_returns.append(daily_return)

    average_return = calculate_average(daily_returns)

    squared_differences = []

    for value in daily_returns:

        difference = value - average_return

        squared_differences.append(
            difference ** 2
        )

    variance = calculate_average(
        squared_differences
    )

    volatility = variance ** 0.5

    return volatility


def determine_trend(prices: MarketData) -> str:
    """
    Determines whether the recent trend is
    upward, downward or neutral.
    """

    if len(prices.prices) < 6:
        return "INSUFFICIENT_DATA"

    recent_prices = [
        price.close
        for price in prices.prices[:5]
    ]

    older_prices = [
        price.close
        for price in prices.prices[-5:]
    ]

    recent_average = calculate_average(
        recent_prices
    )

    older_average = calculate_average(
        older_prices
    )

    difference_percentage = (
        (recent_average - older_average)
        / older_average
    ) * 100

    if difference_percentage > 1:
        return "UPTREND"

    elif difference_percentage < -1:
        return "DOWNTREND"

    else:
        return "NEUTRAL"


def determine_signal(
    return_percentage: float,
    volatility: float,
    trend: str
) -> str:
    """
    Converts quantitative market information
    into a simple market signal.
    """

    if trend == "UPTREND" and return_percentage > 0:
        if volatility < 2:
            return "POSITIVE"
        else:
            return "CAUTIOUSLY_POSITIVE"

    if trend == "DOWNTREND" and return_percentage < 0:
        if volatility > 2:
            return "HIGH_RISK"
        else:
            return "CAUTION"

    return "NEUTRAL"


def determine_risk_level(
    volatility: float,
    trend: str
) -> str:
    """
    Determines market risk level.
    """

    if volatility > 2.0 or trend == "DOWNTREND":
        return "HIGH"
    elif volatility > 1.0:
        return "MODERATE"
    else:
        return "LOW"


def analyze_market(
    market_data: MarketData
) -> MarketAnalysis:
    """
    Main market-analysis function.
    """

    return_percentage = calculate_return(
        market_data
    )

    volatility = calculate_volatility(
        market_data
    )

    trend = determine_trend(
        market_data
    )

    signal = determine_signal(
        return_percentage,
        volatility,
        trend
    )

    risk_level = determine_risk_level(
        volatility,
        trend
    )

    current_price = (
        market_data.prices[0].close
        if market_data.prices
        else 0.0
    )

    return MarketAnalysis(
        symbol=market_data.symbol,
        exchange=market_data.exchange,
        currency=market_data.currency,
        current_price=round(current_price, 2),
        return_percent=round(return_percentage, 2),
        volatility_percent=round(volatility, 2),
        trend=trend,
        risk_level=risk_level,
        momentum=signal
    )








if __name__ == "__main__":

    from market.client import TwelveDataClient

    client = TwelveDataClient()

    market_data = client.get_daily_prices(
        symbol="INFY",
        exchange="NSE",
        outputsize=30
    )

    analysis = analyze_market(
        market_data
    )

    print("\n================================")
    print("       MARKET ANALYSIS")
    print("================================")

    print(
        f"Symbol           : "
        f"{analysis.symbol}"
    )

    print(
        f"Exchange         : "
        f"{analysis.exchange}"
    )

    print(
        f"Return           : "
        f"{analysis.return_percent}%"
    )

    print(
        f"Volatility       : "
        f"{analysis.volatility_percent}%"
    )

    print(
        f"Trend            : "
        f"{analysis.trend}"
    )

    print(
        f"Market Signal    : "
        f"{analysis.momentum}"
    )

    print("================================")