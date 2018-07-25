import numpy as np
import os
from PIL import Image
import click
import argparse
from model import generator_model
from utils import load_image, deprocess_image, preprocess_image

def deblur(image_path):
    data = {
        'A_paths': [image_path],
        'A': np.array([preprocess_image(load_image(image_path))])
    }
    x_test = data['A']
    g = generator_model()
    g.load_weights('generator.h5')
#    g.load_weights('weights/719/generator_2_640.h5')
    generated_images = g.predict(x=x_test)
    generated = np.array([deprocess_image(img) for img in generated_images])
    x_test = deprocess_image(x_test)
    for i in range(generated_images.shape[0]):
        x = x_test[i, :, :, :]
        img = generated[i, :, :, :]
        im = Image.fromarray(img.astype(np.uint8))
        im.save('deblur'+image_path)

def deblur_command(image_folder):
    #imagelist = []
    for parent, dirnames, filenames in os.walk(image_folder):
    	for filename in filenames:
            deblur(os.path.join(parent, filename))
            print('Deblurred: '+filename)

if __name__ == "__main__":
    deblur_command('PATCHES')
