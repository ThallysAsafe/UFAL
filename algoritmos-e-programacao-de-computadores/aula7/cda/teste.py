conjunto = set([1,3,5,4,3,8,9,12,3])
conjunto2 = set([-1,-5,-3,-2,1,3,5])

#uniao, junção de todos os numeros
print(conjunto | conjunto2)
#interseccao, valores que estão presente em ambos conjuntos
print(conjunto & conjunto2)
#diferenca, o que tem em conjunto A que não tem em B
print(conjunto - conjunto2)
#elementos em a ou b, menos intersecção (ou exclusivo)
print(conjunto ^ conjunto2)
