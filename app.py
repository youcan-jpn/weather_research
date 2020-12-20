from flask import Flask, request, render_template
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import urllib
from io import BytesIO
from datetime import datetime, timedelta

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/plot/maxmin')
def plot_maxmin():

    # obtain query parameters
    area1 = request.args.get('area1', type=str)
    area2 = request.args.get('area2', type=str)
    area3 = request.args.get('area3', type=str)
    maxmin_color1 = request.args.get('maxmin_color1', type=str)
    maxmin_color2 = request.args.get('maxmin_color2', type=str)
    maxmin_color3 = request.args.get('maxmin_color3', type=str)
    maxmin_year1 = request.args.get('maxmin_year1', type=str)
    maxmin_year2 = request.args.get('maxmin_year2', type=str)
    maxmin_year3 = request.args.get('maxmin_year3', type=str)
    maxmin_num = request.args.get('data_num', type=int)
    areas = [area1, area2, area3]
    maxmin_colors = [maxmin_color1, maxmin_color2, maxmin_color3]
    maxmin_years = [maxmin_year1, maxmin_year2, maxmin_year3]
    df1 = pd.DataFrame()
    df2 = pd.DataFrame()
    df3 = pd.DataFrame()
    dfs = [df1, df2, df3]
    max_temps = []
    min_temps = []

    # read csv
    for i in range(maxmin_num):
        dfs[i] = pd.read_csv('weather_research/static/data/{0}/maxmin_{1}.csv'.format(areas[i], maxmin_years[i]), skiprows=6, header=None)
        max_temps.append(dfs[i].iloc[:, 1])
        min_temps.append(dfs[i].iloc[:, 4])

    fig, ax = plt.subplots(1, 1)

    # plot
    for i in range(maxmin_num):
        ax.scatter(min_temps[i], max_temps[i], c=maxmin_colors[i], label='{0}:{1}'.format(str(maxmin_years[i]), areas[i]))

    ax.set_xlabel('min temperature')
    ax.set_ylabel('max temperature')
    plt.legend()

    png_out = BytesIO()

    # save figure
    plt.savefig(png_out, format="png", bbox_inches="tight")
    plt.close()
    img_data = urllib.parse.quote(png_out.getvalue())

    return "data:image/png:base64," + img_data


@app.route('/plot/rain')
def plot_rain():

    # obtain query parameters
    area1 = request.args.get('area1', type=str)
    area2 = request.args.get('area2', type=str)
    area3 = request.args.get('area3', type=str)
    areas = [area1, area2, area3]
    start = datetime.strptime(request.args.get("start", default="2010-01-01", type=str), "%Y-%m-%d")
    end = datetime.strptime(request.args.get("end", default="2019-12-31", type=str), "%Y-%m-%d")
    rain_color1 = request.args.get('rain_color1', type=str)
    rain_color2 = request.args.get('rain_color2', type=str)
    rain_color3 = request.args.get('rain_color3', type=str)
    rain_colors = [rain_color1, rain_color2, rain_color3]
    rain_num = request.args.get('data_num', type=int)

    df1 = pd.DataFrame()
    df2 = pd.DataFrame()
    df3 = pd.DataFrame()
    dfs = [df1, df2, df3]

    fig, ax = plt.subplots(1, 1)
    if start > end:
        start, end = end, start

    if (start + timedelta(days=7)) > end:
        end = start + timedelta(days=7)

    # plot
    for i in range(rain_num):
        dfs[i] = pd.read_csv('weather_research/static/data/{0}/rain.csv'.format(areas[i]), index_col=0, skiprows=5, parse_dates=True)
        ax.plot(dfs[i].loc[:, "rain"], c=rain_colors[i], label="{}".format(areas[i]))

    ax.set_xlim([start, end])
    plt.xticks(rotation=30)
    ax.set_ylabel('preciptation')

    plt.legend()

    png_out = BytesIO()

    # save figure
    plt.savefig(png_out, format="png", bbox_inches="tight")
    plt.close()
    img_data = urllib.parse.quote(png_out.getvalue())

    return "data:image/png:base64," + img_data


if __name__ == '__main__':
    app.run(debug=True, port=5000)
