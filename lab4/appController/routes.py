import os

import flask
from flask import render_template, request, redirect, url_for, flash, Flask, request, url_for, Response
from werkzeug.security import check_password_hash, generate_password_hash
from flask import request, g, redirect
from urllib.parse import urlparse, urljoin
from flask import request, jsonify
import matplotlib.pyplot as plt

from appController import app, controller


@app.route('/', methods=['GET', 'POST'])
def home():
    x1, x2, y1, y2, x, y, r = 0, 0, 0, 0, 0, 0, 0

    if request.method == 'GET':
        return render_template('index.html'), 200

    if request.method == 'POST':
        method = request.form['method']
        if method == 'okr':
            x, y, r = int(request.form['x']), int(request.form['y']), int(request.form['r'])
            points = list(controller.bresenham_circle_algorithm(x, y, r))
            x_values = [point[0] for point in points]
            y_values = [point[1] for point in points]
            plt.scatter(x_values, y_values)
            plt.gca().set_aspect('equal', adjustable='box')
            plt.savefig('/Users/andrey_pf/Desktop/workspace/semester6/cg6sem/lab4/appController/static/images/res.png')
            plt.show()
        else:
            x1 = int(request.form['x1'])
            x2 = int(request.form['x2'])
            y1 = int(request.form['y1'])
            y2 = int(request.form['y2'])
            if method == 'brez':
                points = list(controller.bresenham_algorithm(x1, y1, x2, y2))
                x_values = [point[0] for point in points]
                y_values = [point[1] for point in points]
                plt.plot(x_values, y_values)
            elif method == 'cda':
                points = controller.cda_algorithm(x1, y1, x2, y2)
                x_values = [point[0] for point in points]
                y_values = [point[1] for point in points]
                plt.plot(x_values, y_values)
            elif method == 'step':
                points = controller.step_by_step_algorithm(x1, y1, x2, y2)
                x_values = [point[0] for point in points]
                y_values = [point[1] for point in points]
                plt.plot(x_values, y_values)
            plt.savefig('/Users/andrey_pf/Desktop/workspace/semester6/cg6sem/lab4/appController/static/images/res.png')
            plt.show()

        return render_template('index.html')

    return render_template('index.html'), 200
