import cv2
import numpy as np


def otsu_threshold(image_path):
    # Загрузка изображения
    image = cv2.imread(image_path)
    # Преобразование изображения в градации серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Вычисление порога методом Оцу
    _, thresholded = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    return thresholded


def adaptive_threshold(image_path, block_size=11, constant=2):
    # Загрузка изображения
    image = cv2.imread(image_path)
    # Преобразование изображения в градации серого
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Применение метода адаптивной пороговой обработки
    thresholded = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, constant)
    # Сохранение порогового изображения в файл
    return thresholded


def operation_sum(image_path):
    # Загрузка изображения
    image = cv2.imread(image_path)

    blue = image[:, :, 0]
    image_sum = cv2.add(image, (255, 0, 0, 0))
    # Сохранение результатов
    cv2.imwrite('output_sum.jpg', image_sum)

    return image_sum


def operation_masked(image_path):
    image = cv2.imread(image_path)

    # Поэлементное умножение изображения на маску (mask)
    mask = np.ones(image.shape, dtype=np.uint8) * 100
    image_masked = cv2.multiply(image, mask)
    cv2.imwrite('output_masked.jpg', image_masked)

    return image_masked


def operation_contrast(image_path):
    image = cv2.imread(image_path)

    # Линейное контрастирование изображения
    alpha = 1.5  # коэффициент контраста
    beta = 50  # коэффициент яркости
    image_contrast = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    cv2.imwrite('output_contrast.jpg', image_contrast)

    return image_contrast
