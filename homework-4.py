# Contrast stretching

import cv2
import numpy as np
import matplotlib.pyplot as plt

def contrast_stretching(image_path):
    # Görüntüyü oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Kontrast genişletme işlemi uygula
    min_val = np.min(image)
    max_val = np.max(image)

    stretched_image = 255 * ((image - min_val) / (max_val - min_val))

    # Görselleştirme
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orijinal Görüntü')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(stretched_image, cmap='gray', vmin=0, vmax=255)
    plt.title('Kontrast Genişletme Sonrası')
    plt.axis('off')

    plt.show()

# Örnek bir görüntü üzerinde kontrast genişletme işlemi uygula
image_path = "apple.jpg"
contrast_stretching(image_path)