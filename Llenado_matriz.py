class llenado:
    
    def __init__(self,n,m):
        self.n=n
        self.m=m
        
    def llenar(self):
        
        #para generar la matriz llena de ceros
        M=[[0 for _ in range(self.m)] for _ in range(self.n)]
        
        cont=1
        for i in range(self.n):
            if i%2==0:
                for j in range(self.m):
                    M[i][j]=cont
                    cont+=1         
            else:
                for j in range(self.m-1,-1,-1):
                    M[i][j]=cont
                    cont+=1
        
        #zig zag horizontal 
        print('\nLa matriz se llena de la siguiente manera:')
        print('  ')
        for f in range (self.n):
            for j in range (self.m):
                print(M[f][j],end="\t")
            print("")

print('\nEste programa está diseñado para llenar una matriz de N filas por M columnas en zig zag.')

ciclo=True
while ciclo:
    
    preg=str(input('\n¿Desea continuar? (si/no): '))
    if preg.lower()=='no':
        ciclo=False
        input('\nPresione enter para salir.')
        
    elif preg.lower()=='si':
        
        try:
            n=int(input('\nIngrese el número de filas: '))
            m=int(input('Ingrese el número de columnas: '))
            instancia_llenado=llenado(n,m)
            instancia_llenado.llenar()
            
        except Exception as error:
            print('\nError en los datos ingresados:',error)
            
    elif preg.lower()=='no':
        ciclo=False
        input('\nPresione enter para salir.')
        
    else:
        print('\nRespuesta no reconocida, por favor intente de nuevo.')