# Zusatzaufgabe 18 1)

# Burrows Wheeler Transformation

Um Daten komprimierungsfreundlicher zu gestalten möchten wir sie so transformieren, dass sie viele gleiche Buchstaben aufeinander folgen. Texte wie $ABCDABC$ beinhalten viele Wiederholungen von der Silbe $ABC$ aber keine Buchstabendopplungen welche die kompression deutlich erleichtern. Eine Lösung dazu bietet die **Burrows–Wheeler–Transformation**.

## Transformation

```flowchart
st=>start: Start|past
e=>end: End|future
op1=>operation: Trage die zyklischen
Verschiebungen von
S in eine Tabelle ein|past
op2=>operation: Sortiere die Tabelle 
alphabetisch|current
sub1=>subroutine: My Subroutine|invalid
cond=>condition: Yes
or No?|approved:>http://www.google.com
c2=>condition: Good idea|rejected
io=>inputoutput: Gebe folgende Werte zurück:
Index der Zeile mit S
letzte Spalte der Tabelle|future
st->op1(right)->op2(right)->io->e
```

#### Zyklische Tabelle

Tragen Sie alle zyklischen Verschiebungen des Strings in eine Tabelle ein.

| $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ |
| --- | --- | --- | --- | --- | --- | --- |
| $A$ | $B$ | $C$ | $D$ | $A$ | $B$ | $C$ |
| $B$ | $C$ | $D$ | $A$ | $B$ | $C$ | $A$ |
| $C$ | $D$ | $A$ | $B$ | $C$ | $A$ | $B$ |
| $D$ | $A$ | $B$ | $C$ | $A$ | $B$ | $C$ |
| $A$ | $B$ | $C$ | $A$ | $B$ | $C$ | $D$ |
| $B$ | $C$ | $A$ | $B$ | $C$ | $D$ | $A$ |
| $C$ | $A$ | $B$ | $C$ | $D$ | $A$ | $B$ |

#### Sortieren

Sortieren Sie die Tabelle alphabetisch.

| $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ |
| --- | --- | --- | --- | --- | --- | --- |
| $A$ | $B$ | $C$ | $A$ | $B$ | $C$ | $D$ |
| $A$ | $B$ | $C$ | $D$ | $A$ | $B$ | $C$ |
| $B$ | $C$ | $A$ | $B$ | $C$ | $D$ | $A$ |
| $B$ | $C$ | $D$ | $A$ | $B$ | $C$ | $A$ |
| $C$ | $A$ | $B$ | $C$ | $D$ | $A$ | $B$ |
| $C$ | $D$ | $A$ | $B$ | $C$ | $A$ | $B$ |
| $D$ | $A$ | $B$ | $C$ | $A$ | $B$ | $C$ |

#### Rückgabe

Geben Sie den Index der Zeile in welcher der ursprüngliche Text steht  und die letzte Spalte der Tabelle zurück. $s=DCAABBC$ und $i=1$

### Psydocode

```py
def BWT(s):
	l_shift = lambda s, i: s[i:]+s[:i]
	table = sorted([l_shift(s, i) for i in range(len(s))])
	return ''.join(row[-1] for row in table), table.index(s)

BWT('ABCDABC') -> ('DCAABBC', 1)
```

## Inverse

Um die Transformation umzukehren wollen wir den String $DCAABBC$ in die letzte Spalte der Tabelle eintragen. Danach sortieren wir die Tabelle und tragen den String $DCAABBC$ in die vorletzte Spalte. Diesen Vorgang wiederholen wir bis die Tabelle gefüllt ist. Danach geben wir die Zeile der Tabelle mit dem Index $i$ zurück.

```flowchart
st=>start: Start|past
e=>end: End|future
op1=>operation: Trage S in die
letzte offene Spalte
der Tabelle ein|past
op2=>operation: Sortiere die Tabelle 
alphabetisch|current
sub1=>subroutine: My Subroutine|invalid
cond=>condition: Tabelle voll?|approved
c2=>condition: Good idea|rejected
io=>inputoutput: Gebe folgende Werte zurück:
Zeile des Index I|future

st->op1->op2(right)->cond
cond(no)->op1
cond(yes)->io->e
```

#### Eintragen des Strings

| $1$  | $2$  | $3$  | $4$  | $5$  | $6$  | $7$ |
| ---- | ---- | ---- | ---- | ---- | ---- | --- |
| $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $D$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $C$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $A$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $A$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $B$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $B$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $C$ |

#### Sortieren

| $1$  | $2$  | $3$  | $4$  | $5$  | $6$  | $7$ |
| ---- | ---- | ---- | ---- | ---- | ---- | --- |
| $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $A$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $A$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $B$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $B$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $C$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $C$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $D$ |

#### Wiederholen

| $1$  | $2$  | $3$  | $4$  | $5$  | $6$ | $7$ |
| ---- | ---- | ---- | ---- | ---- | --- | --- |
| $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $D$ | $A$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $C$ | $A$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $A$ | $B$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $A$ | $B$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $B$ | $C$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $B$ | $C$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $C$ | $D$ |

## 

| $1$  | $2$  | $3$  | $4$  | $5$  | $6$ | $7$ |
| ---- | ---- | ---- | ---- | ---- | --- | --- |
| $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $A$ | $B$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $A$ | $B$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $B$ | $C$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $B$ | $C$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $C$ | $A$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $C$ | $D$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $\_$ | $D$ | $A$ |

| $1$  | $2$  | $3$  | $4$  | $5$ | $6$ | $7$ |
| ---- | ---- | ---- | ---- | --- | --- | --- |
| $\_$ | $\_$ | $\_$ | $\_$ | $D$ | $A$ | $B$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $C$ | $A$ | $B$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $A$ | $B$ | $C$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $A$ | $B$ | $C$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $B$ | $C$ | $A$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $B$ | $C$ | $D$ |
| $\_$ | $\_$ | $\_$ | $\_$ | $C$ | $D$ | $A$ |

$\dots$

| $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ |
| --- | --- | --- | --- | --- | --- | --- |
| $A$ | $B$ | $C$ | $A$ | $B$ | $C$ | $D$ |
| $A$ | $B$ | $C$ | $D$ | $A$ | $B$ | $C$ |
| $B$ | $C$ | $A$ | $B$ | $C$ | $D$ | $A$ |
| $B$ | $C$ | $D$ | $A$ | $B$ | $C$ | $A$ |
| $C$ | $A$ | $B$ | $C$ | $D$ | $A$ | $B$ |
| $C$ | $D$ | $A$ | $B$ | $C$ | $A$ | $B$ |
| $D$ | $A$ | $B$ | $C$ | $A$ | $B$ | $C$ |

#### Ausgabe

Gebe die Zeile $i$ zurück.

## Psydocode

```py
def BWT_i(s, i):
	table = sorted(s)
	for _ in range(len(s)-1):
		table = [char + row for char, row in zip(s, table)]
		table = sorted(table)
	return table[i]


BWT_i('DCAABBC', 7) -> 'ABCDABC'
```

### Warum funktioniert das?

Um die Rücktransformation durchzuführen brauchen wir die bei der Hintransformation erstellte Tabelle. Über diese wissen wir, dass die letzte Spalte unser String $S$ ist. Ebenfalls wissen wir, dass die erste Spalte der sortierte String $\hat{S}$ ist. Da wir zuletzt noch wissen, dass in jeder Zeile der gleiche Text bloß rotiert steht, wissen wir auch, dass der letzte Buchstabe nach einer Zeile immer direkt vor dem ersten dieser Zeile steht. Von hier aus können wir nun rekursiv für jeden Buchstaben der letzten Spalte seinen Vorgänger finden, indem wir die Tabelle erneut sortieren und die Vorgänger aus $S$ in die vorletzte Spalte eintragen.

# Zusatzaufgabe 18 2)

Die Rücktransformation ergibt folgende Tabelle

| $1$ | $2$ | $3$ | $4$ | $5$ | $6$ | $7$ | $8$ | $9$ | $10$ | $11$ | $12$ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | ---- | ---- |
| $B$ | $E$ | $I$ | $N$ | $R$ | $E$ | $I$ | $N$ | $K$ | $E$  | $I$  | $N$  |
| $E$ | $I$ | $N$ | $B$ | $E$ | $I$ | $N$ | $R$ | $E$ | $I$  | $N$  | $K$  |
| $E$ | $I$ | $N$ | $K$ | $E$ | $I$ | $N$ | $B$ | $E$ | $I$  | $N$  | $R$  |
| $E$ | $I$ | $N$ | $R$ | $E$ | $I$ | $N$ | $K$ | $E$ | $I$  | $N$  | $B$  |
| $I$ | $N$ | $B$ | $E$ | $I$ | $N$ | $R$ | $E$ | $I$ | $N$  | $K$  | $E$  |
| $I$ | $N$ | $K$ | $E$ | $I$ | $N$ | $B$ | $E$ | $I$ | $N$  | $R$  | $E$  |
| $I$ | $N$ | $R$ | $E$ | $I$ | $N$ | $K$ | $E$ | $I$ | $N$  | $B$  | $E$  |
| $K$ | $E$ | $I$ | $N$ | $B$ | $E$ | $I$ | $N$ | $R$ | $E$  | $I$  | $N$  |
| $N$ | $B$ | $E$ | $I$ | $N$ | $R$ | $E$ | $I$ | $N$ | $K$  | $E$  | $I$  |
| $N$ | $K$ | $E$ | $I$ | $N$ | $B$ | $E$ | $I$ | $N$ | $R$  | $E$  | $I$  |
| $N$ | $R$ | $E$ | $I$ | $N$ | $K$ | $E$ | $I$ | $N$ | $B$  | $E$  | $I$  |
| $R$ | $E$ | $I$ | $N$ | $K$ | $E$ | $I$ | $N$ | $B$ | $E$  | $I$  | $N$  |

Aus dem Index $i=7$ lässt sich die Zeile $KEINBEINREIN$ als Rückgabewert ablesen.

# Zusatzaufgabe 19

# Move to Front

Um einen vergleichbaren Effekt wie in der WBT zu erzielen kann der sog. Move to Front Algorithmus angewandt werden. Wir transformieren dabei ein Wort in eine Sequenz in dem wir für jeden Buchstaben die folgenden zwei Schritte ausführen.

Wir starten mit einem sortierten Alphabet und einer leeren Sequenz. Für jedes Buchstaben des Strings:

1. Hänge den Index, bei welchem sich der Buchstabe im Alphabet befindet an die Sequenz an.

2. Verschiebe den Buchstaben aus dem Alphabet, an den Anfang des Alphabets.
   

Für die Rücktransformation für man einfach die folgenden Schritte für alle Elemente der Sequenz aus; wieder beginnend mit einem sortierten Alphabet.

1. Hänge den Alphabetsbuchstaben des Index (Element aus der Sequenz) an das Wort an.

2. Verschiebe den Buchstaben an den Anfang des Alphabets.

### Hintransformation

| String         | Sequenz                                                              | Alphabet                                                                                                   |
| -------------- | -------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| $Nkrbeeeniiin$ | $\left \langle 13\right \rangle$                                     | $\left \langle n, a, b, c, d, e, f, g, h, i, j, k, l, m, o, p, q, r, s, t, u, v, w, x, y, z\right \rangle$ |
| $nKrbeeeniiin$ | $\left \langle 13, 11\right \rangle$                                 | $\left \langle k, n, a, b, c, d, e, f, g, h, i, j, l, m, o, p, q, r, s, t, u, v, w, x, y, z\right \rangle$ |
| $nkRbeeeniiin$ | $\left \langle 13, 11, 17\right \rangle$                             | $\left \langle r, k, n, a, b, c, d, e, f, g, h, i, j, l, m, o, p, q, s, t, u, v, w, x, y, z\right \rangle$ |
| $nkrBeeeniiin$ | $\left \langle 13, 11, 17, 4\right \rangle$                          | $\left \langle b, r, k, n, a, c, d, e, f, g, h, i, j, l, m, o, p, q, s, t, u, v, w, x, y, z\right \rangle$ |
| $nkrbEeeniiin$ | $\left \langle 13, 11, 17, 4, 7\right \rangle$                       | $\left \langle e, b, r, k, n, a, c, d, f, g, h, i, j, l, m, o, p, q, s, t, u, v, w, x, y, z\right \rangle$ |
| $nkrbeEeniiin$ | $\left \langle 13, 11, 17, 4, 7, 0\right \rangle$                    | $\left \langle e, b, r, k, n, a, c, d, f, g, h, i, j, l, m, o, p, q, s, t, u, v, w, x, y, z\right \rangle$ |
| $nkrbeeEniiin$ | $\left \langle 13, 11, 17, 4, 7, 0, 0\right \rangle$                 | $\left \langle e, b, r, k, n, a, c, d, f, g, h, i, j, l, m, o, p, q, s, t, u, v, w, x, y, z\right \rangle$ |
| $nkrbeeeNiiin$ | $\left \langle 13, 11, 17, 4, 7, 0, 0, 4\right \rangle$              | $\left \langle n, e, b, r, k, a, c, d, f, g, h, i, j, l, m, o, p, q, s, t, u, v, w, x, y, z\right \rangle$ |
| $nkrbeeenIiin$ | $\left \langle 13, 11, 17, 4, 7, 0, 0, 4, 11\right \rangle$          | $\left \langle i, n, e, b, r, k, a, c, d, f, g, h, j, l, m, o, p, q, s, t, u, v, w, x, y, z\right \rangle$ |
| $nkrbeeeniIin$ | $\left \langle 13, 11, 17, 4, 7, 0, 0, 4, 11, 0\right \rangle$       | $\left \langle i, n, e, b, r, k, a, c, d, f, g, h, j, l, m, o, p, q, s, t, u, v, w, x, y, z\right \rangle$ |
| $nkrbeeeniiIn$ | $\left \langle 13, 11, 17, 4, 7, 0, 0, 4, 11, 0, 0\right \rangle$    | $\left \langle i, n, e, b, r, k, a, c, d, f, g, h, j, l, m, o, p, q, s, t, u, v, w, x, y, z\right \rangle$ |
| $nkrbeeeniiiN$ | $\left \langle 13, 11, 17, 4, 7, 0, 0, 4, 11, 0, 0, 1\right \rangle$ | $\left \langle n, i, e, b, r, k, a, c, d, f, g, h, j, l, m, o, p, q, s, t, u, v, w, x, y, z\right \rangle$ |

```py
def mtf(s):
	alphabet = list('abcdefghijklmnopqrstuvwxyz')
	result = []
	for c in s.lower():
		idx = alphabet.index(c)
		result.append(idx)
		alphabet = [alphabet[idx]] + alphabet[:idx] + alphabet[idx+1:]
	return result


mtf('nkrbeeeniiin') -> [13, 11, 17, 4, 7, 0, 0, 4, 11, 0, 0, 1]
```

### Rücktransformation

| Sequenz                                                                        | String                                                            | Alphabet                                                                                                     |
| ------------------------------------------------------------------------------ | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| $\left \langle \textbf{13}, 11, 17, 4, 7, 0, 0, 4, 11, 0, 0, 1 \right \rangle$ | $\left \langle n \right \rangle$                                  | $ \left \langle n, a, b, c, d, e, f, g, h, i, j, k, l, m, o, p, q, r, s, t, u, v, w, x, y, z \right \rangle$ |
| $\left \langle 13, \textbf{11}, 17, 4, 7, 0, 0, 4, 11, 0, 0, 1 \right \rangle$ | $\left \langle n, k \right \rangle$                               | $ \left \langle k, n, a, b, c, d, e, f, g, h, i, j, l, m, o, p, q, r, s, t, u, v, w, x, y, z \right \rangle$ |
| $\left \langle 13, 11, \textbf{17}, 4, 7, 0, 0, 4, 11, 0, 0, 1 \right \rangle$ | $\left \langle n, k, r \right \rangle$                            | $ \left \langle r, k, n, a, b, c, d, e, f, g, h, i, j, l, m, o, p, q, s, t, u, v, w, x, y, z \right \rangle$ |
| $\left \langle 13, 11, 17, \textbf{4}, 7, 0, 0, 4, 11, 0, 0, 1 \right \rangle$ | $\left \langle n, k, r, b \right \rangle$                         | $ \left \langle b, r, k, n, a, c, d, e, f, g, h, i, j, l, m, o, p, q, s, t, u, v, w, x, y, z \right \rangle$ |
| $\left \langle 13, 11, 17, 4, \textbf{7}, 0, 0, 4, 11, 0, 0, 1 \right \rangle$ | $\left \langle n, k, r, b, e \right \rangle$                      | $ \left \langle e, b, r, k, n, a, c, d, f, g, h, i, j, l, m, o, p, q, s, t, u, v, w, x, y, z \right \rangle$ |
| $\left \langle 13, 11, 17, 4, 7, \textbf{0}, 0, 4, 11, 0, 0, 1 \right \rangle$ | $\left \langle n, k, r, b, e, e \right \rangle$                   | $ \left \langle e, b, r, k, n, a, c, d, f, g, h, i, j, l, m, o, p, q, s, t, u, v, w, x, y, z \right \rangle$ |
| $\left \langle 13, 11, 17, 4, 7, 0, \textbf{0}, 4, 11, 0, 0, 1 \right \rangle$ | $\left \langle n, k, r, b, e, e, e \right \rangle$                | $ \left \langle e, b, r, k, n, a, c, d, f, g, h, i, j, l, m, o, p, q, s, t, u, v, w, x, y, z \right \rangle$ |
| $\left \langle 13, 11, 17, 4, 7, 0, 0, \textbf{4}, 11, 0, 0, 1 \right \rangle$ | $\left \langle n, k, r, b, e, e, e, n \right \rangle$             | $ \left \langle n, e, b, r, k, a, c, d, f, g, h, i, j, l, m, o, p, q, s, t, u, v, w, x, y, z \right \rangle$ |
| $\left \langle 13, 11, 17, 4, 7, 0, 0, 4, \textbf{11}, 0, 0, 1 \right \rangle$ | $\left \langle n, k, r, b, e, e, e, n, i \right \rangle$          | $ \left \langle i, n, e, b, r, k, a, c, d, f, g, h, j, l, m, o, p, q, s, t, u, v, w, x, y, z \right \rangle$ |
| $\left \langle 13, 11, 17, 4, 7, 0, 0, 4, 11, \textbf{0}, 0, 1 \right \rangle$ | $\left \langle n, k, r, b, e, e, e, n, i, i \right \rangle$       | $ \left \langle i, n, e, b, r, k, a, c, d, f, g, h, j, l, m, o, p, q, s, t, u, v, w, x, y, z \right \rangle$ |
| $\left \langle 13, 11, 17, 4, 7, 0, 0, 4, 11, 0, \textbf{0}, 1 \right \rangle$ | $\left \langle n, k, r, b, e, e, e, n, i, i, i \right \rangle$    | $ \left \langle i, n, e, b, r, k, a, c, d, f, g, h, j, l, m, o, p, q, s, t, u, v, w, x, y, z \right \rangle$ |
| $\left \langle 13, 11, 17, 4, 7, 0, 0, 4, 11, 0, 0, \textbf{1}\right \rangle$  | $\left \langle n, k, r, b, e, e, e, n, i, i, i, n \right \rangle$ | $ \left \langle n, i, e, b, r, k, a, c, d, f, g, h, j, l, m, o, p, q, s, t, u, v, w, x, y, z \right \rangle$ |

```py
def mtf_i(s):
	alphabet = list('abcdefghijklmnopqrstuvwxyz')
	result = []
	for idx in s:
		result.append(alphabet[idx])
		alphabet = [alphabet[idx]] + alphabet[:idx] + alphabet[idx+1:]
	return ''.join(result)

mtf_i([13, 11, 17, 4, 7, 0, 0, 4, 11, 0, 0, 1]) -> 'nkrbeeeniiin'
```
