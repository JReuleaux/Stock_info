import pandas as pd
from Dailyrun import DailyUpdate
import asyncio
import sqlite3

DATABASE_PATH = "Database.db"

async def main():
    """Met de main functie roepen we en awaiten we de dailyupdate."""
    """Omdat we in dailyupdate de data al omzetten naar een dataframe hoeven we dat hier niet meer te doen"""
    df = await DailyUpdate.get_updates()
    print(df)

    """Hier maken we een lokale sqllite database aan"""
    """We geven de tabel de naam stock_data en verkiezen ervoor om data die al erinstaat te vervangen."""
    """Hier gebruiken we een try except block voor eventueele error handling."""
    """Het toevoegen van een finally is zeer aan te raden dat zelfs als er iets mis gaat de connectie naar de db sluit.""" 
    try:
        connection = sqlite3.connect(DATABASE_PATH)
        df.to_sql("stock_data", connection, if_exists="replace", index=False)
        
    
    except Exception as e:
        print(f"Main.py Main {e}")
    
    finally:
        connection.close()

asyncio.run(main())
"""Voor het aanroepen van de main functie moeten we ook asyncio gebruiken omdat we deze opdracht async willen uitvoeren."""


