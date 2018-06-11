# Wencke Hartwig
# 790786
# Uebungsblatt 4

# 1 Stringverarbeitung
# 1.1 Merkmalsfunktionen


#definieren der Funktion spelling
def spelling(w) :
	#leerer string als "Hülle" für neues, zu ersetzendes Wort
	new_word = ''
	#definieren der Funktion, die für die Länge des eingegebenen strings alle Zeichen ausgibt
	for i in range(0,len(w)) :
		letter = w[i]
		#jedes Zeichen des eingegebenen strings wird verglichen:
		#wenn das Zeichen ein Grossbuchstabe ist, dann ersetze ihn durch X, wenn nicht dann...	
		if letter.isupper() :
			new_word = new_word + 'X'
		#wenn das Zeichen ein Kleinbuchstabe ist, dann ersetze ihn durch x, wenn nicht dann...
		elif letter.islower() :
			new_word = new_word + 'x'
		#wenn das Zeichen eine Ziffer ist, dann ersetze ihn durch 9, wenn nicht dann...
		elif letter.isdigit() :
			new_word = new_word + '9'
		#wenn das Zeichen ein - ist, dann ersetze ihn durch --, wenn nicht dann...
		elif letter == '-' :
			new_word = new_word + '--'
		#ersetze alles Verbleibende durch .
		else :
			new_word = new_word + '.'
	#gibt den neu umgeschriebenen string aus
	return new_word
	
#gebe für folgende strings die oben definierte Ausgabe:
print(spelling('Python-2018'))

print(spelling('UniPotsdam'))

print(spelling('PRS-TUT um 15:00 Uhr.'))

print(spelling('CLSoSe2018'))

print(spelling('Leistungspunkte sammeln macht Spass.'))
	

		
		
