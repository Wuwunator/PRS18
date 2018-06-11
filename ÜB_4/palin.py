# Wencke Hartwig
# 790786
# Uebungsblatt 4

# 1 Stringverarbeitung
# 1.2 Palindrome

#definition der funktion is_palindrome
def is_palindrome(p) :
	#wenn der eingegebene string kleiner 2also 0 oder 1 Zeichen lang ist, dann ist es ein Palindrom/True
	if len(p) < 2 :
		return True
	#wenn der eingegebene string grösser 2 ist, dann vergleiche jeweils das erste und letzte zeichen des strings, setze dabei alle zeichen klein
	#wenn dies bis zur mitte des strings abhandelbar ist, dann ist es ein Palindrom/True
	if p[0].lower() == p[-1].lower() :
		return is_palindrome(p[1:-1])
	#wenn keiner der beiden oberen Fälle True ist, dann ist es kein Palindrom/False
	else :
		return False

print(is_palindrome('Rentner'))
print(is_palindrome('Reliefpfeiler'))
print(is_palindrome('Palindrom'))
print(is_palindrome('racecar'))
print(is_palindrome('Python'))


	
		
		



