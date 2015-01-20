from setuptools import setup

longDescription='''
Utilities that are designed to make it relatively easy to interact with the file
system and run commands.
'''

setup(
    name='scripts'
  , version='1.0.0'
  , description='Scripting Utilities'
  , long_description=longDescription
  , author="Ken Kundert"
  , author_email='ken@designers-guide.com'
  , py_modules=['scripts']
  , use_2to3 = True
)
