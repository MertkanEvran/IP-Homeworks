#

import cv2
import numpy as np
import matplotlib.pyplot as plt

def rgb_slice(image_path, lower_threshold, upper_threshold):
    # Görüntüyü oku
    image = cv2.imread(image_path)

    # Renk bölütlenmesi yap
    mask = cv2.inRange(image, lower_threshold, upper_threshold)
    result = cv2.bitwise_and(image, image, mask=mask)

    # Görselleştirme
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 3, 1)
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Orijinal Görüntü')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(mask, cmap='gray')
    plt.title('Maske')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    plt.title('Bölütlenmiş Görüntü')
    plt.axis('off')

    plt.show()

# Örnek bir görüntü üzerinde RGB bölütlenme uygula
image_path = "apple.jpg"

# Alt ve üst renk eşik değerleri
lower_threshold = np.array([0, 0, 100])
upper_threshold = np.array([50, 50, 255])

rgb_slice(image_path, lower_threshold, upper_threshold)
