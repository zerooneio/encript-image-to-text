import base64

print("IMAGE to TEXT")
gambar = input("masukan nama gambar.format(png/dll) ! harus satu folder \n-> ")
setring = input("nama text.txt -> ")
tmp_str = None

with open(gambar,"rb") as imageFile:
	tmp_str = base64.b64encode(imageFile.read())

with open(setring, "wb") as setringFile:
	setringFile.write(tmp_str)
	
