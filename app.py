from flask import Flask, request, render_template
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import urllib
from io import BytesIO

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/plot')
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
    maxmin_num = request.args.get('maxmin_num', type=int)
    areas = [area1, area2, area3]
    maxmin_colors = [maxmin_color1, maxmin_color2, maxmin_color3]
    maxmin_years = [maxmin_year1, maxmin_year2, maxmin_year3]

    # scatter plot
    for i in range(maxmin_num):
        # read csv
        df = pd.read_csv('/data/{0}/maxmin_{1}.csv'.format(areas[i],
                         maxmin_years[i]), skiprows=6, header=None)
        max_temp = df.iloc[:, 1]
        min_temp = df.iloc[:, 4]

        # scatter plot
        fig, ax = plt.subplots(1, 1)
        ax.scatter(min_temp, max_temp, c=maxmin_colors[i])

        png_out = BytesIO()

    # save figure
    plt.savefig(png_out, format="png", bbox_inches="tight")
    plt.close()
    img_data = urllib.parse.quote(png_out.getvalue())

    return "data:image/png:base64," + img_data


if __name__ == '__main__':
    app.run(debug=True, port=5000)
