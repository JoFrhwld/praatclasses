import pandoc
import os

pandoc.core.PANDOC_PATH = '/usr/local/bin/'

doc = pandoc.Document()
doc.markdown = open('README.md').read()
#f = open('README.rst','w+')
print(doc.rst)
#f.close()
#os.system("setup.py register")
#os.remove('README.rst')