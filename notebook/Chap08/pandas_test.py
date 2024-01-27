import datetime
import pandas as pd
import numpy as np

# 現在の時刻から5分前の時刻
now = pd.Timestamp(datetime.datetime.now()).round("s")

five_min = datetime.timedelta(seconds=300)

# 現在の時刻から5分前の時刻
start = pd.Timestamp(datetime.datetime.now()).round("s") - datetime.timedelta(
    seconds=300
)

print(now)
print(five_min)
print(start)

price = np.random.randn(50).cumsum()    # cumsumは累積和
print(price)

df = pd.DataFrame(
    {"price": np.random.randn(50).cumsum()},   # cumsumは累積和
    index=pd.date_range(start, freq="s", periods=50),
)

print(df)