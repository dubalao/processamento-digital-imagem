import cv2
import numpy as np

def high_boost_filter(image, k):
    # Aplicar um filtro passa-baixa (filtro de média 5x5)
    kernel = np.ones((5, 5), np.float32) / 25
    
    blur_image = cv2.filter2D(image, -1, kernel)

    cv2.imwrite(f'blur{k} {image_path}', blur_image)

    # Calcular a mascara
    mask = cv2.subtract(image, blur_image)
    cv2.imwrite(f'mask{k} {image_path}', mask)
    
    # Aplicar o fator de amplificação (k)
    scaled_mask = cv2.convertScaleAbs(mask, alpha=k)
    boosted_image = cv2.add(image, scaled_mask)
    
    #garante q os valores estao em um intervalo valido 
    boosted_image = np.clip(boosted_image, 0, 255).astype(np.uint8)

    return boosted_image

# Carregar a imagem 

#image_path = 'original.jpg'
image_path = 'lua.jpg'
image = cv2.imread(image_path, 0)

# Aplicar a filtragem high-boost
k = 3.5

boosted_image = high_boost_filter(image, k)
cv2.imshow('Original', image)
cv2.imshow(f'High-Boost (k={k})', boosted_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Salvar a imagem
cv2.imwrite(f'hb k={k} {image_path}', boosted_image)
