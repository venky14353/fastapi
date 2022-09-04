
from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class Forecasting(BaseModel):

    MortgageRate: float
    Inflation: float
    TreasuryYield: float
    UnemploymentRate: float
    GDP: float
    ConsumerConfidenceIndex:  float
    DisposableIncome: float