# PythonDziki
Wprowadzenie
Niniejsza dokumentacja opisuje sposób działania projektu PythonDziki.

O Projekcie
Program(dataCollecting.py) otrzymuje dane w postaci linków do stoków narciarskich z różnych państw.
Na ich podstawie przeszukuje kolejne podstrony każdego ośrodka narciarskiego dla każdego państwa.
Program dla każdego stoku wyszukuje następujące dane:
•	Całkowita długość stoku
•	Różnica wysokości między stacją a szczytem stoku
•	Ilość wyciągów
•	Poszczególne ilość każdego typu wyciągów
Dane trafiają do DataFrameu i są zapisywane w pliku „exportDataframe.csv”
Program(machineLearning.py) wczytuje dataframe z pliku „exportDataframe.csv”.
Następnie do programu dostarczane są dane z parametrami oraz klasyfikacja etykiet
(machine learning – nauka programu czy dany stok ma bardzo dobre parametry czy słabe).
Użytkownik uruchamiając program ma możliwość podania parametrów stoku oraz sprawdzenie czy parametry klasyfikują stok jako świetny czy też słaby.
