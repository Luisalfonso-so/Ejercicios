class Metodo_Newton:
    def __init__(self,xant,a,tol,n):
        self.a=a
        self.tol=tol
        self.n=n 
        self.xant=xant
      
    def raiz_enesima(self): #metodo para calcular el valor de x siguiente
        x_ant=self.xant
        xsig=0
        while abs(xsig-x_ant)>self.tol:
            xsig=(((self.n-1)*x_ant)+(self.a/(x_ant**(self.n-1))))/self.n
            
            #en caso de que la diferencia entre xant y xsig sea mayor que la tolerancia, esto cambia el valor de xant
            #por el valor de xsig obtenido para poder obtener el valor de xsig.
            x_ant,xsig=xsig,x_ant 

        print(f'\nEl valor de la raíz es: {xsig}')
        
print('\nEste programa calcula la raíz enesima de un numero dados ciertos datos:')

ciclo=True
while ciclo:
    pregunta=input('\n¿Desea comenzar? (si/no): ')
    
    #finaliza el ciclo try except
    if pregunta.lower()=='no':
        ciclo=False
        input('\nPresione enter para finalizar.')
    elif pregunta.lower()=='si':
        
        try:
            #entrada de datos
            x_anter=float(input('\nIngrese el valor de x anterior (número anterior a que usted considera que es la raíz): '))
            a=int(input('Ingrese el valor de a (entero y positivo): '))
            tol=float(input('Ingrese el valor de la tolerancia (debe estar entre cero y uno): '))
            n=int(input('Ingrese el índice de la raíz: '))
            
            #validación de que algunos datos estén en el rango adecuado
            if a<0 or tol<=0 or tol>=1:
                print('\nUno de los datos ingresados no es correcto.')
                x_anter=float(input('\nIngrese el valor de x anterior (número anterior a que usted considera que es la raíz): '))
                a=int(input('Ingrese el valor de a: '))
                tol=float(input('Ingrese el valor de la tolerancia: '))
                n=int(input('Ingrese el índice de la raíz: '))
                instancia_metodo_Newton=Metodo_Newton(x_anter,a,tol,n)
                instancia_metodo_Newton.raiz_enesima()
                
            else:
                #se ejecuta si todos los datos fueron ingresados conrrectamente.
                instancia_metodo_Newton=Metodo_Newton(x_anter,a,tol,n)
                instancia_metodo_Newton.raiz_enesima()
                      
        except Exception as error:
            #me arroja un error en caso de que sea ingresado un dato con un tipo diferente al solicitado.
            print('\nError en tipo de dato:',error)
            
    elif pregunta.lower()=='no':
        #finaliza el ciclo try except
        ciclo=False
        input('Presione enter para finalizar.')
        
    else:
        #Imprime este mensaje si el usuario ingresa algo diferente a si o no al inicio, para poder continuar con la ejecución del programa
        print('\nRespuesta incorrecta, intente nuevamente.')