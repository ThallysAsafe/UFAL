# Inversão de String Recursiva:
# Implemente uma função recursiva para inverter uma string.

def inverter(palavra, i):
    if i == 0:
        return palavra[i]
    else:
        return palavra[i] + inverter(palavra, i-1)
palavra= 'Thallys'    
i = len(palavra)-1
print(inverter(palavra,i))
def inverter(palavra):
    if not palavra:
        return ''
    else:
        return palavra[-1] + inverter(palavra[:-1])
palavra= 'Thallys'    
print(inverter(palavra))