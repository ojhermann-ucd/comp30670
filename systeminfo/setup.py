from setup import setup
from scipy.optimize._tstutils import description
from pip._vendor.requests import packages
import systeminfo

setup(name="systeminfo",
      version="0.1",
      description="Basic system information for comp30670",
      url="",
      author="Otto Hermann",
      author_email="otto.hermann@ucdconnect.ie",
      license="GPL3",
      packages=['systeminfo'],
      entry_points={
          'console_scripts':['comp30670_systeminfo=systeminfo.main:main']
          }
    )