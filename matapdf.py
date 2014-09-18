
import re
import os

METAPAT = re.compile(b'="[\D|\s]*"')

def clean_pdf(path, overwrite=False):
    if not os.path.isfile(path):
        raise FileNotFoundError
    newname = 'clean_' + os.path.split(path)[1]
    saveto  = os.path.join(os.path.split(path)[0], newname) 
    if overwrite:
        saveto = path
    open(saveto, 'wb').write(METAPAT.sub(b'=""', open(path, 'rb').read()))

    return newname
