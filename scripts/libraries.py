

#the code "pipreqs ." is used to generate the requirement.txt file
#however, this code doesn't work properly with notebooks
#this file is used to list all the libraries used in the project
#to that "pipreqs ." is able to generate automatically the requirement.txt file

#All libraries used in the notebooks should be listed here. Verify if all libraries are listed before running "pipreqs ."


import os

import numpy as np 
import matplotlib.pyplot as plt

#cartopy
import cartopy 
import cartopy.crs as ccrs
import cartopy.io.img_tiles as cimgt
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

import geopy
from geopy import distance

