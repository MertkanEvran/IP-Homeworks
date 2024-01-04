# Sobel filtresi

import cv2
import numpy as np
import matplotlib.pyplot as plt

def sobel_filter(image_path):
    # Görüntüyü oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Sobel filtresi uygula
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)

    # Kenar büyüklüğünü hesapla
    edge_magnitude = np.sqrt(np.square(sobel_x) + np.square(sobel_y))

    # Görselleştirme
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orijinal Görüntü')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(sobel_x, cmap='gray')
    plt.title('Sobel X')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(sobel_y, cmap='gray')
    plt.title('Sobel Y')
    plt.axis('off')

    plt.show()

    # Kenar büyüklüğünü görselleştir
    plt.figure(figsize=(8, 5))
    plt.imshow(edge_magnitude, cmap='gray')
    plt.title('Kenar Büyüklüğü (Sobel)')
    plt.axis('off')
    plt.show()

# Örnek bir görüntü üzerinde Sobel filtre işlemi uygula
image_path = "apple.jpg"
sobel_filter(image_path)
