# Wencke Hartwig
# 790786
# Uebungsblatt 3

# 2 Numerische Funktion
# 2.1 Logarithmus

def taylor(x, n) :
	value = 0.0
	for i in range(1, n+1) :
		taylor_teil = ((-1) ** (i + 1) / i) * ((x-1) ** i)
		value = value + taylor_teil
	return value 
		
	
for i in range(1, 51) :
	
	print(str(i) + "\t" + str(taylor(1.5, i)))
	
# So hab ich mit verschiedenen Einträgen der Tabelle einzelne Werte gegengeprüft.
