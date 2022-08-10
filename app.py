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
import plot3

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/service')
def word():
    return render_template("service.html")

@app.route('/verify', methods = ['POST', 'GET'])
def verify():
    if request.method == 'POST':
        fig = plot3.create_figure()
        output = io.BytesIO()
        FigureCanvas(fig).print_png(output)
        return Response(output.getvalue(), mimetype='image/png')

