
import pandas as pd
from yahooquery import Ticker
stock = Ticker("RELIANCE.NS")
stock.asset_profile #  profile
stock.financial_data #  financial data
stock.key_stats # KPIs

bs=stock.balance_sheet() #  Balance Sheet
bs_df=pd.DataFrame(bs)
print(bs_df)
#stock.cash_flow(trailing=False) #  Cask Flow

#stock.income_statement() # Income Statement(Edited)