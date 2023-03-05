import flask
from flask import render_template, request, redirect, url_for, flash, Flask, request, url_for
from werkzeug.security import check_password_hash, generate_password_hash
from flask import request, g, redirect
from urllib.parse import urlparse, urljoin
from flask import request, jsonify

from colorController import app, converter


@app.route('/', methods=['GET', 'POST'])
def index():
    color = {
        'c': 0,
        'm': 0,
        'y': 0,
        'k': 0,
        'r': 0,
        'g': 0,
        'b': 0,
        'h': 0,
        'l': 0,
        's': 0,
        'status': False
    }

    if request.method == 'POST':
        button_id = request.form.get('button')
        c1 = request.form['cmyk1']
        m1 = request.form['cmyk2']
        y1 = request.form['cmyk3']
        k1 = request.form['cmyk4']
        r2 = request.form['rgb1']
        g2 = request.form['rgb2']
        b2 = request.form['rgb3']
        h3 = request.form['hls1']
        l3 = request.form['hls2']
        s3 = request.form['hls3']

        if button_id == 'cmyk':
            r1, g1, b1 = converter.cmyk_to_rgb(c1, m1, y1, k1)
            h1, l1, s1 = converter.cmyk_to_hls(c1, m1, y1, k1)

            if (r1 == -1 and g1 == -1 and b1 == -1) or (h1 == -1 and l1 == -1 and s1 == -1):
                color = {
                    'c': c1,
                    'm': m1,
                    'y': y1,
                    'k': k1,
                    'r': r2,
                    'g': g2,
                    'b': b2,
                    'h': h3,
                    'l': l3,
                    's': s3,
                    'status': True
                }
                return render_template('index.html', color=color)

            color = {
                'c': c1,
                'm': m1,
                'y': y1,
                'k': k1,
                'r': r1,
                'g': g1,
                'b': b1,
                'h': h1,
                'l': l1,
                's': s1,
                'status': False
            }

            return render_template('index.html', color=color)

        elif button_id == 'rgb':
            c2, m2, y2, k2 = converter.rgb_to_cmyk(r2, g2, b2)
            h2, l2, s2 = converter.rgb_to_hls(r2, g2, b2)

            if (c2 == -1 and m2 == -1 and y2 == -1 and k2) or (h2 == -1 and l2 == -1 and s2 == -1):
                color = {
                    'c': c1,
                    'm': m1,
                    'y': y1,
                    'k': k1,
                    'r': r2,
                    'g': g2,
                    'b': b2,
                    'h': h3,
                    'l': l3,
                    's': s3,
                    'status': True
                }
                return render_template('index.html', color=color)

            color = {
                'c': c2,
                'm': m2,
                'y': y2,
                'k': k2,
                'h': h2,
                'l': l2,
                's': s2,
                'r': r2,
                'g': g2,
                'b': b2,
                'status': False
            }

            return render_template('index.html', color=color)
        else:
            r3, g3, b3 = converter.hls_to_rgb(h3, l3, s3)
            c3, m3, y3, k3 = converter.hls_to_cmyk(h3, l3, s3)

            if (r3 == -1 and g3 == -1 and b3 == -1) or (c3 == -1 and m3 == -1 and y3 == -1 and k3):
                color = {
                    'c': c1,
                    'm': m1,
                    'y': y1,
                    'k': k1,
                    'r': r2,
                    'g': g2,
                    'b': b2,
                    'h': h3,
                    'l': l3,
                    's': s3,
                    'status': True
                }
                return render_template('index.html', color=color)

            color = {
                'c': c3,
                'm': m3,
                'y': y3,
                'k': k3,
                'r': r3,
                'g': g3,
                'b': b3,
                'h': h3,
                'l': l3,
                's': s3,
                'status': False
            }

            return render_template('index.html', color=color)

    return render_template('index.html', color=color)
