SCRAP_DATA

Description

In this Project we are trying to scrap the data table form the online dynamic website and the we are trying to print the data on the csv file and then we are pushing this table to the postgres database and trying to perform the CRUD operations on it.

Installation

Clone the Repository:
`Bash
git clone <repository-url>
cd <repository-directory>`


Install Dependencies:
`Bash
pip install -r requirements.txt`

Usage

1. Run the Scraping Script:

`Bash
python main.py`

This command will execute your main.py script, which presumably handles the scraping logic.


Access the PostgreSQL Database:

Prerequisites: 

Ensure you have PostgreSQL installed and running on your system.
  Adjust database connection details in your crud_operations.py or relevant file if necessary.

Steps:

a. Create the Database:
`Bash
psql -h <host> -U <username> -p <port> -c "CREATE DATABASE harshit_scrap;"`
Replace <host>, <username>, and <port> with your PostgreSQL server's credentials.

b. Connect to the Database (Optional):
You can use a tool like pgAdmin or the command line (psql) to connect to the scrap_data database and explore the scraped data.

For Performing the CRUD Operations :



You can run the file named curd_operations for operating the CRUD Opeations 


***Desclaimer Note: 

CRUD Operations can only be performed in the postgres database and the data is accessed from the database itself only. ***

For running the crud Operations run 
`Bash
crud_operations.py`

for Exporting the Csv file of the data run: 
`Bash
 generate_csv.py`

 
