# PYTHON-DRONE-OPERATOR

### WINDOW VERSION

**library dependency and installation**

    pdcurses 
    
    > https://sourceforge.net/projects/pdcurses/files/pdcurses/
    
    or
    
    > 
    
    install : paste in [install python drive]:\Python27 = [pdcurses.dll repository]

    unicurses
    
    > https://sourceforge.net/projects/pyunicurses/files/latest/download
    
    or
    
    >
    
    install : click .exe file and select python directory and install
    
    >open text editor [install python drive]:\Python27\Lib\site-packages\unicurses.py 
    
    >search txt pdcurses.dll all line and replace [pdcurses.dll repository]\pdcurses.dll all line > save
    
    >run [python compiler] > import unicurses > if not error..it'work
    
    colorama[optional]
    
    > https://pypi.python.org/pypi/colorama
    
    or
    
    >
    
    install : >download colorama >goto colorama directory >run [python compiler] setup.py install


**font install and setting in command prompt in window** 

    *recommend > FreeMono [font]

    get font and paste in C:\Windows\Fonts

    run > regedit > HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Console\TrueTypeFont
    
    new > string value > set value name > 00 > value data > fontname Ex.Consolas,FreeMono
    
**command prompt full screen setting**

    cmd > wmic > exit
    
### LINUX VERSION
