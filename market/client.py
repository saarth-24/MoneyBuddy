import os
import requests

from dotenv import load_dotenv

from market.models import MarketData, PricePoint


load_dotenv()


class TwelveDataClient:

    BASE_URL = "https://api.twelvedata.com"

    def __init__(self):
        self.api_key = os.getenv("TWELVE_DATA_API_KEY")

        if not self.api_key:
            raise ValueError(
                "TWELVE_DATA_API_KEY is not set in .env"
            )

    def get_daily_prices(
        self,
        symbol: str,
        exchange: str = "NSE",
        outputsize: int = 30
    ) -> MarketData:

        url = f"{self.BASE_URL}/time_series"

        params = {
            "symbol": symbol,
            "interval": "1day",
            "exchange": exchange,
            "outputsize": outputsize,
            "apikey": self.api_key
        }

        response = requests.get(
            url,
            params=params,
            timeout=10
        )

        if response.status_code != 200:
            print("STATUS:", response.status_code)
            print("API RESPONSE:", response.text)
            raise RuntimeError("Twelve Data request failed")

        data = response.json()

        if data.get("status") == "error":
            raise RuntimeError(
                data.get(
                    "message",
                    "Twelve Data API error"
                )
            )

        values = data.get("values", [])

        if not values:
            raise RuntimeError(
                f"No market data returned for {symbol}"
            )

        prices = []

        for item in values:
            prices.append(
                PricePoint(
                    date=item["datetime"],
                    close=float(item["close"])
                )
            )

        meta = data.get("meta", {})

        return MarketData(
            symbol=meta.get("symbol", symbol),
            exchange=meta.get("exchange", exchange),
            currency=meta.get("currency", "INR"),
            prices=prices
        )


if __name__ == "__main__":

    client = TwelveDataClient()

    market_data = client.get_daily_prices(
    symbol="INFY",
    exchange="NSE",
    outputsize=10
)

    print("\n==============================")
    print("       MARKET DATA TEST")
    print("==============================")

    print(f"Symbol   : {market_data.symbol}")
    print(f"Exchange : {market_data.exchange}")
    print(f"Currency : {market_data.currency}")

    print("\nRecent prices:")

    for price in market_data.prices:
        print(
            f"{price.date} : {market_data.currency} {price.close}"
        )

    print("==============================")   