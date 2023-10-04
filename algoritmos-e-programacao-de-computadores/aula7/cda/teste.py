conjunto = set([1, 7, 3, 9, 0, 8, 5, 6, 2, 4])
conjunto2 = set([9, 0, 7, 5, 8, 4, 6, 2, 3, 1])

#uniao, junção de todos os numeros
print(conjunto | conjunto2)
#interseccao, valores que estão presente em ambos conjuntos
print(conjunto & conjunto2)
#diferenca, o que tem em conjunto A que não tem em B
print(conjunto - conjunto2)
#elementos em a ou b, menos intersecção (ou exclusivo)
print(conjunto ^ conjunto2)
