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


#Codigo para el metofo biseccion
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

#Codigo para el metodo de aproximaciones susesivas