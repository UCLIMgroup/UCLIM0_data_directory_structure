# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 12:05:20 2021

@author: Jesus Lizana

"""

import os

#geodata
import geopy
from geopy import distance
                       
#%%	
###########################################################

#INPUT DATA required to select city

###########################################################

city = "Paris"

#location and extent
lat = 48.83
long = 2.349092294549077
plot =  75  # to define the grid size to map in km (kmxkm), e.g. 70 = 70x70km2


#timeframe for data extraction -- day-month-year
first_date='01-01-2023 00:00'  
last_date='31-12-2023 23:00'

#Timeframe criteria to eliminate statations with data availability <90%  -- day-month-year
first_date1='20-05-2023'  
last_date1='20-09-2023'

#colors
color_net = 'lightskyblue' 
color_wund ="royalblue" 
color_ows ='k'
color_cws = 'blue'
color_outliers = 'r'


                       
#%%	

###########################################################

#INTERNAL VARIABLES - automatically calculated - don't modify

###########################################################

#Directories
cwd_project = os.path.dirname(__file__)

# Now using os.path.join for all paths to ensure compatibility across different OS

#data
cwd_data_raw = os.path.join(cwd_project, "data", "10_raw")
cwd_data_raw_netatmo = os.path.join(cwd_project, "data", "10_raw","netatmo")
cwd_data_raw_wunder = os.path.join(cwd_project, "data", "10_raw","wunder")

cwd_data_str = os.path.join(cwd_project, "data", "11_structured")

cwd_data_qc = os.path.join(cwd_project, "data", "20_quality_control")
cwd_data_gap = os.path.join(cwd_project, "data", "21_gap_filling")

cwd_data_spatial = os.path.join(cwd_project, "data", "30_generation_spatial")
cwd_data_temporal = os.path.join(cwd_project, "data", "30_generation_temporal")

cwd_data_analysis = os.path.join(cwd_project, "data", "40_analysis")
cwd_data_application = os.path.join(cwd_project, "data", "50_application")


#results
cwd_results_raw = os.path.join(cwd_project, "results", "10_raw")
cwd_results_raw_netatmo = os.path.join(cwd_project, "results", "10_raw","netatmo")
cwd_results_raw_wunder = os.path.join(cwd_project, "results", "10_raw","wunder")

cwd_results_str = os.path.join(cwd_project, "results", "11_structured")

cwd_results_qc = os.path.join(cwd_project, "results", "20_quality_control")
cwd_results_gap = os.path.join(cwd_project, "results", "21_gap_filling")

cwd_results_spatial = os.path.join(cwd_project, "results", "30_generation_spatial")
cwd_results_temporal = os.path.join(cwd_project, "results", "30_generation_temporal")

cwd_results_analysis = os.path.join(cwd_project, "results", "40_analysis")
cwd_results_application = os.path.join(cwd_project, "results", "50_application")


                      
#%%	

#Definition of extent - frame for mapping
dist = plot/2
center_pt = [lat,long]

#calculation of zoom in coordenadas
# given: lat1, lon1, b = bearing in degrees, d = distance in kilometers
origin = geopy.Point(center_pt)

#lat
a = distance.distance(kilometers=dist).destination(origin,0) #lat
lat_d = repr(a[0])
lat_d = float(lat_d) - float(lat)

#long
b = distance.distance(kilometers=dist).destination(origin,90) #lat
lon_d = repr(b[1])
lon_d = float(lon_d) - float(long)
 
#Definition of extent - frame for mapping
extent = [center_pt[1]-lon_d,center_pt[1]+lon_d,center_pt[0]-lat_d,center_pt[0]+lat_d] # adjust to zoom  


