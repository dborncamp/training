
#!/usr/bin/env python
'''
About: 
    This python module contains tools I commonly use.

Depends:
    ds9,pyds9,pyfits

Author:
    Roberto J. Avila - Orginal Author
    Dave Borncamp

History:
    9 November 2013 - DB clean up a few things. Add documentation.
    25 July 2012 - Added tvmark function
    24 July 2012 - Added limits function
    5 July 2012 - Added xtalk correction function
    27 April 2012 - Initial version

Current version:
    0.4.0
'''
__author__ = 'Dave Borncamp'
__version__ = '0.4.0'

def limits(nframes,camera,channel,pixscale):
    '''
    Set the limits of ACS/WFC and WFC3/UVIS & WFC3/IR. 
    '''

    import math

    if (camera.lower() == 'wfc3') & (channel.lower() == 'uvis'):
        rn = 3.2
        well = 60000.0
        scale = pixscale/0.04

    elif (camera.lower() == 'wfc3') & (channel.lower() == 'ir'):
        rn = 12.0
        well = 70000.0
        scale = pixscale/0.13

    elif (camera.lower() == 'acs') & (channel.lower() == 'wfc'):
        rn = 5.1
        well = 84000.0
        scale = pixscale/0.0495
        
    else:
        print '** The camera you are using wasn\'t found. Please check your input.\n'
        return 1

    new_rn = math.sqrt(nframes*(rn*scale)*(rn*scale))
    new_well = nframes*well*(scale*scale)

    print 'New readout noise is: {}'.format(new_rn)
    print 'New full well is: {}'.format(new_well)

def dq(x):
    '''
    Descriptions of problems with WFC3/IR pixels
    '''
    print 'These descriptions correspond to WFC3/IR'
    if (x & 0) > 0 : print '0: OK'
    if (x & 1) > 0 : print '1: Reed-Solomon decoding error'
    if (x & 2) > 0 : print '2: Data replaced by fill value'
    if (x & 4) > 0 : print '4: Bad detector pixel'
    if (x & 8) > 0 : print '8: Unstable in zero-read'
    if (x & 16) > 0 : print '16: Hot pixel'
    if (x & 32) > 0 : print '32: Unstable response'
    if (x & 64) > 0 : print '64: Warm pixel'
    if (x & 128) > 0 : print '128: Bad reference pixel'
    if (x & 256) > 0 : print '256: Full-well saturation'
    if (x & 512) > 0 : print '512: Bad or uncertain flat value'
    if (x & 1024) > 0 : print '1024: Reserved'
    if (x & 2048) > 0 : print '2048: Signal in zero-read'
    if (x & 4096) > 0 : print '4096: Cosmic ray detected by MultiDrizzle'
    if (x & 8192) > 0 : print '8192: Cosmic ray detected during up-the-ramp fitting'
    if (x & 16384) > 0 : print '16384: Pixel affected by ghost/crosstalk' 

def mdisplay(searchpattern,extension=1):
    '''
    Main point of program. Will search for a pattern and display it in ds9
    '''

    import glob,ds9

    imagelist = glob.glob(searchpattern)

    print imagelist
    print ''

    D = ds9.ds9()
    i = 1   #counter for image, makes sure ds9 has correct frame

    for image in imagelist:

        image = image+'[' + str(extension) + ']' 
        print image+' number: ',i,' of: ',len(imagelist)
        D.set('frame '+str(i))
        D.set('file '+image)
        i+= 1

    D.set('frame 1')
    D.set('scale log')
    D.set('scale limits 0 1000')
    D.set('match scales')
    D.set('match colorbars')
    D.set('match frames physical')

def mycatfits(searchpattern):
    '''
    Looks for the information of a search pattern
    '''

    import pyfits
    import glob

    imagelist = glob.glob(searchpattern)

    print imagelist
    print ''

    for im in imagelist:

        pyfits.info(im)
        print ''

def tvmark(image,coordfile):
    '''
    Marks things in a new ds9 window given a coordinate file that contains 
    x&y locations.
    '''

    import glob,ds9

    D = ds9.ds9()
    
    D.set('file '+image)
    D.set('regions -format xy -system image ' + coordfile)  
    D.set('scale log')
    D.set('scale limits 0 10000')

def xtalk_correct(searchpattern):
    '''
    Corrects xtalk for WFC3
    '''

    import glob
    import subprocess

    imagelist = glob.glob(searchpattern)

    print imagelist
    print ''

    for im in imagelist:

        print '-----------------------------------------------------------------------'
        command = '/Applications/itt/idl/bin/idl -e \"xtalk_correct_wfc3,\''+im+'\'\"'
        print command
        subprocess.call(command,shell=True)
        print ''
