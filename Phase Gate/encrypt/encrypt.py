def encrypt_text(text):
	lower_case = "abcdefghijklmnopkrstuvwkyz"
	
	alphabets = {"a": "n", "b": "o", "c": "p", "d": "q", "e": "r", "f": "s", "g": "t", "h": "u", "i": "v", "j": "w", "k": "x", "l": "y", "m": "z", "n": "a", "o": "b", "p": "c", "q": "d", "r": "e", "s": "f", "t": "g", "u": "h", "v": "i", "w": "j", "x": "k", "y": "l", "z": "m", }
	
	new = ""


	for char in text:
		if char in alphabets:
			new += alphabets[char]
			
	return new
	
	
	
	