# 3. Implemente uma função recursiva que, dada uma lista de inteiros ordenada, busque por um busca

def busca_linear(x, list,i):
    if x != list[i] and len(list)-1 > i:
        return busca_linear(x,list,i+1)
    elif x == list[i]:
        return True
    else:
        return False
x = 3
list = [-5,-3,0,1,2,4,7,10]
i = 0
print(busca_linear(x, list,i))

def busca_binaria(x, list, i=0,final=None):
    if final is None:
        final = len(list)-1
    if i > final: return False
    mid = (final+i) // 2
    if x == list[mid]:
        return True
    elif x < list[mid]:
        return busca_binaria(x, list, i, mid-1)
    elif x > list[mid]:
        return busca_binaria(x, list, mid + 1, final)

print(busca_binaria(x, list, i=0,final=None))