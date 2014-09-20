
import re
import os

METAPAT = re.compile(b'="[\D|\s]*"')

def pdfcleaner(path):
    if not os.path.isfile(path):
        raise FileNotFoundError
    base, name = os.path.split(path)
    newname = name.replace('.pdf', '_cleaned.pdf')
    saveto  = os.path.join(base, newname)
    open(saveto, 'wb').write(METAPAT.sub(b'=""', open(path, 'rb').read()))
    os.remove(path)
    return os.path.join(base, newname)
