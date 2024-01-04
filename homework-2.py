# Bit plane slicing

import cv2
import numpy as np
import matplotlib.pyplot as plt

def bit_plane_slicing(image_path):
    # Görüntüyü oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Görüntü boyutları
    rows, cols = image.shape

    # Her bir bit düzeyini ayrı ayrı görselleştir
    for i in range(8):
        # 2^i'inci biti çıkar
        bit_plane = np.bitwise_and(image, 2**i)

        # Görselleştirme
        plt.subplot(2, 4, i + 1)
        plt.imshow(bit_plane, cmap='gray')
        plt.title('Bit ' + str(7 - i))  # 7'den başlayarak sırala
        plt.xticks([]), plt.yticks([])

    plt.show()

# Örnek bir görüntü üzerinde bit plane slicing işlemi uygula
image_path = "apple.jpg"
bit_plane_slicing(image_path)