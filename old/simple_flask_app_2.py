# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 20:31:36 2021

@author: ABC
"""

# ---------------------------------------------------------------
# Modules to be imported
# ---------------------------------------------------------------

from modules import *
from dashboard_library_basic import *
#from portfolio_library import *
from bokeh.resources import CDN
from bokeh.embed import file_html
import warnings
warnings.filterwarnings('ignore')


from bokeh.util.warnings import BokehUserWarning 
import warnings 
warnings.simplefilter(action='ignore', category=BokehUserWarning)



#-------------------------------------------------------------------------
# Start of dasboard app
#-------------------------------------------------------------------------

# Running flask app in browser
app = Flask(__name__)


# Different tab formation in browser
@app.route('/')
def home():
    return render_template('h1.html')

@app.route('/Run backtest')
def rb():
    return render_template('ts.html')

# Selection of time frame and SMA from dropdown
@app.route('/BacktestAnalysis',  methods=['POST'])
def user_rec2():
    tindicator = request.form.getlist('myDropDown1')    
    print('yes')
    mv_avg=request.form.getlist('ma1')
    dates = pd.date_range("20100101", periods=365)
    df1 = pd.DataFrame(np.random.randn(365, 4), index=dates, columns=list("ABCD"))
    sma=int(mv_avg[0])
    plot_list=[]
    df1.index=pd.to_datetime(df1.index)
    df=df1.tail(5)
    df2=pd.DataFrame(df['A']) #This shoud come from ajax
    print(df)

    plot_list.append(plot_table(df2))
    plot_list.append(plot_timeseries(df2,"Hello"))

    print('Good')
    a1 = layout([[plot_list[0]]], sizing_mode='fixed')
    a2 = layout([[plot_list[1]]], sizing_mode='fixed')

    #t1 = Panel(child=a1,title="Summary Statistics")
    #tab = Tabs(tabs=[t1]) 
    #save(tab)    
    layout1=column(a1,a2)
    #save(layout1)
    html1 = file_html(layout1, CDN, "Dashboard")
    return render_template("dummy3.html", text=html1)

if __name__ == '__main__':    
    app.run()
