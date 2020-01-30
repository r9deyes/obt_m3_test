from distutils.core import setup, Extension
setup(
    name='m3_project.app',
    version='0.1.0',
    packages=['app',],
    #requiries=["django==1.11", "m3-objectpack==2.2.25"]
    scripts=['__setup_script.py',]
)