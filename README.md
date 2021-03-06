
### Context

Name of the project: NYC safest path  
Context of the project: BeCode, Liège Campus, AI/Data Operator Bootcamp, January 2021  
Objective of the project: Given two addresses (or coordinates) in New York city, find the least dangerous path between those two points.  
We used the cleaned dataset, `data_100000_out_final.csv` from the [NYC Crashes Project](../content/4.machine_learning/0.data_preprocessing/nyc_crashes_project.md).  
In this previous project we have applied all the first required steps to do a data preprocessing based [on collected informations about all the traffic accidents that happened in New York City.](https://github.com/becodeorg/LIE-Thomas-1.26/blob/master/content/additional_resources/datasets/NYC%20Motor%20Vehicle%20Crashes/data_100000.csv)


### Description
In this project we create a Python script/application to find the safest path between the two given geographical locations in New York city.  
  
The dangerosity has been defined as the potential number of accidents on a specific path based on the number of accidents occured per year on that specific path.  
The number of accidents per street was previously weighted according to the severity of each accident.    
  
This algorithm find the least dangerous path and a graph of edges and vertices mapping to roads and intersections is given (Using OSMNX module).  
An interactive and more friendly  graphical web interface has been created using HTML and HTTP request.  


### Usage

You have to select (left click) directly your locations (an origin and a destination) in the map on the interactive interface and the safest path is found and shown on the map. 

An additional prepocessing phase has been added to addapt our data set to the OSMNX data base.



### Libraries & the requirements.txt
>Python, pandas, numpy, matplotlib, shapely.geometry, ipyleaflet, typing,..     
>Flask  
>request  
>render_template  
>flash  
>jsonify  
>json  
>os
>Bootstrap from flask_bootstrap  
>NYMapOSMnx from ny_map_osmnx  
>CSRFProtect from flask_wtf.csrf  
>networkx  
>osmnx   

### Pending things to do

There is not enough nodes to perfectly fit the shape of some streets in the OSNMX data base.  
Therefore, some optimal paths are ponctually visually off road on the map but remain the right solution.  
The alternative would be to find a module that outperforms the OSMNX.



### Authors

*Andreas Margraff, junior AI developer at BeCode;*

*Abdellah El Ghibzouri, junior AI developer at BeCode;*

*Ebubekir Kocadag, junior AI developer at BeCode;*

*Frédéric Fourré, junior AI developer at BeCode;*

*Pierre Wasilewski, junior AI developer at BeCode.*
