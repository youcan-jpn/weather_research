import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta


df = pd.read_csv('weather_research/static/data/Tokyo/rain.csv', skiprows=5)
df["date"] = pd.to_datetime(df["date"])

# [0]の部分を変えると日付も変わる
start_date = df.iloc[170]["date"]
end_date = df.iloc[170]["date"] + timedelta(days=+14)
title_label = start_date.strftime("%Y/%m/%d") + " - " + end_date.strftime("%Y/%m/%d")

df_lim = df.iloc[170:184, :]
# print(df_lim)

fig = plt.figure(figsize=(16, 8))
ax = fig.add_subplot(1, 1, 1)

ax.bar(x=df["date"], height=df["rain"], width=0.98, color="lightgreen", align="edge")
ax.set_xlim(start_date, end_date)
ax.set_ylim(0, df_lim.max()[1]+10)
ax.set_title(title_label)
ax.set_facecolor("white")
ax.grid(axis="both", which="both", linewidth=0.5, linestyle="dashed", alpha=0.5)

plt.show()
