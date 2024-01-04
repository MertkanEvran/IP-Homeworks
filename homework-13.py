#

import cv2
import numpy as np
import matplotlib.pyplot as plt

def contraharmonic_mean_filter(image_path, kernel_size, Q):
    # Görüntüyü oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Contraharmonic Mean filtresi uygula
    filtered_image = cv2.filter2D(image, -1, np.ones((kernel_size, kernel_size), np.float32) / (kernel_size**2))
    numerator = cv2.filter2D(image**(Q+1), -1, np.ones((kernel_size, kernel_size), np.float32) / (kernel_size**2))
    denominator = cv2.filter2D(image**Q, -1, np.ones((kernel_size, kernel_size), np.float32) / (kernel_size**2))
    filtered_image = numerator / denominator

    # Görselleştirme
    plt.figure(figsize=(15, 5))

    plt.subplot(1, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orijinal Görüntü')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(filtered_image, cmap='gray')
    plt.title('Contraharmonic Mean Filtre (Q={})'.format(Q))
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(filtered_image.astype(np.uint8), cmap='gray')
    plt.title('Sonuç (UInt8)')
    plt.axis('off')

    plt.show()

# Örnek bir görüntü üzerinde Contraharmonic Mean filtresi uygula
image_path = "apple.jpg"
contraharmonic_mean_filter(image_path, kernel_size=3, Q=1.5)