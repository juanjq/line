import numpy as np
import matplotlib.pyplot as plt

import httpimport
with httpimport.remote_repo(['line'], 'https://raw.githubusercontent.com/juanjq/lines/main'):
     import line

#we define a clas for linear regressions
class Linear:
    
    #init function
    def __init__(self,x,y):
        
        #we need valid data
        if len(x) != len(y):
            print('Error: x,y arrays don\'t have same length')
          
        #lenght of the data arrays  
        else:
            self.N = len(x)
        
        #average values and deviations
        xavg = np.mean(x)
        yavg = np.mean(y)
        sxy = sum([(x[i]-xavg)*(y[i]-yavg) for i in range(len(x))])
        sxx = sum([(x[i]-xavg)**2          for i in range(self.N)])
        syy = sum([(y[i]-yavg)**2          for i in range(self.N)])

        #defining the slope (B), the intercept (A), and the R^2 value
        self.B = sxy/sxx
        self.A = yavg-self.B*xavg
        self.R = sxy**2/sxx/syy

        devy = np.sqrt(sum([(y[i]-self.A-self.B*x[i])**2 for i in range(self.N)])/(self.N-2))
        norm = self.N*sum(list(map(lambda x: x**2, x)))-sum(x)**2
          
        #now the standard deviations of slope and intercept
        self.uA = devy*np.sqrt(sum(list(map(lambda x: x**2, x)))/norm)
        self.uB = devy*np.sqrt(self.N/norm)
     
    #defining a function that print the results
    def results(self):
        print('slope = '+str(round(float(self.B),2))+'+-'+str(round(float(self.uB),2))+'\n')
        print('y-intercept = '+str(round(float(self.A),2))+'+-'+str(round(float(self.uA),2))+'\n')
        print('R² = '+str(round(float(self.R),7))+'\n')
    
    #slope attribute
    def B(self):
        return self.B
     
    #uncertainty of slope attribute
    def uB(self):
        return self.uB  
     
    #y intercept attribute
    def A(self):
        return self.A

    #uncertainty of y intercept attribute 
    def uA(self):
        return self.uA
     
    #value of R^2 attribute
    def R(self):
        return self.R
    
    #plot a the line
    def plot(self,ax,color='darkblue',linestyle='-'):
        line.line(self.B,self.A,ax,mode='slope',color=color,linestyle=linestyle)
        

class Polynomial:
    
    #main function
    def __init__(self,x,y,degree):
     
        #checking if data is valid
        if len(x) != len(y):
            print('Error: x,y arrays don\'t have same length')
        
        #we use polyfit methods
        self.coef   = np.polyfit(x,y,degree)
        self.degree = degree
        
    #plotting the results
    def results(self):
        text=''
        for i in range(self.degree+1):
            if i == 0:
                text=text+str(round(float(self.coef[-1-i]),2))
            elif i == 1:
                if (self.coef[-1-i]>=0):
                    text = text+'+'+str(round(float(self.coef[-1-i]),2))+'x'                
                else:
                    text = text+'-'+str(abs(round(float(self.coef[-1-i]),2)))+'x'
            else:
                if (self.coef[-1-i]>=0):
                    text = text+'+'+str(round(float(self.coef[-1-i]),2))+'x^'+str(i)                
                else:
                    text = text+'-'+str(abs(round(float(self.coef[-1-i]),2)))+'x^'+str(i) 
        print(text)
    
    #array of coefficients
    def coefs(self):
        
        return [float(self.coef[-1-k]) for  k in range(self.degree+1)]
    
    #plot a the curve
    def plot(self, ax, color = 'darkblue',linestyle='-'):
        
            right = ax.get_xlim()[1]
            left  = ax.get_xlim()[0]
            
            x_graf = np.linspace(left,right,400)
            y_graf = [ sum([ self.coef[-1-j]*x_graf[i]**j for j in range(self.degree+1)]) for i in range(400)]
            
            col = LineCollection([np.column_stack((x_graf,y_graf))], colors=color,linestyle=linestyle,antialiased=True)
            ax.add_collection(col, autolim=False)
            
