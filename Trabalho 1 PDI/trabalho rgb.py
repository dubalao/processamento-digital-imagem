import numpy as np
import cv2

def cubo_RGB(face, i):
    if face < 1 or face > 6:
        raise ValueError("Face deve ser um valor entre 1 e 6")
    if i < 0 or i > 255:
        raise ValueError("O valor de i deve estar entre 0 e 255")

    # Criar uma matriz de zeros com forma 256x256x3 para representar a imagem
    image = np.zeros((256, 256, 3), dtype=np.uint8)

    if face == 1: 
        image[:, :, 1] = np.arange(256).reshape(1, 256)  
        image[:, :, 2] = np.arange(256).reshape(256, 1)  
        image[:, :, 0] = i 

    elif face == 2: 
        image[:, :, 0] = np.arange(256).reshape(256, 1)  
        image[:, :, 2] = np.arange(255,-1,-1).reshape(1, 256)  
        image[:, :, 1] = i 
        image = np.flipud(image)
    
    elif face == 3:
        image[:, :, 1] = np.arange(256).reshape(1, 256)  
        image[:, :, 2] = np.arange(256).reshape(256, 1)  
        image[:, :, 0] = 255-i

    elif face == 4: 
        image[:, :, 0] = np.arange(256).reshape(256, 1)  
        image[:, :, 2] = np.arange(255,-1,-1).reshape(1, 256)  
        image[:, :, 1] = 255-i  
        image = np.flipud(image)

    elif face == 5:
        image[:, :, 0] = np.arange(256).reshape(256, 1)  
        image[:, :, 1] = np.arange(256).reshape(1, 256)  
        image[:, :, 2] = 255-i  
        image = np.flipud(image)

    elif face == 6:
        image[:, :, 0] = np.arange(256).reshape(256, 1)  
        image[:, :, 1] = np.arange(256).reshape(1, 256)  
        image[:, :, 2] = i
        image = np.flipud(image)

    return image

# Parâmetros de entrada
face = 1  # Número da face (1 a 6)
i = 0     # Valor da i-ésima fatia (0 a 255)

# Gerar a fatia do cubo RGB com a primeira face escolhida
image = cubo_RGB(face, i)
image1 = cubo_RGB(face, i+85)
image2 = cubo_RGB(face, i+170)
image3 = cubo_RGB(face, i+255)

cv2.imshow(f'face {face}, fatia 0', image)
cv2.imshow(f'face {face}, fatia 85', image1)
cv2.imshow(f'face {face}, fatia 170', image2)
cv2.imshow(f'face {face}, fatia 255)', image3)

cv2.waitKey(0)

cv2.destroyAllWindows()