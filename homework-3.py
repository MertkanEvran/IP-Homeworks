# Histogram eşitleme

import cv2
import numpy as np
import matplotlib.pyplot as plt

def histogram_equalization(image_path):
    # Görüntüyü oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Histogram eşitleme işlemi uygula
    equalized_image = cv2.equalizeHist(image)

    # Görselleştirme
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orijinal Görüntü')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(equalized_image, cmap='gray')
    plt.title('Histogram Eşitleme Sonrası')
    plt.axis('off')

    plt.show()

# Örnek bir görüntü üzerinde histogram eşitleme işlemi uygula
image_path = "apple.jpg"
histogram_equalization(image_path)