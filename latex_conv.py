# -*- coding: utf-8 -*-
# Wencke Hartwig
# 790786
# Uebungsblatt 10

# Baumrekursion und Schreiben von Textformaten

# Die zu übernehmende Baumstruktur:
t = ('S', [
    ('NP', [
        ('ART', 'die'), ('N', 'Katze')]),
    ('VP', [

        ('V', 'jagt'),
        ('NP', [
            ('ART', 'die'), ('N', 'Maus')])
    ])
])

# Eine Funktion, die die Knoten durchgeht und nachsieht
def tree_to_tex(node):
    # ob der Knoten ein string ist
    if type(node) == str:
        # wenn dem so ist, gib den Knoten und ein Leerzeichen zurück
        return node + ' '
    result = ''
    # für die Kinder der Knoten
    for child in node:
        # gib das Ergebnis der Knoten und deren Kinder zurück
        result += tree_to_tex(child)
    # wenn der Knoten eine Liste ist
    if type(node) == list:
        # gib das Ergebnis zurück
        return result
    # am Ende gib das Ergebnis der Schleife plus benötigte Zeichen für die Latex
    # Eingabe aus
    return '[.' + result + '] '

# der aus der Funktion folgende Teil, der in Latex eingefügt werden soll
tex = tree_to_tex(t)
# alles, was zuvor stehen muss
pre = '''\\documentclass[]{article}
\\usepackage{qtree}
\\usepackage[utf8]{inputenc}
\\begin{document}
	\\begin{center}
		\\Tree '''
# alles, was folgen muss
post = '''
	\\end{center}
\\end{document}'''

# erstelle daraus eine Datei für Latex mit dem Namen tree
with open('tree.tex', 'w', encoding='utf-8') as f:
    # in der folgendes steht
    f.write(pre + tex + post)