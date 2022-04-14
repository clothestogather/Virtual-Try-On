from PIL import Image
import PIL
import math

src_img = "sample003.png"
res_img = "sample03.jpg"

image = Image.open(src_img)

image = image.convert('RGB')

fixed_height = 1024
height_percent = (fixed_height / float(image.size[1]))
width_size = int((float(image.size[0]) * float(height_percent)))
image = image.resize((width_size, fixed_height), PIL.Image.NEAREST)

if image.size[0] > 768:
	res = image.crop((int((image.size[0] - 768) / 2), 0, int((image.size[0] - 768) / 2) + 768, 1024))
else:
	res = Image.new(image.mode, (768, 1024), (255, 255, 255))
	res.paste(image, (int((768 - width_size) / 2), 0))

res.save(res_img)

print(res.size)