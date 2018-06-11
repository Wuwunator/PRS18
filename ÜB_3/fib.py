# Wencke Hartwig
# 790786
# Uebungsblatt 3

# 2 Numerische Funktion
# 2.2 Fibonacci Zahlen

def fib(n) :
	
	f1, f2 = 1, 1
	
	for i in range(n-1) :
		fn = f2
		f2 = f1 + f2
		f1 = fn
		
	return f1
	
print('n\tfib(n)')
for i in range(1,21) :
	print(str(i) + '\t' + str(fib(i)))
	


		
	
