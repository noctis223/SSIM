import numpy as np
from skimage import img_as_float
from skimage.metrics import structural_similarity as ssim

# Leggi la prima immagine dall'input utente
data = input('Inserisci i dati della prima immagine: ')

# Converti i dati in un array NumPy
image1 = np.fromstring(data, sep=' ').reshape((512, 512))

# Leggi la seconda immagine dall'input utente
data = input('Inserisci i dati della seconda immagine: ')

# Converti i dati in un array NumPy
image2 = np.fromstring(data, sep=' ').reshape((512, 512))

# Converte le immagini in float
image1 = img_as_float(image1)
image2 = img_as_float(image2)

# Calcola l'indice SSIM tra le due immagini
index = ssim(image1, image2)

# Stampa il risultato
print(f"SSIM index: {index}")