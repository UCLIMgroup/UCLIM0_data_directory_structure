# UCLIM0 - Data Directory Structure [v0.1]  

Code to create the directory structure for your city project, to save all your files following the UCLIM framework. 

Every time you start a new project, you need to open this code and create a new directory structure for your project. 

All repositories in UCLIM will follow this data structure. 

## How to use **UCLIM0_data_directory_structure**?

The approach is divided into different Jypyter Notebooks to guide the workflow.

- **Notebook 00_NewProject** - Define and create the new project directory to save and process data. 


Once you have created the project folder structure, copy an existing "config_porject.py" to your "projectname/" folder. 
You should also have a "credentials.py" file in your "local_directory_folder/". 

You can find examples of "config_porject.py" and "credentials.py" in the folder [z_project_data_example](https://github.com/UCLIMgroup/UCLIM0_data_directory_structure/tree/main/z_project_data_example)


## The directory structure
------------

The directory structure of the UCLIM framework looks like this: 

```
local_directory_folder/         <- directory defined in path_to_data.txt
│             		
├── projectname1/			<- Database divided by project (city) - Example: London
│   ├─ data/
│   	├─ 10_raw/
│   	├─ 11_structured/
│   	├─ 20_qualitycontrol/
│   	├─ 21_gap_filling/
│   	├─ 30_generation_spatial/
│   	├─ 31_generation_temporal/
│   	├─ 40_analysis/
│   	├─ 50_application/
│
│   ├─ results/
│   	├─ 10_raw/
│   	├─ 11_structured/
│   	├─ 20_qualitycontrol/
│   	├─ 21_gap_filling/
│   	├─ 30_generation_spatial/
│   	├─ 31_generation_temporal/
│   	├─ 40_analysis/
│   	├─ 50_application/
│ 
│   ├─**config_porject.py**     <- Specific config file with project info (name, dates, coordinates, etc.)
│
├── projectname2/
│   ├─ data/
│       ├─...
│
│   ├─ results/
│       ├─...
│
│   ├─**config_porject.py**
│
├─ **credentials.py**           <- Private file with usernames, passwords and API tokens
│
└──
```

