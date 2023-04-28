import os

import cv2
import flask
from flask import render_template, request, redirect, url_for, flash, Flask, request, url_for, Response
from werkzeug.security import check_password_hash, generate_password_hash
from flask import request, g, redirect
from urllib.parse import urlparse, urljoin
from flask import request, jsonify
from PIL import Image, ImageFilter

from appController import app, controller


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    # Получение пути к изображению из формы
    path = request.form['img_path']
    img_path = os.path.abspath('appController') + '/' + path
    print(img_path)

    # Обработка изображения в зависимости от выбранного фильтра
    filter_type = request.form['filter']
    if filter_type == 'methodOne':
        binary_image = controller.otsu_threshold(img_path)
        _, img_encoded = cv2.imencode('.png', binary_image)
        img_bytes = img_encoded.tobytes()
        # возвращение бинарного изображения в виде HTTP-ответа
        return Response(response=img_bytes, content_type='image/png')
    elif filter_type == 'methodTwo':
        binary_image = controller.adaptive_threshold(img_path)
        _, img_encoded = cv2.imencode('.png', binary_image)
        img_bytes = img_encoded.tobytes()
        # возвращение бинарного изображения в виде HTTP-ответа
        return Response(response=img_bytes, content_type='image/png')
    elif filter_type == 'methodThree':
        binary_image = controller.operation_sum(img_path)
        _, img_encoded = cv2.imencode('.png', binary_image)
        img_bytes = img_encoded.tobytes()
        # возвращение бинарного изображения в виде HTTP-ответа
        return Response(response=img_bytes, content_type='image/png')
    elif filter_type == 'methodFour':
        binary_image = controller.operation_masked(img_path)
        _, img_encoded = cv2.imencode('.png', binary_image)
        img_bytes = img_encoded.tobytes()
        # возвращение бинарного изображения в виде HTTP-ответа
        return Response(response=img_bytes, content_type='image/png')
    elif filter_type == 'methodFive':
        binary_image = controller.operation_contrast(img_path)
        _, img_encoded = cv2.imencode('.png', binary_image)
        img_bytes = img_encoded.tobytes()
        # возвращение бинарного изображения в виде HTTP-ответа
        return Response(response=img_bytes, content_type='image/png')

    # Возвращение результата в виде HTML-страницы
    return render_template('result.html')
