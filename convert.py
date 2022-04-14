from PIL import Image
import PIL 

# label_colours = [	(0,0,0), (128,0,0), (255,0,0), (0,85,0), (170,0,51), (255,85,0), (0,0,85), (0,119,221), 
#					(85,85,0), (0,85,85), (85,51,0), (52,86,128), (0,128,0), (0,0,255), (51,170,221), (0,255,255), 
#					(85,255,170), (170,255,85), (255,255,0), (255,170,0)]

# 0: Background		1: Hat			2: Hair			3: Glove		4: Sunglasses
# 5: Upper-clothes	6: Dress		7: Coat			8: Socks		9: Pants
# 10: tosor-skin	11: Scarf		12: Skirt		13: Face		14: Left-arm
# 15: Right-arm		16: Left-leg	17: Right-leg	18: Left-shoe	19: Right-shoe

src_img = "0.png"		# Source for palette, for quantizing images
target_img = ""
res_img = ""

src = Image.open(src_img)
target = Image.open(target_img)

res = target
print(src, res)

res = res.quantize(palette=src, kmeans=10, method=Image.FASTOCTREE)

for i in range(res.size[0]):
	for j in range(res.size[1]):
		if res.getpixel((i, j)) >= 20:		
			res.putpixel((i, j), 0)



print(src, res)

res.save(res_img)