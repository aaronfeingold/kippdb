### Description:
This python application offers services to connect to and query a MSSQL database warehouse.

In test are the exporter and tableauServerClient modules. 

Main.py will run the perform the task of querying a specific database for all its tables, and the
views, stored procedures, and triggers associated to each table.

Ultimately, this will allow a datateam to map out all the relation between a sql table to the programs
or applications which are used to insert data into that table.

Thus, when identifying what table or views are extracted to Tableau, it will then be streamlined to simply 
identify the where along the chain exists the source data. This will help in decreasing troubleshooting time
by already having these sql query results availble to search. 

### Usage steps:

## Download and Install

1. Click the green button "Code". Drop down menu will give a few ways to download to your machine.

  - Not familiar with forking, cloning, or using the git cli? Simply download the zip file, and unzip it.

2. In a command terminal/shell, change into the root directory of the project:
  - download and install dependacies with pip: pip install

## Update secretsTemplate.json

1. There is a file in the root directory called secretsTemplate.json
  - This file must be updated manually to represent your secrets
  - ie: usernames and passwords which you do not want uploaded to the web
  - fill in the correct data
  - rename the file to: secrets.json
  - the .gitignore file is written to exlude this from being commited to a cloud repository

2. please reach out to me at ajfeingold88@gmail.com with questions to fill this out.

## Run Main.py

1. If dependancies are downloaded, including python, in the root directory in your command line/shell
 - run: python main.py
2. There are lot of tables being queried and many requests, so it may take some time. The command line will print status on each table, 
and return complete when it has run. 
3. The data will be saved to a file called map.csv. You can copy and paste from that file into a spreadsheet editor of your choice.
  - google sheets for instance.



