import cv2
import matplotlib.pyplot as plt

def gaussian_blur(image_path, kernel_size=5):
    # Görüntüyü oku
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Gaussian blurring uygula
    smoothed_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

    # Görselleştirme
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Orijinal Görüntü')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(smoothed_image, cmap='gray')
    plt.title('Gaussian Yumuşatma (Kernel Boyutu = {})'.format(kernel_size))
    plt.axis('off')

    plt.show()

# Örnek bir görüntü üzerinde Gaussian yumuşatma işlemi uygula
image_path = "apple.jpg"
gaussian_blur(image_path)


