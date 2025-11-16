# Aufgabe 1
Die datei kann mithilfe des Befehls ```pandoc sheet04.md -o sheet04.pdf``` 
zu einer pdf umgewandelt werden.


# Quantenmechanik und Spin
1. In der Quantenstatistik unterscheidet man verschiedene Teilchensorten, die unterschiedlichen Gleichgewichtsverteilungen folgen. Der Zusammenhang zwischen Spin und Statistik wird in d   er relativistischen Quantenfeldtheorie durch das sogenannte Spin-Statistik-Theorem
hergestellt. [^1]


| Teilchensorte | Statistik | Spin |
|:------:|:------:|:------:|
| Fermion | Fermi-Dirac | halbzahlig |
| Boson | Bose-Einstein | ganzzahlig |

1. Für die Bose-Einstein-Verteilung ergibt sich die Besetzungszahl
   
$\bar{n_i} = \frac{g_i}{e^{(\epsilon_i-\mu)}/k_\text{B}T-1}$

für das Energieniveau i, wobei gi der Entartungsgrad, εi die Energie und μ das chemische
Potential ist. Analog erhält man für die Fermi-Dirac-Verteilung

$\bar{n_i} = \frac{g_i}{e^{(\epsilon_i-\mu)}/k_\text{B}T+1}$

3. Eine relativistische Theorie der Elektronen erhält man durch Quantisierung der Dirac-
Gleichung

$(i\hbar \gamma^u \delta_\mu - mc) \psi (x) = 0$

Die Dirac-Gleichung wurde 1928 von Paul Dirac eingeführt.

![Paul Dirac (1933), Quelle: ](/sheet04/Dirac.png)


In obiger Gleichung ist $\psi$(x) der Dirac-Spinor und die Dirac-Matrizen $\gamma^\mu$ sind gegeben durch

$\gamma^0 = \begin{bmatrix} I_2 & 0 \\ 0 & -I_2 \end{bmatrix}$,
$\gamma^i = \begin{bmatrix} 0 & a^{i} \\ -a^{i} & 0 \end{bmatrix}$,

mit den Pauli-Matrizen σi. Ausgeschrieben ergibt sich somit

$\gamma^0 = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & -1 & 0 \\ 0 & 0 & 0 & -1 \end{bmatrix}$, 
$\gamma^1 = \begin{bmatrix} 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & -1 & 0 & 0 \\ -1 & 0 & 0 & 0 \end{bmatrix}$,

$\gamma^2 = \begin{bmatrix} 0 & 0 & 0 & -i \\ 0 & 0 & i & 0 \\ 0 & i & 0 & 0 \\ -i & 0 & 0 & 0 \end{bmatrix}$,
$\gamma^3 = \begin{bmatrix} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & -1 \\ -1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \end{bmatrix}$, 

\newpage

# Aufgabe 2
Mithilfe diesem Skript werden die Blkätter in eine Pdf gemacht.

```
#!/bin/bash
# Dieses Skript erstellt pdf Dateien aus Markdown Dateien

i=0
while [ $i -lt 5 ]; do
    INDEX=$(printf "%02d" $i)
    if [ -f sheet"$INDEX".md ]; then
        echo "Konvertiere sheet$INDEX.md zu PDF..."
        pandoc sheet"$INDEX".md -o sheet"$INDEX".pdf
    else
        echo "Datei sheet$INDEX.md nicht gefunden. Beende Konvertierung."
        break
    fi
    i=$((i + 1))
done

echo "Skript beendet."
```

---
[^1]: [https://de.wikipedia.org/wiki/Spin-Statistik-Theorem](https://de.wikipedia.org/wiki/Spin-Statistik-Theorem)