# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 12:44:46 2023

@author: Ruturaj
"""

from yahooquery import Ticker
stock = Ticker("RELIANCE.NS")
stock.asset_profile #  profile
stock.financial_data #  financial data
stock.key_stats # KPIs


test=stock.cash_flow(trailing=False) #  Cask Flow
