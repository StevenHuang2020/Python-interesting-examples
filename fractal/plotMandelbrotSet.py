# Python3 steven
#https://en.wikipedia.org/wiki/Mandelbrot_set
import numpy as np
import matplotlib.pyplot as plt
# MandelBrot eqaution： z:=z**2 + c

def mandelbrot(N=10):  #generate madenlbrot series
    sets=[]
    c = complex(.1, .2)
    a = c
    while N>0:
        print(abs(a),' ',end='')
        sets.append(abs(a))
        a = a**2 + c

        N -= 1
    return sets

def yieldMandelbrot(N):  #binay oper only yield >2.0
    xvalues = np.linspace(-2, 2, N)
    yvalues = np.linspace(-2, 2, N)
    for u, x in enumerate(xvalues):
        for v, y in enumerate(yvalues):
            z = 0 + 0j
            c = complex(x, y)
            for i in range(100):
                z = z * z + c
                if abs(z) > 2.0:
                    yield v,u,abs(z)
                    break
 
def yieldMandelbrotAll(N):
    xvalues = np.linspace(-2, 2, N)
    yvalues = np.linspace(-2, 2, N)
    for u, x in enumerate(xvalues):
        for v, y in enumerate(yvalues):
            z = 0 + 0j
            c = complex(x, y)
            for i in range(100):
                z = z * z + c
                if abs(z) > 2.0:               
                    break
                yield v,u,abs(z)

def genMandelbrotColor(N=1000):  #color image,3 channels
    M = np.zeros([N, N,3], int) # + 255
    for v,u,z in yieldMandelbrotAll(N): #map z(0~2) to 0~255 pixsel value
        #M[v, u, :] = int(z*256/2)
        #M[v, u, 0] = int(z*256/2) #r channel     
        M[v, u, 1] = int(z*256/2) #g channel
        #M[v, u, 2] = int(z*256/2) #b channel             
    return M
                            
def genMandelbrotGray(N=1000):  #gray image[0~255]
    M = np.zeros([N, N], int)
    for v,u,z in yieldMandelbrotAll(N): #map z(0~2) to 0~255 pixsel value
        M[v, u] = int(z*256/2) #M[v, u] = 1                    
    return M
             
def genMandelbrot(N=1000):  #white&black two value[0,1] image
    M = np.zeros([N, N], int)
    if 1:
        for v,u,_ in yieldMandelbrot(N):
            M[v, u] = 1
        return M
    else:#First version
        xvalues = np.linspace(-2, 2, N)
        yvalues = np.linspace(-2, 2, N)
        for u, x in enumerate(xvalues):
            for v, y in enumerate(yvalues):
                z = 0 + 0j
                c = complex(x, y)
                for i in range(100):
                    z = z * z + c
                    if abs(z) > 2.0:
                        m[v,u] = 1
                        break
        return m

def main():
    #mandelbrot()
    #plt.imshow(genMandelbrot(),cmap='gray')
    #plt.imshow(genMandelbrotGray(),cmap='gray')
    plt.imshow(genMandelbrotColor(1000))
    plt.show()
    
if __name__=='__main__':
    main()
