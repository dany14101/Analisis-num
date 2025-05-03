import numpy as np

#Codigo para el metofo grafico
def grafico(punto_ini,error=1e-3,limite=50):
    act=punto_ini
    p=np.poly1d([4,5,1])
    for _ in range(limite):
        sig=p(act);
        if abs(act-sig)<error:
          break
        act=sig;
   
    return float(act)


#Codigo para el metodo biseccion
def biseccion(a,b,error=1e-3,limite=50):
    p=np.poly1d([4,5,1])
    for _ in range(limite):
        x=(a+b)/2
        y=p(x);
        if p(a)*y<0:
            b=x
        else:
            a=x
        if abs(y)<error:
            break
    return (x)

#Codigo para el metodo de la falsa posicion
def falsan(a,b,error=1e-3,limite=50):
    p=np.poly1d([4,5,1]) 
    for _ in range(limite):
        fa=p(a)
        fb=p(b)
        x=b-fb*((a-b)/(fa-fb))
        y=p(x)
        a1=p(a)
        if fa*y<0:
          b=x
        else:
           a=x
        if abs(y)<error:
            break
    return(x)

#Codigo para el metodo de punto fijo
def puntofijo(x0,error=1e-3,limite=50):
    p=lambda x:1*(3*x+2)
    for _ in range(limite):
        x1=p(x0)
        if abs(x1-x0)<error:
            break
        x0=x1
    return (x1)


#Codigo para el metodo de newton raphson
def newton(x0,error=1e-3,limite=50):
    f= lambda x:5*x*3+10*x+5     
    df= lambda x:15*x**2+10                
    for _ in range(limite):
        x1=x0-f(x0)/df(x0)
        if abs(x1-x0)<error:
            break
        x0=x1
    return (x1)

#Codigo para el metodo de secante
def secante(x0,error=1e-3,limite=50):
    f= lambda x:5*x**3+10*x+5  
    x1=x0+0.1   
    for _ in range(limite):
        fx0=f(x0)
        fx1=f(x1)
        x2=x1-fx1*(x1-x0)/(fx1-fx0)
        if abs(x2-x1)<error:
            return (x2)
        x0=x1
        x1=x2
    return (x1)

#Codigo para gauss jordan
def gaussjordan(M1,M2):
    M1=np.array(M1,dtype=float)
    M2=np.array(M2,dtype=float).reshape(-1, 1)
    RES=np.hstack([M1,M2])
    n=len(M2)
    
    for i in range(n):
        RES[i]=RES[i]/RES[i][i]
        for j in range(n):
            if i!=j:
                RES[j]=RES[j]-RES[j][i]*RES[i]
    
    return (RES[:,-1])

#Codigo para resolver por matriz diagonal superior
def diago_inferior(M1,M2):
    tam=len(M2)
    x=[0]*tam
    for i in range(tam):
        tot=sum(M1[i][j]*x[j] for j in range(i))
         x[i]=(M2[i]-tot)/M1[i][i]
    return (x)

# Metodo de jacobi
def jacobi(A, b,x0=None,error=1e-3,limite=50):
    A=np.array(A,dtype=float)
    B=np.array(b,dtype=float)
    tam=len(b) 
    if x0 is None:
        x0=np.zeros(tam)
    arr=x0.copy()
    for _ in range(limite):
        nuevo=np.zeros_like(arr)
        for i in range(tam):
            suma=sum(A[i][j]*arr[j] for j in range(tam) if j!=i)
            nuevo[i]=(b[i]-suma)/A[i][i]
        if np.linalg.norm(nuevo-arr,ord=np.inf)<error:
            return nuevo
        arr=nuevo.copy()
    return (arr)

# Metodo de Gaus seidel
def gaussseidel(A,b,x0=None,error=1e-3,limite=50):
    # convierte a flotantes
    A=np.array(A,dtype=float)
    B=np.array(b,dtype=float)
    tam=len(b)
    # checa que caso es
    if x0 is None:
        x0=np.zeros(tam)
    arr=x0.copy()
    # hace las iteraciones
    for _ in range(limite):
        # guarda el anterior
        anterior=arr.copy()
        for i in range(tam):
            suma=sum(A[i][j]*arr[j] for j in range(tam) if j!=i)
            arr[i]=(b[i]-suma)/A[i][i]
        # checa si se cumplio la condicion y ve el cambio
        if np.linalg.norm(arr-anterior,ord=np.inf)<error:
            return (arr)
    return (arr)

#Codigo para metodo trapecio
def trap(limab,limar,n): 
    h=(limar-limab)/n
    suma=funcion(limab)+funcion(limar)
    for i in range(1,n):
        xi=limab+i*h
        suma+=2*funcion(xi)     
    return float((h/2)*suma)

def funcion(x):
    return float (x**2)

#Codigo para simpson 1/3
def simpsontercio(limab,limar,n): 
    if n%2!=0:
        exit()
    h=(limar-limab)/n
    sumaimpar=sumapar=0
    suma=funcion(limab)+funcion(limar)
    for i in range(1,n):
        xi=limab+i*h
        if i%2==0:
         sumapar+=2*funcion(xi)    
        if i%2!=0:
         sumaimpar+=4*funcion(xi)    
    return float((h/3)*(suma+sumapar+sumaimpar)

#Codigo para simpson 3/8 (checar)
def simpsonoct(limab,limar,n): 
    if n%3!=0:
        exit()
    h=(limar-limab)/n
    suma1=suma2=suma3=0
    suma=funcion(limab)+funcion(limar)
    for i in range(1,n):
        xi=limab+i*h
        if i%3==0:
            suma3+=2*funcion(xi)
        else:
            suma1+=3*funcion(xi)
    return float((3*h/8)*(suma+suma1+suma2))