# Blurring operation with Laplace

import cv2
import numpy as np
import matplotlib.pyplot as plt

def laplacian_blur(image_path):
    # Görüntüyü oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Gaussian blurring uygula
    blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

    # Laplacian filtresi uygula
    laplacian = cv2.Laplacian(blurred_image, cv2.CV_64F)

    # Görselleştirme
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orijinal Görüntü')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(blurred_image, cmap='gray')
    plt.title('Gaussian Bulanıklık')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(laplacian, cmap='gray')
    plt.title('Laplacian Filtre (Kenarlar)')
    plt.axis('off')

    plt.show()

# Örnek bir görüntü üzerinde Laplacian blurring işlemi uygula
image_path = "apple.jpg"
laplacian_blur(image_path)
