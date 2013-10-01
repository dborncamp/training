'''
ABOUT:
This program contains everything needed for all of the training manual.

DEPENDS:
Python 2.7.3

AUTHOR:
Dave Borncamp STScI 2013/9/30

USE:
python everything.py
'''

__author__='Dave Borncamp STScI 2013/9/30'
__version__=0.4


#global imports
import glob #used in Exercise 7
import numpy #used in Exercise 8
import random #used in Exercise 12
import pdb
import pyfits
import matplotlib.pyplot as plot

'''
MyFirstScript made into a function for Exercise 14
'''
def MyFirstScript():
    Mself='MyFirstScript'

    print Mself+' starting'
    
    gordon='/user/ely/RIAB/Gordon2005_Fig16.txt' #the infile
    outfile='fig16_log.pdf'
    
    slope, ran_slope_unc, corr_slope_unc, both_slope_unc, \
       eqn_slope_unc, ran_yint_unc, corr_yint_unc, both_yint_unc, \
       eqn_yint_unc = numpy.loadtxt(gordon, unpack=True)
    
    #rename variables so they are easily typeable
    xx = slope
    yy1 = ran_slope_unc
    yy2 = corr_slope_unc
    yy3 = both_slope_unc
    yy4 = eqn_slope_unc
    
    #create figure object
    figure,ax=plot.subplots()
    
    #add things to the plot
    ax.loglog(xx, yy1, ls='--', lw=3, color='b', label='Random Unc.')
    ax.loglog(xx, yy2, ls=':', lw=3, color='r', label='Correlated Unc.')
    ax.loglog(xx, yy3, ls='-', lw=3, color='g', label='Both')
    ax.loglog(xx, yy4, ls='-.', lw=3, color='m', label='Equation')
    
    #make labels
    ax.set_xlabel('Slope [e-/s]')
    ax.set_ylabel('Slope Uncertainty [e-/s]')
    ax.legend(loc='best')
    
    #show the plot
    figure.show()
    
    #save the file
    print 'saving file as '+outfile
    figure.savefig(outfile)
    figure.clf()
    
    print Mself+' ending'
    return

def mkplot(outfile,xx,yy1,yy2,yy3,yy4,ylab='Slope Unc. [e-/s]'):
    pself='mkplot'
    print pself+' starting'
    
    figure, ax = plt.subplots()
    
    pdb.set_trace()
    
    ax.set_xlabel('Slope [e-/s]')
    ax.set_ylabel('Slope Uncertainty [e-/s]')
    ax.plot(xx, yy1, ls='--', color='b', label='Randon Unc.')
    ax.plot(xx, yy2, ls=':', color='r', label='Correlated Unc.')
    ax.plot(xx, yy3, ls='-', color='g', label='Both')
    ax.plot(xx, yy4, ls='-.', color='m', label='Equation')
    ax.legend(loc='best')
    
    figure.show()
    figure.savefig(outfile)
    figure.clf()
    print 'Saved file to: ',outfile
    return




'''
Main program
'''
def main():
    #Exercise 1
    print ' Exercise 1: '
    dictionary={'Dave':'first','Borncamp':'last'}
    print dictionary
    print ' '
    
    for i in dictionary:
       print i
    
    print ' '
    
    
    #Exercise 2
    print ' Exercise 2: '
    print 'This whole script will be printed.\n'
    
    
    #Exercise 3
    print ' Exercise 3: '
    print 'Looked at help() seemed useful... \n'
    
    
    #Exercise 4
    print ' Exercise 4: '
    a=range(10)
    vectors=[]
    
    for i in a:
       vectors.append(i ** i)
    print 'The vectors are: '
    
    print vectors
    print ' '
    
    
    #Exercise 5
    print ' Exercise 5: '
    a=range(4)
    dates=[]
    year='2001-0'
    month='-01'
    
    for i in a:
       dates.append(year+str(i+1)+month)
    print dates
    print ' '
    
    
    #Exercise 6
    print ' Exercise 6: '
    a=range(5)
    
    for i in a:
       try:
          print 1.0/i
       except ZeroDivisionError:
          print 'Denomenator is: '+str(i)+', cannot divide by zero!!'
          #I print this off just to make sure it is 0
    print ' '
    
    
    #Exercise 7
    print ' Exercise 7: '
    #since I try not to keep files on my desktop I will search somewhere else...
    print 'Print the scripts I currently have in my IDL folder:'
    files=glob.glob('/Users/dborncamp/idl/*.pro')
    
    for i in files:
        print i
    print ' '
    
    
    #Exercise 8
    print ' Exercise 8: '
    a=[1,2,3,4,5]
    b=numpy.array([1,2,3,4,5])
    print ' Multiply list and array by 2:'
    print a*2,' it made 2 of the list.'
    print b*2,' it doubled every element in the array.'
    print ' add 2 to list and array.'
    print 'list crashed when I tried a+2. Said can only concatenate list to list.' 
    print b+2,'every element has 2 added to it.\n'
    
    
    #Exercise 9
    print ' Exercise 9: '
    c=[6,7,8]
    print a+c,' appended c to the end of a.'
    print 'crashed when I tried to do b+c, operands could not broadcast together with shapes.\n' 
    
    
    #Exercise 10
    print ' Exercise 10: '
    test=numpy.arange(.1,1.5,.1)
    print test
    print ' '
    
    
    #Exercise 11 
    print ' Exercise 11: '
    test=numpy.arange(.1,1.5,.1)
    print test
    test=numpy.arange(-3.2,-.9,.2)
    print test
    print ' '
    
    
    #Exercise 12
    print ' Exercise 12:'
    a=range(10)
    b=[]
    
    for i in a:
        r=random.random()
        b.append(r)
    
    c=numpy.array(b)
    print c[c>.5]
    print ' '
    
    
    #Exercise 13
    print ' Exercise 13: '
    print 'Looks like a column table with all of the information needed to recreate the plot.'
    print 'If you unpack it it reads by column, if not, it reads by line.\n'
    
    
    #Exercise 14
    print ' Exercise 14: '
    print 'I decided to add this as a function instead of another script, so here it is: '
    MyFirstScript()
    
    
    #Exercise 15
    print ' Exercise 15: '
    print 'I am using version:',__version__
    print 'It does list an author.\n'
    
    
    #Exercise 16
    print ' Exercise 16: '
    print 'Good to know what happens.\n'
    
    
    #Exercise 17
    print ' Exercise 17: '
    print 'Good to know how to debug.\n'
    
    
    #Exercise 18
    print ' Exercise 18: '
    print 'An instance is a.'
    print 'An attribute is side.'
    print 'A method is area formula.'
    print 'Function is GetArea. \n'

    
    #Exercise 19
    print ' Exercise 19: '
    print 'Classes are here.'
    
    
    #Exercise 20
    print ' Exercise 20: '
    print 'See file MyPyraf.py \n'
    
    return

class FitsClass(object):
    def __init__(self,filename,hdr,data):
        self.filename=filename
        self.hdr=hdr
        self.data=data
    
    def NewName(outname):
        rename(self.filename,outname)

if __name__ == '__main__':
    main() 


