# -*- coding: utf-8 -*-
# Wencke Hartwig
# 790786
# Uebungsblatt 8

# 1 Grammatikrepräsentation

# eine Regelmenge von 20 Beispielen
R = {
    'S --> NP VP',
    'NP --> NP VP VP',
    'NP --> ART ADJ NN',
    'VP --> ART VFIN',
    'VP --> VFIN',
    'VP --> ART ADJ VFIN',
    'ART --> der',
    'ART --> die',
    'ART --> das',
    'NN --> Hund',
    'NN --> Katze',
    'NN --> Haus',
    'VFIN --> schläft',
    'VFIN --> nervt',
    'VFIN --> spielt',
    'ADJ --> schön',
    'ADJ --> groß',
    'ADJ --> alt',
    # Beispiele, die eine Fehlermeldung erzeugen sollen
    ' --> Hund',
    ' --> '}

# die Funktion parse_rules nimmt sich die Beispiele der Regelmenge R und unterteilt diese
# in eine Menge von Regeln (in keys und values)
def parse_rules(R):
    # als Ausgangspunkt ist eine leere Menge gegeben
    rules = {}
    # im weiteren wird nun zwischen dem/n key/s und dem/n value/s unterteilt
    for s in R:
        key, values = s.split(' --> ')
        # um alle Elemente einzeln behandeln zu können, werden sie durch set in eine Menge gelegt
        values_as_set = set(values.split())
        # beim durchgehen der Schleifen werden neue Elemente dem set hinzugefügt,
        # falls sie noch nicht vorhanden sind
        if key in rules:
            rules[key].update(values_as_set)
        # falls sie schon vorhanden sind, werden sie nicht nochmals hinzugefügt,
        # sondern es wird weiter gegangen
        else:
            rules[key] = values_as_set
    # zum Ende der Funktion werden die so aufgeteilten Regeln (in key und values) zurückgegeben
    return rules

# die Funktion find_non_terminators nimmt sich die Beispiele der Regelmenge R und
# unterscheidet zwischen Terminalen und Nicht-Terminalen
def find_non_terminals(R):
    # hierzu legt man fest, dass die keys eine Liste der keys aus R sind
    keys = list(R.keys())
    # dass alle keys Nicht-Terminale sind
    non_terminals = set(keys)
    # dass Terminale ein weiteres set sind
    terminals = set()
    # wobei gilt, dass alle Nicht-Terminale immer keys sind, dass jedoch
    # bei den Terminalen nochmals überprüft werden muss, ob sie wiederholt Nicht-Terminale sind,
    for key, values in R.items():
        for value in values:
            if value in keys:
                non_terminals.add(value)
                # wenn die values nur Terminale und keine Nicht-Terminale sind, werden sie zu den values der
                # Terminale hinzugefügt
            else:
                terminals.add(value)
    # zum Ende der Funktion werden dann Nicht-Terminale und Terminale zurückgegeben
    return (non_terminals, terminals)

# die Funktion sentence_sym nimmt sich die Beispiele der Regelmenge R und gibt das Satzsymbol
# des 4-Tupel aus. Das Satzsymbol ist ein Nicht-Terminal, was nur einmal auftritt
def sentence_sym(R):
    # als Ausgangspunkt ist eine leere Liste gegeben
    check_values = []
    # für die values in den values von R wird geschaut, ob sie vorhanden sind
    for values in R.values():
        for value in values:
            # wenn ja, wird die Liste erweitert
            check_values.append(value)
    # für die keys in den keys von R wird geschaut, ob sie schon in den keys vorkamen
    for key in R.keys():
        # wenn nicht, kamen sie nur ein einziges mal vor, sind demnach Satzsymbole
        if not key in check_values:
            # und werden als key zurückgegeben
            return key

# die Funktion parse_grammar nimmt sich die Beispiele der Regelmemge R und definiert die einzelnen
# Bestandteile des 4-Tupel
def parse_grammar(R):
    P = parse_rules(R)
    N, T = find_non_terminals(P)
    S = sentence_sym(P)
    # zum Ende der Funktion wird das 4-Tupel zurückgegeben
    return N, T, S, P


from pprint import pprint as print

print(parse_grammar(R))