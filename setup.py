# -*- coding: utf-8 -*-
from distutils.core import setup
setup(
    name='m3_project.app',
    version='0.1.0',
    packages=['app', ],
    py_modules=['manage','m3_project/settings','m3_project/urls'],
    requiries=["django==1.11", "m3-objectpack==2.2.25"],
)