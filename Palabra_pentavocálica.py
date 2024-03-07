class Pentavocalica:
    
    def __init__(self,palabra):
        self.palabra=palabra
        
    def verificar_letras(self):
        vocales=['a','e','i','o','u']
        contador=0
        for letra in self.palabra:
            if letra in vocales:
                contador+=1
        if contador==5:
            print(f'\nLa palabra {self.palabra} es pentavocálica.')
        else:
            print(f'\nLa palabra {self.palabra} no es pentavocálica.')
    
print('''\nEste programa determina si una palabra es pentavocálica; es decir, determina si
      la palabra contiene las cinco vocales, sin repetirse.''')

ciclo=True

while ciclo:
    
    inicio=input('\n¿Desea comenzar? (si/no): ')
    if inicio.lower()=='no':
        ciclo=False
        input('\nPresione enter para finalizar.')
        
    elif inicio.lower()=='si':
        
        try:
            palabra=str(input('\nIngrese la palabra para determinar si es pentavocálica: '))
            instancia_pentavocalica=Pentavocalica(palabra)
            instancia_pentavocalica.verificar_letras()
        
        except Exception as error:
            print('\nError en el tipo de dato:',error)

    else:
        print('\nRespuesta incorrecta, por favor intente nuevamente.')