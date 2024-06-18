import pdf2image
from PIL import Image


def process_input(input_path):
    if input_path.endswith('.pdf'):
        imgs_list = pdf2image.convert_from_path(input_path)
    else:
        imgs_list = [Image.open(input_path)]
    
    return imgs_list
