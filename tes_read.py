import base64

tmp_str = None

with open("cat.jpg","rb") as imageFile:
	tmp_str = base64.b64encode(imageFile.read())
	#print(tmp_str)

fh = open("imageToSave.jpeg", "wb")
fh.write(base64.b64decode(tmp_str))
fh.close()
	
