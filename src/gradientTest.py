#gradient descent learning
#steven 29/02/2020 Initial
#11/03/2020  add plotSeekPoint to plot the seek process
#import random
import matplotlib.pyplot as plt
import numpy as np
from plotCommon import plotSub

def difference_derivative(f,x,h=0.00001): #one parameter fuction derivate
    return (f(x+h)-f(x))/h

def question_linearFuc(x):
    a = 6.5   #must a > 0
    b = 1.88 #the final optimum x
    c = -8.8  #the final minimum value
    return a*(x - b)**2 + c

def question_linearFucMin():
    """seek x, make f(x) = ax^2 + bx + c (a>0)  minimize
    this fuction is always as the simplest(one feature data) cost fuction in machine learning
    """

    #tolerance = 0.0000000001  #1.0e-15
    #max_iter = 10000
    iter = 0
    alpha = 0.001 #0.01 #learning rate
    seekList=[]

    x = -10  #random.random()
    stepInter = 0
    while True:
        gradient = difference_derivative(question_linearFuc,x,h=0.0001)

        x_next = x - alpha * gradient

        if iter % 20 == 0:
            print(iter," :",x,gradient,x_next,question_linearFuc(x),stepInter)
            seekList.append(x)

        #stepInter = (question_linearFuc(x) - question_linearFuc(x_next))**2
        stepInter = abs(question_linearFuc(x) - question_linearFuc(x_next))
        #if (stepInter < tolerance) or (iter > max_iter) :
        #if (stepInter - tolerance == 0) or (iter > max_iter) :
        #if (stepInter == 0) or (iter > max_iter) or (x - x_next == 0):
        if (stepInter == 0) or (x - x_next == 0):
            break

        x = x_next
        iter += 1

    print (iter,'result: x=',x, 'minValue:',question_linearFuc(x))

    plotSeekPoint(seekList)

def plotSeekPoint(seekList):
    _, ax = plt.subplots()

    x = np.linspace(-10,10,20)
    y = question_linearFuc(x)
    ax.plot(x,y) #plot function curve

    print(len(seekList))
    x = np.array(seekList)
    y = question_linearFuc(x)
    ax.scatter(x, y, s=10, color='r', alpha=0.75) #plot seekpoint in the seeking process
    plt.show()

def question_CurvePeakAndValley():
    """seek x, findout all curve's peak and valleys, that is where the derivative equal to 0"""
    def func(x):
        #return x**4
        #return  (x**3 + 3*x**2-6*x-8)/4
        return x**5 + 2*x**4 + 3*x**3 + 8*x**2 + 10*x

    x = np.linspace(-1.25,-0.65, 100)
    z0=[]
    for i, _ in enumerate(x):
        if i>=len(x)-1:
            break
        d1 = difference_derivative(func,x[i])
        d2 = difference_derivative(func,x[i+1])
        if d1*d2<=0:
            print('x = ',x[i])
            z0.append(x[i])
        #print('d1,d2,* = ',d1,d2,d1*d2)

    ax = plt.subplot(1,1,1)
    plotSub(x, func(x), ax, label='func',color='b')
    for k in z0:
        plt.vlines(k, np.min(func(x)), func(x[-1]),linestyles='dotted', color='r')
    #plt.axis('square')
    plt.legend()
    plt.grid()
    plt.show()

def main():
    #question_linearFucMin()
    question_CurvePeakAndValley()

if __name__ == '__main__':
    main()
