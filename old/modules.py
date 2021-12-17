
import numpy as np
import math
from math import pi
import pandas as pd
import os
import datetime


from bokeh.models.widgets import DataTable, DateFormatter, TableColumn
from bokeh.palettes import Viridis6 as palette
from bokeh.palettes import Dark2_5
from bokeh.transform import factor_cmap
from bokeh.models import ColumnDataSource,FactorRange,HoverTool
from bokeh.palettes import Spectral6
from bokeh.plotting import figure, show, output_file,save
from bokeh.embed import components,file_html
from bokeh.resources import CDN
from bokeh.layouts import row,column
from bokeh.palettes import Category20b
from bokeh.models.widgets import Tabs, Panel
from bokeh.io import curdoc
from bokeh.layouts import layout
from bokeh.core.properties import value
from bokeh.palettes import Category20c
from bokeh.transform import cumsum



from flask import Flask, request, render_template, session, redirect,send_file
import webbrowser
from threading import Timer
from collections import defaultdict