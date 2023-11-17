import pandas as pd
from yahooquery import Ticker
tickers = [
    "POWERGRID.NS",
    "TITAN.NS",
    "HDFCLIFE.NS",
    "M&M.NS",
    "BPCL.NS",
    "NTPC.NS",
    "BRITANNIA.NS",
    "HEROMOTOCO.NS",
    "BAJAJFINSV.NS",
    "TATAMOTORS.NS",
    "BAJAJ-AUTO.NS",
    "ITC.NS",
    "NESTLEIND.NS",
    "SBIN.NS",
    "CIPLA.NS",
    "HINDUNILVR.NS",
    "COALINDIA.NS",
    "BAJFINANCE.NS",
    "LT.NS",
    "ASIANPAINT.NS",
    "TATACONSUM.NS",
    "INDUSINDBK.NS",
    "TCS.NS",
    "SBILIFE.NS",
    "ONGC.NS",
    "SUNPHARMA.NS",
    "HCLTECH.NS",
    "EICHERMOT.NS",
    "APOLLOHOSP.NS",
    "MARUTI.NS",
    "ICICIBANK.NS",
    "AXISBANK.NS",
    "JSWSTEEL.NS",
    "LTIM.NS",
    "TECHM.NS",
    "KOTAKBANK.NS",
    "RELIANCE.NS",
    "GRASIM.NS",
    "UPL.NS",
    "DIVISLAB.NS",
    "TATASTEEL.NS",
    "WIPRO.NS",
    "ULTRACEMCO.NS",
    "INFY.NS",
    "ADANIENT.NS",
    "BHARTIARTL.NS",
    "DRREDDY.NS",
    "ADANIPORTS.NS",
    "HDFCBANK.NS",
    "HINDALCO.NS"
]


results_df = pd.DataFrame(columns=["EBIT", "EnterpriseValue", "NetFixedAssets", "NetWorkingCap", "EarningYield", "ROIC"])

# Create an empty list to store the results
all_data = []

for ticker in tickers:
    stock = Ticker(ticker)

    # Getting the Data
    Bigd = stock.all_financial_data()
    valm = stock.valuation_measures
    latest_val = valm.iloc[3]
    latest_year_data = Bigd.iloc[3]

    # Create a DataFrame for the latest year data
    ticker_data = pd.DataFrame(latest_year_data).transpose()

    # Add the ticker as a column
    ticker_data["Ticker"] = ticker

    # Append the data for this ticker to the all_data list
    all_data.append(ticker_data)

    # Extract and store EnterpriseValue for this ticker
    enterprise_value = latest_val.get("EnterpriseValue")
    all_data[-1]["EnterpriseValue"] = enterprise_value

# Concatenate all DataFrames in the list into one DataFrame
final_data = pd.concat(all_data, ignore_index=False)
final_data1 = final_data.T

# EBIT
ebit_values = final_data1.loc['EBIT']
#EnterpriseValue
EV=final_data1.loc["EnterpriseValue"]
#Net fixed assets
net_fixed_assets = final_data1.loc['NetTangibleAssets']
#Net working capital
CA=final_data1.loc['CurrentAssets']
CL=final_data1.loc['CurrentLiabilities']

net_working_capital=CA-CL
#Magic formula calculation
Ernyld=ebit_values/EV#earning yeild
temp = net_fixed_assets + net_working_capital
rico=ebit_values/temp


#Append the data to the results dataframe
results_df["EBIT"] = ebit_values
results_df["EnterpriseValue"] = EV
results_df["NetFixedAssets"] = net_fixed_assets
results_df["NetWorkingCap"] = net_working_capital
results_df["EarningYield"] = Ernyld
results_df["ROIC"] = rico

#Ranking for EY
results_df["Combrank"]=results_df["EarningYield"].rank(ascending=False,na_option='bottom') + results_df["ROIC"].rank(ascending=False,na_option='bottom')
results_df["Magic_rank"]=results_df["Combrank"].rank(method='first')
value_stocks = results_df.sort_values("Magic_rank")

print("Success!")

