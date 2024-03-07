'''. En el capítulo 73 de la serie "The Big Bang Theory", el personaje principal Sheldon Cooper realiza una 
afirmación intrigante sobre los "números de Sheldon". Según Sheldon, el número 73 es el mejor número, ya que 
tiene propiedades interesantes. El número 73 es el 21-ésimo número primo, y al invertir sus cifras, 
obtenemos el número 37, que es el primo número 12. Si invertimos nuevamente el número 37, obtenemos 21, 
que es el producto de los dígitos 7 y 3. Se te pide diseñar un programa que, dado un número natural L como entrada,
encuentre todos los "números de Sheldon" que sean menores que L. Un número primo será considerado un número de Sheldon 
si cumple dos condiciones: el producto de sus dígitos debe ser igual a su posición en la secuencia de números primos, 
y al invertir sus cifras, obtendremos el número primo cuya posición es el reverso de su posición original.'''

class Numero_de_Sheldon():
    
    def __init__(self,l):
        self.l=l
    
    def determinar_sheldon(self):
        primos=[]
        for i in range(2,self.l+1):
            es_primo=True
            for j in range(2,i):
                if i%j==0:
                    es_primo=False
                    break
            if es_primo:
                primos.append(i)
                
        n=0  
        Numero_de_Sheldon=[]  
        while n<len(primos):
            for elemento in primos:
                total=1
                posicion_elemento=(primos.index(elemento)+1)
                if elemento<10:
                    total*=elemento
                    if total==posicion_elemento:
                        numero_original=elemento
                        numero_invertido=srt(numero_original[::-1])   
                        total=0
                        
                else:
                    for digito in str(elemento):
                        total*=int(digito)
                        if total==posicion_elemento:
                            Numero_de_Sheldon.append(elemento)
                            total=0
                    
#no se por que en el 17 y en el 73 da cero el total
  
                print(elemento, posicion_elemento, total)
                input()
                n+=1        

        print('\nLos números de Sheldon son:',Numero_de_Sheldon)
        
instancia=Numero_de_Sheldon(100)
instancia.determinar_sheldon()