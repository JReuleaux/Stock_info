from Stock_info import stock_list, api_key, GetStockInfo
import asyncio
import pandas as pd
import datetime

class DailyUpdate:

    @staticmethod
    async def get_updates():
        todays_date_time = datetime.datetime.now()
        data = {'Name': [], 'Price': [], 'Date': []}

        tasks = []
        for stock in stock_list:
            tasks.append(GetStockInfo.get_stock_quote(stock, api_key))
            tasks.append(GetStockInfo.get_stock_price(stock, api_key))

        results = await asyncio.gather(*tasks)
        
        for i in range(0, len(results), 2):
            name = results[i]
            price = results[i+1]
            data['Name'].append(name)
            data['Price'].append(price)
            data['Date'].append(todays_date_time)

        return pd.DataFrame(data)




