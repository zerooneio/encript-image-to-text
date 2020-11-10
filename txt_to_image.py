import base64

print("TEXT to IMAGE")
setring = input("masukan nama text.format(txt/dll) ! harus satu folder \n-> ")
gambar = input("simpan nama gambar+format -> ")
tmp_str = None

with open(setring, "rb") as setringFile:
	tmp_str = setringFile.read()

with open(gambar, "wb") as gambarFile:
	gambarFile.write(base64.b64decode(tmp_str))
