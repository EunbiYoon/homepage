from flask import Flask, render_template
from flask import Flask,render_template,request,redirect
import io
from flask import Flask, render_template, Response
from matplotlib.figure import Figure
import io
import random
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
import matplotlib.pyplot as plt

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/service')
def word():
    return render_template("service.html")

