# latex-notation-stats

This Python script gets all LaTeX math expressions contained in a list of LaTeX documents (defined using `$...$` syntax at the moment) and computes, for each of them, the number of isolated occurences and the number of occurences as substring of longer math expressions.

The extracted information from the document are stored in a data structure that can be queried using SQL syntax and it is possible to easily run your own queries by editing the script.

The purposes of the script are:

- Check if the notation you adopted in your LaTeX documents (e.g., a scientific paper or a master thesis) is consistent;
- Check if a certain math expression, that occurres many times in the LaTeX documents, should be replaced with a macro;

Here is an example of output of the script:

|    | math_expression   |   isolated_occurences |   occurences_as_substring |
|---:|:------------------|----------------------:|--------------------------:|
|  0 | $\utxouts$        |                     1 |                         2 |
|  1 | $\compsec$        |                     1 |                         6 |
|  2 | $z$               |                     1 |                         8 |
|  3 | $F$               |                     1 |                        11 |
|  4 | $w$               |                     1 |                        26 |
|  5 | $h$               |                     1 |                        46 |
|  6 | $n$               |                     1 |                        51 |
|  7 | $s$               |                     1 |                        65 |
|  8 | $r$               |                     1 |                        75 |
|  9 | $t$               |                     1 |                       133 |
| 10 | $[0, 2^l - 1]$    |                     2 |                         0 |
| 11 | $d_i=0$           |                     2 |                         0 |
| 12 | $\calX$           |                     2 |                         1 |
| 13 | $\calY$           |                     2 |                         1 |
| 14 | $f(x)$            |                     2 |                         1 |
| 15 | $\mathcal{D}$     |                     2 |                         2 |
| 16 | $\utxoins$        |                     2 |                         3 |
| 17 | $0$               |                     2 |                         7 |
| 18 | $1$               |                     2 |                        49 |
| 19 | $g$               |                     2 |                        49 |
| 20 | $\mathcal{S}$     |                     3 |                         0 |
| 21 | $\mathcal{A}$     |                     3 |                         0 |
| 22 | $d_i=1$           |                     3 |                         0 |
| 23 | $\p_i$            |                     3 |                         0 |
| 24 | $y$               |                     3 |                         5 |
| 25 | $q$               |                     3 |                         9 |
| 26 | $p$               |                     3 |                        38 |
| 27 | $\mathcal{F}$     |                     4 |                         0 |
| 28 | $\mathbb{G}$      |                     4 |                         0 |
| 29 | $\pi$             |                     4 |                         1 |
| 30 | $x$               |                     4 |                        74 |
| 31 | $\Fsc$            |                     5 |                         0 |
