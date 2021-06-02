# Database System Map API for Tableau dashboard troubleshooting

## Description:
This python application offers services to connect to and query a MSSQL database warehouse.

Please take care to observe the details in the usage steps.

Note: In test are the exporter and tableauServerClient modules. They are not set to run from main.py currently.

Main.py will perform the task of querying a specific database within a warehouse for all its tables, and the
views, stored procedures, and triggers associated to each table, exporting to map.csv.

Ultimately, this will allow a datateam to identify the relation between a sql table to the programs
which are inserting data into that table.

Thus, when identifying what table or views are extracted to Tableau, it will then be streamlined to 
identify where along the conections exists the source data, and how that data is fed to Tableau.

This will help in decreasing troubleshooting time by already having at hand the results of many system
queries within the map.csv. In conjunction with google sheets and docs files, the approach to determining
the data flow will be concretized. 

## Usage steps:

### Download and Install

1. Click the green button "Code". Drop down menu will give a few ways to download to your machine.
  - Not familiar with forking, cloning, or using the git cli? Simply download the zip file, and unzip it.

2. In a command terminal/shell, change into the root directory of the project:
  - download and install dependacies with pip: pip install

3. Trouble with not having the right package manager program, or adding bash commands to you PATH? 
  - feel free to email me at ajfeingol88@gmail.com with questions
  - if we can then schedule a zoom call, I'd be more than happy to walk you through that.

### Update secretsTemplate.json

1. There is a file in the root directory called secretsTemplate.json
  - This file must be updated manually to represent your secrets
  - ie: usernames and passwords which you do not want uploaded to the web
  - fill in the correct data
  - rename the file to: secrets.json
  - the .gitignore file is written to exlude secrets.json and NOT the template from being commited to a cloud repository
  - thus, not renaming it will expose these secrets. Do not let that happen.

2. Please reach out to me at ajfeingold88@gmail.com with questions to fill this out.

### Run Main.py

1. If dependancies are downloaded, including python, in the root directory in your command line/shell
  - run: python main.py
2. Note: There are lot of tables being queried and many requests, so it may take some time. 
  - The command line will print table names after completion, and return "Complete" when done. 
3. The data will be saved to a file called map.csv. 
  - You can copy and paste from that file into a spreadsheet editor of your choice.
  - google sheets for instance.



