import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


df = pd.read_csv('weather_research/static/data/Tokyo/rain.csv', skiprows=5)
df["date"] = pd.to_datetime(df["date"])

# [0]の部分を変えると日付も変わる
start_date = df.iloc[180]["date"]
end_date = df.iloc[180]["date"] + timedelta(days=+28)
title_label = start_date.strftime("%Y/%m/%d") + " - " + end_date.strftime("%Y/%m/%d")

df_lim = df.iloc[180:208, :]
# print(df_lim)

fig = plt.figure(figsize=(16, 8))
ax = fig.add_subplot(1, 1, 1)

ax.bar(x=df["date"], height=df["rain"], width=0.96, color="skyblue", align="edge")
ax.set_xlim(start_date, end_date)
ax.set_ylim(0, df_lim.max()[1]+2)
ax.set_title(title_label)
ax.set_facecolor("white")
ax.set_ylabel("precipitation /mm")
ax.grid(axis="y", which="both", linewidth=0.5, linestyle="dashed", alpha=0.5)
plt.xticks(rotation=60)

plt.show()

# days_index = (datetime.strptime("2010-12-31", "%Y-%m-%d")-datetime.strptime("2010-01-01", "%Y-%m-%d")).days

# print(days_index)
# print(df.iloc[days_index])