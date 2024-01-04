import cv2
import numpy as np
import matplotlib.pyplot as plt

def mean_filter(image_path, kernel_size=3):
    # Görüntüyü oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Ortalama filtresi uygula
    filtered_image = cv2.blur(image, (kernel_size, kernel_size))

    # Görselleştirme
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orijinal Görüntü')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(filtered_image, cmap='gray')
    plt.title('Ortalama Filtre Sonrası (Kernel Boyutu = {})'.format(kernel_size))
    plt.axis('off')

    plt.show()

# Örnek bir görüntü üzerinde ortalama filtre işlemi uygula
image_path = "apple.jpg"
mean_filter(image_path, kernel_size=5)