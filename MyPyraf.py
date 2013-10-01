#! /usr/bin/env python


import pyraf,glob,os
from pyraf import iraf
from iraf import noao, digiphot, daophot

infile='n9vf01hfq_ima.fits'

iraf.daofind(image=infile+'[1]')

filelist=glob.glob('*_ima.fits')
print ' Found files: \n'
print filelist

for file in filelist:
   query=os.access(file+'1.coo.1')
   if query:
      os.remove(file+'1.coo.1')
   iraf.daofind(image=file+'[1]', interactive='no', verify='no')

iraf.daofind.unlearn()   


