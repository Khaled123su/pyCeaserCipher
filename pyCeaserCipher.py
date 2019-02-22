#made by ThePyBeast

message = "SECRET" #the message that is going to be encrytped or decrypted
def encrypt():
	global t #the output
	global key #the encryption key
	o = [] #a list to get the characters
	key = 10000
	t = ""
	for letter in message:
		o.append(ord(letter)+key)
		
	for i in o:
			t += chr(i)
	print(t)
def decrypt():
	d = '' 
	k = []
	for letter in t:
		k.append(ord(letter)-key)
	for i in k:
		d += chr(i) 
	print(d)	
encrypt()
decrypt()
