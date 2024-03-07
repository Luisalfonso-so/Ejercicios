'''Dado un par de palabras ingresadas como datos, determina si son anagramas entre sí. 
Por ejemplo, consideremos las palabras "fresa" y "frase".'''

class Anagrama:
    
    def __init__(self,palabra1,palabra2):
        self.palabra1=palabra1
        self.palabra2=palabra2
        
    def comparar(self):
        copia1=self.palabra1
        copia2=self.palabra2
        lista1=[]
        lista2=[]
        
        for i in self.palabra1:
            lista1.append(i)
            lista1.sort()
        for j in self.palabra2:
            lista2.append(j)
            lista2.sort()
            
        if lista1==lista2:
            print(f'\nLas palabras {copia1,copia2} son anagramas entre sí')
                            
        else:
            print(f'\nLas palabras {copia1,copia2} no cumplen las condiciones, por lo tanto no son anagramas entre sí.')
    
print('\nEste programa permite verificar si dos palabras son anagramas entre si.')
print('Para que dos palabras sean anagramas entre si deben tener las mismas letras y la misma cantidad de letras.')

ciclo=True
while ciclo:
    
    comenzar=input('\n¿Desea comenzar? (si/no): ')
    
    if comenzar.lower()=='no':
        ciclo=False
        input('\nPresione enter para finalizar.')
        
    elif comenzar.lower()=='si':
        try:
            palabra1=input('\nIngrese la primera palabra: ')
            palabra2=input('Ingrese la segunda palabra: ')
            instancia_anagrama=Anagrama(palabra1,palabra2)
            instancia_anagrama.comparar()
            
        except Exception as error:
            print('\nError en el tipo de dato:',error)
            
    elif comenzar.lower()=='no':
        ciclo=False
        input('\nPresione enter para finalizar.')

    else:
        print('\nRespuesta incorrecta, intente nuevamente.')