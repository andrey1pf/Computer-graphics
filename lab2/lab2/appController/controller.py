import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import os
from math import log2, ceil


pathCheck = ['/Users/andrey_pf/Desktop/workspace/semester6/cg6sem/lab2/lab2/appController/forCheckLab2']
pathJpg = ['/Users/andrey_pf/Desktop/workspace/semester6/cg6sem/lab2/lab2/appController/forCheckJpg']
pathGif = ['/Users/andrey_pf/Desktop/workspace/semester6/cg6sem/lab2/lab2/appController/forCheckGif']
pathTif = ['/Users/andrey_pf/Desktop/workspace/semester6/cg6sem/lab2/lab2/appController/forCheckTif']
pathBmp = ['/Users/andrey_pf/Desktop/workspace/semester6/cg6sem/lab2/lab2/appController/forCheckBmp']
pathPng = ['/Users/andrey_pf/Desktop/workspace/semester6/cg6sem/lab2/lab2/appController/forCheckPng']
pathPcx = ['/Users/andrey_pf/Desktop/workspace/semester6/cg6sem/lab2/lab2/appController/forCheckPcx']

image_list_check = []
image_list_jpg = []
image_list_gif = []
image_list_tif = []
image_list_bmp = []
image_list_png = []
image_list_pcx = []


class Img:
    def __init__(self, path_arr):
        self.path = os.path.join(*path_arr)
        img = Image.open(self.path)
        self.image = img.copy()
        img.close()
        self.name = path_arr[-1]

    def get_name(self):
        return self.name

    def get_size(self):
        return self.image.size

    def get_depth(self):
        temp = self.image.getextrema()
        if isinstance(temp[0], tuple):
            ans = max(i[1] for i in temp)
            return ceil(log2(ans)) * len(temp)
        else:
            ans = max(temp)
            return ceil(log2(ans))

    def get_entropy(self):
        return self.image.entropy()

    def get_dpi(self):
        sz = self.get_size()
        return min(sz[0] * sz[1] // ((13 * 2.54) ** 2), 90.0)


def check_check():
    for file_name in os.listdir(os.path.join(*pathCheck)):
        pathCheck.append(file_name)
        image_list_check.append(Img(pathCheck))
        pathCheck.pop()


def check_jpg():
    for file_name in os.listdir(os.path.join(*pathJpg)):
        pathJpg.append(file_name)
        image_list_jpg.append(Img(pathJpg))
        pathJpg.pop()


def check_gif():
    for file_name in os.listdir(os.path.join(*pathGif)):
        pathGif.append(file_name)
        image_list_gif.append(Img(pathGif))
        pathGif.pop()


def check_tif():
    for file_name in os.listdir(os.path.join(*pathTif)):
        pathTif.append(file_name)
        image_list_tif.append(Img(pathTif))
        pathTif.pop()


def check_bmp():
    for file_name in os.listdir(os.path.join(*pathBmp)):
        pathBmp.append(file_name)
        image_list_bmp.append(Img(pathBmp))
        pathBmp.pop()


def check_png():
    for file_name in os.listdir(os.path.join(*pathPng)):
        pathPng.append(file_name)
        image_list_png.append(Img(pathPng))
        pathPng.pop()


def check_pcx():
    for file_name in os.listdir(os.path.join(*pathPcx)):
        pathPcx.append(file_name)
        image_list_pcx.append(Img(pathPcx))
        pathPcx.pop()


def ret(type_folder):
    if type_folder == 'Bmp':
        check_bmp()
        return image_list_bmp
    elif type_folder == 'Gif':
        check_gif()
        return image_list_gif
    elif type_folder == 'Jpg':
        check_jpg()
        return image_list_jpg
    elif type_folder == 'Lab2':
        check_check()
        return image_list_check
    elif type_folder == 'Pcx':
        check_pcx()
        return image_list_pcx
    elif type_folder == 'Png':
        check_png()
        return image_list_png
    elif type_folder == 'Tif':
        check_tif()
        return image_list_tif

    return []
