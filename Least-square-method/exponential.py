welcome="""
#*#*#*#*#*#*#*#*#**#*#*#*#**#*#*#*#**#*#*#*#*#*#**#*#*#*#**#*#*#*#**#*#
#*                                                                   #*
#*                        Curve Fitting                              #*
#*                              By                                   #*
#*                     Least Square Method                           #*
#*       Find the Exponential Curve that BEST fits for your data     #*
#*                                                                   #*
#*#*#*#*#*#*#*#*#**#*#*#*#**#*#*#*#**#*#*#*#*#*#**#*#*#*#**#*#*#*#**#*#
"""
print(welcome)

import numpy as np
import math
from tabulate import tabulate
x=[]
y=[]
try:
    n=int(input("How many number of sets you've got there? \n n= "))
    print('-'*70)
    print("Let, y=ae^(bx) or Y=A+Bx where Y=log10(y) , A=log10(a) and B=blog10(e) ")
    print('-'*70)
    #taking x values
    print("\nInput values of x: ")
    for i in range(1,n+1):
        xnum=float(input(f" x{i} = "))
        x.append(xnum)
    #taking y values
    print("\nInput values of y:")
    for j in range(1,n+1):
        ynum=float(input(f" y{j} = "))
        y.append(ynum)
    #making x square row
    squarex=[a*a for a in x]
    #making Y=log10(y) row
    Y=[math.log10(b) for b in y]
    #making x*y row
    multi=[a*b for a,b in zip(x,Y)]
    #table
    table=[(p,q,r,s,t) for p,q,r,s,t in zip(x,y,Y,squarex,multi)]
    headers=['x','y','Y=log10(y)','x^2','xY']
    print(tabulate(table,headers,tablefmt="pretty"))
    #table summation
    sumx=sum(x)
    sumy=sum(y)
    sumY=sum(Y)
    sumsquarex=sum(squarex)
    sumxY=sum(multi)
    #table2
    table2=[(sumx,sumy,sumY,sumsquarex,sumxY)]
    headers2=['∑x','∑y','∑Y','∑x^2','∑xY']
    print(tabulate(table2,headers2,tablefmt="pretty"))

    print(f"\nEquation 1 is: {sumY} = {n} A + {sumx} B")
    print(f"Equation 2 is: {sumxY} = {sumx} A + {sumsquarex} B")
    #solve liner equations
    M=np.array([[n,sumx],[sumx,sumsquarex]])
    N=np.array([sumY,sumxY])
    X=np.linalg.solve(M,N)
    #solve a and b
    a=math.pow(10,X[0])
    b=X[1]/(math.log10(math.e))
    print(f"Hence, the required curve is: y={a} e^({b} x)")
except:
    print("\nNo.. input is not a number. It's a string.")
    print("Please input number to continue your calculation")
