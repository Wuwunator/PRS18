# Wencke Hartwig
# 790786
# Uebungsblatt 2
# 08.05.2018

# 2 for-Schleifen
# 2.1 Fakultät

def fakultaet(n) :
	x = 1
	for i in range(1,n+1) :
		x = x * i
	return x

j = int(input('Fakultaet der Zahl _ ?'))
print (fakultaet(j))


# Was fällt auf?

# Je mehr Stellen die eingegebene Zahl hat, desto langsamer wird die Fakultät berechnet.
# Ist die Zahl länger als 5 Stellen, bleibt das Terminal bei der Ausführung hängen.

