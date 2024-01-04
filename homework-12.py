# Salt and pepper

import cv2
import numpy as np
import matplotlib.pyplot as plt

def add_salt_and_pepper_noise(image, salt_prob, pepper_prob):
    noisy_image = np.copy(image)
    total_pixels = image.size

    # Salt noise
    num_salt = np.ceil(salt_prob * total_pixels)
    salt_coords = [np.random.randint(0, i-1, int(num_salt)) for i in image.shape]
    noisy_image[salt_coords[0], salt_coords[1]] = 1

    # Pepper noise
    num_pepper = np.ceil(pepper_prob * total_pixels)
    pepper_coords = [np.random.randint(0, i-1, int(num_pepper)) for i in image.shape]
    noisy_image[pepper_coords[0], pepper_coords[1]] = 0

    return noisy_image

def median_filter(image, kernel_size=3):
    return cv2.medianBlur(image, kernel_size)

# Örnek bir görüntü üzerinde salt-and-pepper gürültüsü ekleyip giderme
image_path = "apple.jpg"
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Salt-and-pepper gürültü ekleyerek bir kopya oluştur
noisy_image = add_salt_and_pepper_noise(original_image, salt_prob=0.02, pepper_prob=0.02)

# Medyan filtresi uygula
denoised_image = median_filter(noisy_image, kernel_size=3)

# Görselleştirme
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(original_image, cmap='gray')
plt.title('Orijinal Görüntü')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(noisy_image, cmap='gray')
plt.title('Salt-and-Pepper Gürültülü Görüntü')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(denoised_image, cmap='gray')
plt.title('Medyan Filtre Sonrası')
plt.axis('off')

plt.show()
