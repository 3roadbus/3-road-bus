from pycat.base import NumpyImage
from pycat.core import Window

window = Window(height=360, width=750)

og_image = NumpyImage.get_array_from_file("k9da.png")

def extract_texture(image: NumpyImage, i: int, j:int, size: int) -> NumpyImage:
    start_col = i*size
    end_col = (i+1)*size
    start_row = j*size
    end_row = (j+1)*size
    array =image[start_col:end_col,start_row:end_row,:]
    texture = NumpyImage.get_texture_from_array(array)
    return texture

segment00 = window.create_sprite(x=90,y=90)
segment00.texture = extract_texture(og_image,0,0,180)
segment01 = window.create_sprite(x=270,y=90)
segment01.texture = extract_texture(og_image,0,1,180)
segment10 = window.create_sprite(x=90,y=270)
segment10.texture = extract_texture(og_image,1,0,180)
segment11 = window.create_sprite(x=270,y=270)
segment11.texture = extract_texture(og_image,1,1,180)

window.run()
