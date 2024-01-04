import cv2
import numpy as np
import matplotlib.pyplot as plt

def opening(image_path, kernel_size=3):
    # Görüntüyü siyah-beyaz (ikili) hale getir
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Yapılandırma elemanını oluştur
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    # Açma işlemi uygula
    opened_image = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

    # Görselleştirme
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orijinal Görüntü')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(kernel, cmap='gray')
    plt.title('Yapılandırma Elemanı')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(opened_image, cmap='gray')
    plt.title('Açma İşlemi Sonrası')
    plt.axis('off')

    plt.show()

# Örnek bir görüntü üzerinde açma işlemi uygula
image_path = "apple.jpg"
opening(image_path, kernel_size=5)

def closing(image_path, kernel_size=3):
    # Görüntüyü siyah-beyaz (ikili) hale getir
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Yapılandırma elemanını oluştur
    kernel = np.ones((kernel_size, kernel_size), np.uint8)

    # Kapama işlemi uygula
    closed_image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)

    # Görselleştirme
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orijinal Görüntü')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(kernel, cmap='gray')
    plt.title('Yapılandırma Elemanı')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(closed_image, cmap='gray')
    plt.title('Kapama İşlemi Sonrası')
    plt.axis('off')

    plt.show()

# Örnek bir görüntü üzerinde kapama işlemi uygula
image_path = "apple.jpg"
closing(image_path, kernel_size=5)