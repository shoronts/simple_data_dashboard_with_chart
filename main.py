from flask import Flask, request, render_template, jsonify, redirect
from flask.helpers import url_for
import pandas as pd
import numpy as np


# Running flask app in browser
app = Flask(__name__)

# Different tab formation in browser
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/dashboard', methods=['GET','POST'])
def dashboard():
    if request.method == 'POST':
        # Recinving Values from AJAX
        get_data = request.json
        # print(get_data['alpha'])
        # print(get_data['average'])

        # Making DATA by Pandas
        data_lists = list("ABCD")
        dates = pd.date_range("20100101", periods=365)
        random_data = pd.DataFrame(np.random.randn(365, 4), index=dates, columns=data_lists)
        random_data.index=pd.to_datetime(random_data.index)
        data_fream=random_data.tail(5)

        # Find the request type
        try:
            next_data = get_data['changeData']
            is_ajax_request = True

        except:
            next_data = 'A'
            is_ajax_request = False

        # Final data for user
        data_fream_final=pd.DataFrame(data_fream[next_data]) #This coming from ajax

        # Collecting All Values from Final Datas
        all_values = []
        for val in data_fream_final.values.tolist():
            all_values.append(str(val)[1:-1])

        # Collecting All Dates From Final Datas
        all_dates = []
        for dates in data_fream_final.index:
            pd_to_date = dates.to_pydatetime().strftime("%m/%d/%Y, %H:%M:%S")
            all_dates.append(pd_to_date.split(',')[0])

        # Data sending to the user
        if is_ajax_request:
            return jsonify({'values':all_values,'dates':all_dates})
        else:
            return render_template("analysis.html",lists=data_lists,dates=all_dates,values=all_values)
    else:
        return render_template('dashboard.html')


@app.route('/download-data', methods=['GET','POST'])
def download_data():
    # Making DATA by Pandas
    data_lists = list("ABCD")
    dates = pd.date_range("20100101", periods=365)
    random_data = pd.DataFrame(np.random.randn(365, 4), index=dates, columns=data_lists)
    random_data.index=pd.to_datetime(random_data.index)
    data_fream=random_data.tail(5)
    data_fream.to_excel("abc.xlsx")
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True, host='0.0.0.0', port='8000')
