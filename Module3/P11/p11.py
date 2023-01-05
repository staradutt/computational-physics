
def f1(x,y):#given function
    return (y**2)*(1-x)-x** 3
def g1(x,y):
    return y**2+x** 2-1

def f1_x(x,y):#df/dx
    return -y**2-3*x**2
def f1_y(x, y):#df/dy
    return 2*y*(1-x)

def g1_x(x,y):#dg/dx
    return 2*x
def g1_y(x,y):
    return 2*y#dg/dy

def solve(f, g, f_x, g_x, f_y, g_y, xguess, yguess, tol):

    x=xguess
    y=yguess
    while (abs(f(x,y))>tol) or (abs(g(x,y)) > tol):
        x+=(f_y(x,y)*g(x,y)-g_y(x,y)*f(x,y))/(f_x(x,y)*g_y(x,y)-f_y(x,y)*g_x(x,y))
        y+=(g_x(x,y)*f(x,y)-f_x(x,y)*g(x,y))/(f_x(x,y)*g_y(x,y)-f_y(x,y)*g_x(x,y))
    
    if abs(x.imag)<tol:
        x=x.real
    if abs(x.real)<tol:
        x=x.imag*(1j)
    if abs(y.imag)<tol:
        y=y.real
    if abs(y.real)<tol:
        y=y.imag*(1j)
    return (x,y)
f = open("out.txt", 'w')
f.write("\nroot1  =  " + str(solve(f1, g1, f1_x, g1_x, f1_y, g1_y, 1, 1, 1e-14)))
f.write("\nroot2  =  " + str(solve(f1, g1, f1_x, g1_x, f1_y, g1_y, 1, -1, 1e-14)))
f.write("\nroot3  =  " + str(solve(f1, g1, f1_x, g1_x, f1_y, g1_y, 1j, 1j, 1e-14)))
f.write("\nroot4  =  " + str(solve(f1, g1, f1_x, g1_x, f1_y, g1_y, -1j, -1j, 1e-14)))
f.close()
