
def main():
    #escribe tu código abajo de esta línea
    papel = int(input('dame el numero de pliegos que tienes: '))
plumon = int(input('dame el numero de plumones que tienes: '))

print('Numero de tarjetas maximas posibles')
pp = (papel*12)
np = (plumon*35)

if np <pp:
    print(np)
if pp < np:
    print(pp)
    
    pass

if __name__=='__main__':
    main()
