# ------------------ Imports necessary dependencies -----------------#

from dataclasses import dataclass
import datetime

#-------------- Creating DataClass TradeData------------------------#

@dataclass
class TradeData:
    Instrument: str
    Market_position: str
    Qty: int
    Entry_price: float
    Exit_price: float
    Entry_time: datetime.datetime
    Exit_time: datetime.datetime
    Entry_name: str
    Exit_name: str
    Profit: float  # in $
    Commission: float  # in $
    Bars: int