# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 12:49:10 2021

@author: ABC
"""

from modules import *


path=os.getcwd()
path=path.replace('\\','/')

# Set tooltips for the hover tool 
TOOLTIPS = [
    ("(y)", "($y)"),
]


# Calling the required modules for processing



# ---------------------------------------------------------------
# a) Functions for plotting graphs in the dashboard
# ---------------------------------------------------------------

def plot_table(summary_table):
    '''
    This function gets the table containing all the summary statistics 
    '''
    Columns = [TableColumn(field=Ci, title=Ci) for Ci in summary_table.columns] # bokeh columns
    data_table = DataTable(columns=Columns, width=3550,height=900,source=ColumnDataSource(summary_table)) # bokeh table
    return data_table


def plot_stats(data,title):
    '''
    Plots the Bar plot of different summary statistics
    '''
    categories2 = list(data.index)
    data2 = list(data.values)
    sorted_assets = sorted(categories2, key=lambda x: data2[categories2.index(x)])
    p = figure(x_range=sorted_assets,tools="hover", tooltips=TOOLTIPS, plot_width=800, plot_height=300,title=str(title))
    p.vbar(x=categories2, top=data2, width=0.9,color=(Category20b)[16])
    p.xaxis.major_label_orientation = 1
    return p



def plot_timeseries(data,title):
    '''
    Gets the time series line plot of all the variables, where it highlights the portfolio and benchmark
    '''
    p = figure(plot_width=1200, plot_height=600,tools= "hover", tooltips=TOOLTIPS, x_axis_type="datetime")
    p.title.text = str(title)+ '. Click on legend entries to hide the corresponding lines'    
    for col,col2 in zip(list(data.columns),(Category20b)[16]):
        df2=pd.DataFrame(data[[col]])
        df2['date']=df2.index        
        if col=='Portfolio':
            p.circle(df2['date'], df2[col],line_width=6, color="red", alpha=0.8, legend=col)
            

        
        p.line(df2['date'], df2[col], line_width=2, color=col2, alpha=0.8, legend=col)        
    p.legend.location = "top_left"
    p.legend.click_policy="hide" 
    return p
