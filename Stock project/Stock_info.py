import aiohttp

api_key = "API_KEY"

class GetStockInfo:

    try:
        @staticmethod
        async def get_stock_quote(ticker, api):
            """Deze functie maakt een api call via twelvedata naar het kopje quote voor het verkrijgen van de naam met een input van het ticker symbol"""
            """Met aiohttp kunnen we async api calls maken voor de GET call. Door het aanmaken van een sessie kunne we tasks bundelen."""
            """We laten de GET info terug komen in json format en willen hier uit de value van de key price hebben."""
            """Met 'Unkown' as default value handelen we de error KeyError af voor overige errors hebben we de try except blok."""
            url = f"https://api.twelvedata.com/quote?symbol={ticker}&apikey={api}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    data = await response.json()
                    return data.get('name', 'Unknown')
    except Exception as e:
        print(f"Stock_info.py get_stock_quote {e}")

    try:    
        @staticmethod
        async def get_stock_price(ticker, api):
            """Deze functie maakt een api call via twelvedata naar het kopje price voor het verkrijgen van de prijs met een input van het ticker symbol."""
            url = f"https://api.twelvedata.com/price?symbol={ticker}&apikey={api}"
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    data = await response.json()
                    return data.get('price', 'Unknown')
    except Exception as e:
        print(f"Stock_info.py get_stock_price {e}")

stock_list = ['EPR', 'XOM', 'JNJ', 'LTC', 'O']

