# ------------------ Imports necessary libraries -----------------#
import datetime
from .data_models import TradeData
from .metrics import pnl_in_ticks, net_pnl_dollars, gross_pnl_dollars, long_profit_trades, short_profit_trades, \
    all_profitable_trades, win_rate, loss_rate, avg_win, avg_loss, expectancy

import pandas as pd
from typing import List
from .utils import parse_dollar_value

# ------------------------- Normalizes Profit column as it contains '()' -------------------------------------#

#def parse_dollar_value(value: str) -> float:
    #value = value.replace('$', '').replace(',', '')
    #if value.startswith('(') and value.endswith(')'):
        #value = '-' + value[1:-1]  # remove parentheses and prepend minus
    #return float(value)


# ------------------------ Loads Trades from CSV + Loops + Handles Exceptions --------------------------#

def load_trades_from_csv(path: str) -> List[TradeData]:
    df = pd.read_csv(path)
    trades = []



    from .data_models import TradeData
    for index, row in df.iterrows():
        try:
            trade = TradeData(
                Instrument=row["Instrument"],
                Market_position=row["Market_position"],
                Qty=int(row["Qty"]),
                Entry_price=float(row["Entry_price"]),
                Exit_price=float(row["Exit_price"]),
                Entry_time=datetime.datetime.strptime(row["Entry_time"], "%m/%d/%Y %H:%M"),
                Exit_time=datetime.datetime.strptime(row["Exit_time"], "%m/%d/%Y %H:%M"),
                Entry_name=row["Entry_name"],
                Exit_name=row["Exit_name"],
                Profit=parse_dollar_value(row["Profit"]),
                Commission=parse_dollar_value(row["Commission"]),
                Bars=int(row["Bars"])
            )
            trades.append(trade)
        except Exception as e:
            print(f"❌ Skipped row {index + 1} due to error: {e}")
            continue

    return trades


# --------------------- Runs this File -------------------------------------#

if __name__ == "__main__":
    trades = load_trades_from_csv("C:/Users/Deagle/PycharmProjects/trading-log-analyzer/sample/trade_sample.csv")
    print(f"\n📊 Total trades loaded: {len(trades)}")
    print (f"Total PnL in Ticks results to {pnl_in_ticks(trades[0], tick_size=0.25)} ")
    print (f"\n💰 The total Gross Profit results to {gross_pnl_dollars(trades)}")
    print (f"\n📊 The total Net Profit results to {net_pnl_dollars(trades)} ")
    print (f"\n🟩 The total Long trades won are {long_profit_trades(trades)}")
    print (f"\n🟥 The total Short trades won are {short_profit_trades(trades)}")
    print (f" Total number of profitable trades are {all_profitable_trades(trades)}")
    print (f"The Winrate of the Dataset equates to {win_rate(trades):.2f}%")
    print(f"The Lossrate of the Dataset equates to {loss_rate(trades):.2f}%")
    print(f"The Average Win of the Dataset equates to ${avg_win(trades):.2f}")
    print(f"The Average Loss the Dataset equates to ${avg_loss(trades):.2f}")
    print(f"The Strategy Backtest Expectancy equates to ${expectancy(trades):.2f}")







