import os

import flask
from flask import render_template, request, redirect, url_for, flash, Flask, request, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flask import request, g, redirect
from urllib.parse import urlparse, urljoin
from flask import request, jsonify

from appController import app, controller, check_type
from appController.controller import Img


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        folder_path = request.form['folder-path']
        type_folder = check_type.check_type(folder_path)
        table = []
        if type_folder == 'Bmp':
            table = controller.ret('Bmp')
        elif type_folder == 'Gif':
            table = controller.ret('Gif')
        elif type_folder == 'Jpg':
            table = controller.ret('Jpg')
        elif type_folder == 'Lab2':
            table = controller.ret('Lab2')
        elif type_folder == 'Pcx':
            table = controller.ret('Pcx')
        elif type_folder == 'Png':
            table = controller.ret('Png')
        elif type_folder == 'Tif':
            table = controller.ret('Tif')

        file_data = []
        for file in range(len(table)):
            file_name = Img.get_name(table[file])
            file_size = Img.get_size(table[file])
            file_dpi = Img.get_dpi(table[file])
            file_depth = Img.get_depth(table[file])
            file_entropy = Img.get_entropy(table[file])
            file_data.append((file_name, file_size, file_dpi, file_depth, file_entropy))
        return render_template('index.html', file_data=file_data)
    return render_template('index.html')
