import cv2
import matplotlib.pyplot as plt
import numpy as np


image_path = 'araba1.jpg'
color_image = cv2.imread(image_path)

if color_image is None:
    print(f'Hata: Görüntü "{image_path}" yüklenemedi.')
else:

    gray_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)


    plt.figure('Figure1')
    plt.imshow(gray_image, cmap='gray')
    plt.title('Orijinal Görüntü')
    plt.show()


    values = gray_image.flatten()
    histogram = [0] * 256
    for value in values:
        histogram[value] += 1


    plt.figure('Figure2')
    plt.bar(range(0, 256), histogram, color='gray', alpha=0.7)
    plt.title('Gri Seviye Görüntü Histogramı')
    plt.xlabel('Piksel Değeri')
    plt.ylabel('Sıklık')
    plt.show()
