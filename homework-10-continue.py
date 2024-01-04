import cv2
import numpy as np
import matplotlib.pyplot as plt

def laplacian_sharpening(image_path):
    # Görüntüyü oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Laplacian filtresi uygula
    laplacian = cv2.Laplacian(image, cv2.CV_64F)

    # Giriş ve çıkış dizilerinin türünü uygun hale getir
    image = image.astype(np.float64)
    sharpened_image = cv2.addWeighted(image, 1.5, laplacian, -0.5, 0)

    # Görselleştirme
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orijinal Görüntü')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(laplacian, cmap='gray')
    plt.title('Laplacian Filtre (Kenarlar)')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(sharpened_image, cmap='gray')
    plt.title('Keskinleştirme Sonrası')
    plt.axis('off')

    plt.show()

# Örnek bir görüntü üzerinde Laplacian keskinleştirme işlemi uygula
image_path = "apple.jpg"
laplacian_sharpening(image_path)
