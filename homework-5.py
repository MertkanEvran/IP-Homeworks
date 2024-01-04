# Gama

import cv2
import numpy as np
import matplotlib.pyplot as plt

def gamma_correction(image_path, gamma=1.0):
    # Görüntüyü oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Gamma düzeltme işlemi uygula
    corrected_image = np.power(image / 255.0, gamma) * 255.0

    # Görselleştirme
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orijinal Görüntü')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(corrected_image, cmap='gray', vmin=0, vmax=255)
    plt.title('Gamma Düzeltme Sonrası (Gamma = {})'.format(gamma))
    plt.axis('off')

    plt.show()

# Örnek bir görüntü üzerinde gamma düzeltme işlemi uygula
image_path = "apple.jpg"
gamma_correction(image_path, gamma=2)