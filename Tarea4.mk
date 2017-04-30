Resultados_hw4.pdf: Resultados_hw4.tex
	pdflatex Resultados_hw4.tex
Resultados_hw4.tex: Plots_temperatura.py Periodica.txt Fija.txt Abierta.txt
		python Plots_temperatura.py
	Periodica.txt Fija.txt Abierta.txt: a.out
		./a.out
	a.out: DifusionTemperatura.c
		gcc DifusionTemperatura.c
