# Gaussion filtresi

import cv2
import numpy as np
import matplotlib.pyplot as plt

def gaussian_filter(image_path, kernel_size=3, sigma=1.0):
    # Görüntüyü oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Gaussian filtresi uygula
    filtered_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), sigma)

    # Görselleştirme
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orijinal Görüntü')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(filtered_image, cmap='gray')
    plt.title('Gaussian Filtre Sonrası (Kernel Boyutu = {}, Sigma = {})'.format(kernel_size, sigma))
    plt.axis('off')

    plt.show()

# Örnek bir görüntü üzerinde Gaussian filtre işlemi uygula
image_path = "apple.jpg"
gaussian_filter(image_path, kernel_size=5, sigma=1.5)
