from itertools import count
#------------------- Imports ------------------------#
from .data_models import TradeData
from typing import List

from .utils import parse_dollar_value


# ------------------------ Retrieves PnL in Ticks-------------------------------------------------------------#

def pnl_in_ticks(trade: TradeData, tick_size: float) -> float:
    if trade.Market_position == "Long":
        return (trade.Exit_price - trade.Entry_price) / tick_size
    else:
        return (trade.Entry_price - trade.Exit_price) / tick_size


# ----------------------- Calculates Gross PnL in Dollars-----------------------------------------------------#

def gross_pnl_dollars(trades: List[TradeData]) -> float:
    gross_profit = sum(trade.Profit for trade in trades)
    return gross_profit


# ----------------------- Calculates Net Pnl in Dollars------------------------------#
def net_pnl_dollars(trades: List[TradeData]) -> float:
    net_pnl = 0
    for trade in trades:
        net_pnl += (trade.Profit - trade.Commission)

    return net_pnl


# ------------------------ Long Trades Profitability --------------------------------------#

def long_profit_trades(trades: List[TradeData]) -> int:
    counter = 0
    for trade in trades:
        if trade.Market_position == "Long" and trade.Profit >= 0:

            counter = counter + 1

    return counter

#------------------- Short Trades Profitability -------------------#

def short_profit_trades (trades: List[TradeData]) -> int:
    counter = 0
    for trade in trades:
        if trade.Market_position == "Short" and trade.Profit >=0:

            counter += 1

    return counter

#------------------- All Profitable Trades -------------------#

def all_profitable_trades (trades: List[TradeData]) -> int:
    counter = 0
    for trade in trades:
        if trade.Profit >= 0:

                counter += 1

    return counter

#--------------- Calculate Winrate -----------------------#

def win_rate (trades: List [TradeData]) -> float:
    counter = 0
    for trade in trades:
        if trade.Profit >= 0:

                counter += 1

    return (counter/ len(trades)) * 100


#-------------- Calculate Lossrate ---------------------#

def loss_rate (trades: List[TradeData]) -> float:
    counter = 0
    for trade in trades:
        if trade.Profit < 0:

                counter += 1

    return (counter / len(trades)) * 100


#----------- Calculate Average Win---------------------#

def avg_win(trades: List[TradeData]) -> float:
    total = 0
    count = 0

    for trade in trades:
        profit = trade.Profit
        if profit > 0:
            total += profit
            count += 1

    if count == 0:
        return 0

    return total / count

#----------- Calculate Average Loss -----------------#


def avg_loss (trades: List [TradeData]) -> int:
    total = 0
    count = 0

    for trade in trades:
         if trade.Profit < 0:
            total += trade.Profit
            count += 1

    if count == 0:
        return 0

    return float(total) / count

#---------- Calculate Expectancy -----------------#

def expectancy (trades: List[TradeData]) -> float:
    wr = win_rate(trades) / 100
    ar = avg_win(trades)
    lr = loss_rate(trades) / 100
    al = abs(avg_loss(trades))

    return (wr * ar) - (lr * al)




























