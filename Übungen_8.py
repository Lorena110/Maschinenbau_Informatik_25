
nenndurchmesser_schrauben = [3, 4, 5, 6, 8, 10]
spannungsquerschnitt = 0.8 * (3.14 * nenndurchmesser_schrauben **2)/4
Zugfstigkeit = [4.6, 8.8, 10.9]
Vorspannkraft = 0.7 * spannungsquerschnitt * Zugfstigkeit [0]
anziehdrehmoment = 0.2 * nenndurchmesser_schrauben* Vorspannkraft

