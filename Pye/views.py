from django.shortcuts import render
from django.http import HttpResponse

from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.dates import DateFormatter
import matplotlib.pyplot as plt

import random
import datetime
import math
REMOTE_HOST = "https://pyecharts.github.io/assets/js"
def Pyebar(request):
    return render(request, 'pycharts.html')

