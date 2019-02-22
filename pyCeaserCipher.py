message = "SECRET"
def encrypt():
	global t
	global key
	o = []
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
#decrypt()