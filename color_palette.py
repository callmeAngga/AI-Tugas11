import numpy as np
from PIL import Image
from sklearn.cluster import KMeans

def get_palette(image, num_colors=5):
    image = image.resize((150, 150))
    image_np = np.array(image)
    
    pixels = image_np.reshape((-1, 3))
    
    kmeans = KMeans(n_clusters=num_colors)
    kmeans.fit(pixels)
    
    colors = kmeans.cluster_centers_.astype(int)
    return colors
