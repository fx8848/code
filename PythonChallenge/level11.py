#http://www.pythonchallenge.com/pc/return/5808.html
import Image

img = Image.open('level11.jpg')
width, height = img.size
odd = even = Image.new(img.mode, (width, height))
for x in range(width):
	for y in range(height):
		pixel = img.getpixel((x, y))
		thex = x/2 if x%2 == 0 else (x-1)/2
		they = y/2 if y%2 == 0 else (y-1)/2
		if x%2 == y%2:
			even.putpixel((thex, they), pixel)
		else:
			odd.putpixel((thex, they), pixel)
odd.show()
even.show()
