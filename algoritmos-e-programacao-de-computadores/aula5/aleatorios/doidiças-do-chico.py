n = int(input())
fat = 1
def fatorial(n):
    fat = fat * n
    n -= 1
    return(fat)
print(fatorial(n))