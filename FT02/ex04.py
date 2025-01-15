"""Cria agora um nove ficheiro python (extensão .py) com o nome ex04.  
Escreve  um  programa  que  solicite  duas  notas  ([nota1]  e  [nota2])  ao  utilizador  e 
apresente a média das mesmas da seguinte forma:  
 
“A média das notas [nota1] e [nota2] é [média].” """



nota1=float(input('Nota 1: \n'))
nota2=float(input('Nota 2: \n'))
media=round((nota1+nota2)/2,2)#função round - permite arredondamento de número a x casas decimais
print(f'A média das notas {nota1} e {nota2} é {media}')

#sintaxe round --- round(numero_a_arredondar, numer_casas_decimais)