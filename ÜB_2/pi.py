# Wencke Hartwig
# 790786
# Uebungsblatt 2
# 08.05.2018

# 2 for-Schleifen
# 2.2 Berechnung von Pi

def pi(m):
    s = 0.0
    z = 2 * 1.4142135623730951454746218587388284504413604736328125 / 9801
    for n in range(m):
        former = (fakultaet(4 * n)) / (fakultaet(n) ** 4)
        latter = (1103 + 26390 * n) / (396 ** (4 * n))

        s = s + (former * latter)
    return 1 / (z * s)


def fakultaet(n):
    x = 1
    for i in range(1, n + 1):
        x = x * i
    return x


j = int(input('Durchgänge von Pi'))
print(pi(j))

# pirechnung = ((2*1.4142135623730951454746218587388284504413604736328125) / 9801)) *
