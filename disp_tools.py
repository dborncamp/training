
#!/usr/bin/env python
'''
About: 
    This python module contains tools I commonly use. Adapted from rja_tools.py 
    by Roberto Avila.

    This is assumed to be a 'first order' process, It will not throw any 
    exceptions like a 'good' program should, just yell at the user that they 
    are wrong.

Depends:
    ds9,pyfits,glob

Author:
    Roberto J. Avila - Orginal Author (rja_tools.py)
    Dave Borncamp

History:
    9 November 2013 - DB - clean up a few things I don't use. Add some error 
       checking and add documentation.
    25 July 2012 - Added tvmark function
    24 July 2012 - Added limits function (DB Removed 20131104)
    5 July 2012 - Added xtalk correction function (DB Removed 20131104)
    27 April 2012 - Initial version

Current version:
    0.4.0
'''
__author__ = 'Dave Borncamp'
__version__ = '0.4.0'


def mdisplay(searchpattern,extension=1):
    '''
    Main point of program. Will search for a pattern and display it in ds9.
    This function assumes that the data is in extension 1 by default.
      It will look at the same extension for all of the images.
    It will overwrite things in frames previously used.
    '''

    if (type(searchpattern) != str):
       print 'mdisplay requires a string to search for'
       return

    import glob,ds9

    imagelist = glob.glob(searchpattern)

    if (len(imagelist) == 0):
       print 'No images found using pattern:\n',searchpattern
       return

    print imagelist
    print ''

    D = ds9.ds9()
    i = 1  #counter for image, makes sure ds9 has correct frame, will overwrite

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
    Looks for the information of images in a search pattern.
    '''

    import glob,pyfits

    imagelist = glob.glob(searchpattern)

    if (len(imagelist) == 0):
       print 'No images found using pattern:\n',searchpattern
       return

    print imagelist
    print ''

    for im in imagelist:

        pyfits.info(im)
        print ''



def tvmark(image,coordfile):
    '''
    Marks things in a new ds9 window given a coordinate file that contains 
    x&y locations. It will use current ds9 frame if it is already active.
    '''

    import glob,ds9

    coord_test = glob.glob(corrdfile)

    if (len(coord_test) == 0):
       print 'No coordinate file found for: \n',coordfile
       return
    elif (len(coord_test) > 1):
       print 'Found more than 1 coordinate file for: \n',coordfile
       return

    D = ds9.ds9()
    
    D.set('file '+image)
    D.set('regions -format xy -system image ' + coordfile)  
    D.set('scale log')
    D.set('scale limits 0 10000')

