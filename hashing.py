import hashlib as hl

def start_dat():
	option = input("Test for hash or Make a hash? (t or m): ")
	if option.lower() == "t":
		t = open("password.txt", "r")
		text = input("What's the password?: ")
		hash_text = hl.md5(text.encode())
		if t.read() == hash_text.hexdigest():
			input("Welcome User.")
			start_dat()
		else:
			print("Wrong.")
			if t.read() != "":
				print(t.read() + "   FILE")
			input(hash_text.hexdigest() + "   HASHED")
			start_dat()
	elif option.lower() == "m":
		text = input("What would you like to hash?: ")
		hash_text = hl.md5(text.encode())
		t = open("password.txt", "w+")
		t.write(hash_text.hexdigest())
		t.flush()
		start_dat()
	else:
		print("Nope")
		start_dat()

if __name__ == "__main__":
	start_dat()

