'''Escribir un programa que a partir de un vector A de N elementos, se construya otro arreglo B donde cada 
elemento B[i] contenga la posicion que ocuparía el elemento A[i] si estuviese ordenado en forma creciente
[14,8,3,2,15,12,7]
[6,4,2,1,7,5,3]'''

class obtener_posiciones:
    
    def __init__(self,copia_lista,lista):
        self.copia_lista=copia_lista
        self.lista=lista
    
    def vector(self):
        posiciones=[]
        
        #Método de la burbuja
        #Se usa este método para ordenar el vector original y obtener las posiciones para luego comparar y 
        # obtener el vector deseado.
        for i in range(len(self.lista)):
            for j in range(i+1,len(self.lista)):
                if self.lista[i]>self.lista[j]:
                    aux=self.lista[i]
                    self.lista[i]=self.lista[j]
                    self.lista[j]=aux
                    
        for numero in self.copia_lista:
            posicion=self.lista.index(numero)+1
            if numero in self.copia_lista:
                posiciones.append(posicion)
                
        print('\nElementos:',self.copia_lista)
        print('Posiciones que ocuparían:',posiciones)

print('\nEste programa determina las posiciones de los elementos de un vector si estuviese ordenado de manera creciente.')

ciclo=True
while ciclo:
    res=str(input('\n¿Desea comenzar? (si/no): '))
    if res.lower()=='no':
        ciclo=False
        input('\nPresione enter para finalizar.')
        
    elif res.lower()=='si':
        
        try:
            lista=[]
            copia_lista=[]
            cont=0
            cantidad=int(input('\n¿Cuántos elementos contiene el vector?: '))
            while cont<cantidad:
                dato=int(input('\nIngrese el elemento: '))
                lista.append(dato)
                copia_lista.append(dato)
                cont+=1
            instancia_posiciones=obtener_posiciones(copia_lista,lista)
            instancia_posiciones.vector()
            
        except Exception as error:
            print('\nError en el tipo de dato:',error)
    
    elif res.lower()=='no':
        ciclo=False
        input('\nPresione enter para finalizar.')
    
    else:
        print('\nRespuesta no reconocida, intente nuevamente.')
