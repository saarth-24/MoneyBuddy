from typing import Dict

from user_profile.models import FinancialProfile

from market.client import TwelveDataClient
from market.analyzer import analyze_market


def analyze_profile_markets(
    profile: FinancialProfile,
    client: TwelveDataClient
) -> Dict:

    results = {}

    for investment in profile.investments:

        if investment.asset_type.upper() not in {
            "STOCK",
            "ETF"
        }:

            continue

        try:

            market_data = client.get_daily_prices(

                symbol=investment.name,

                exchange="NSE",

                outputsize=30
            )

            results[investment.name] = (
                analyze_market(market_data)
            )

        except Exception as error:

            results[investment.name] = {
                "error": str(error)
            }

    return results