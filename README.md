# Sparkify ETL
## Project Description
The Sparkify music ETL pipeline is written in Python/Postgresql.
It allows the analysis of data that has been collected on songs and user activity on the Sparkify music streaming app, especially what songs users are listening to. As the original data (JSON format) cannot be queried in an easy way, the ETL reads in the activity data of the app as well as the metadata of the songs and creates a Postgresql database, which then can be used for analysis, queries, etc.

## How to run the code
Requirements for this ETL pipeline are the installation of Python(3) and Postgresql.
The data files in JSON format should be copied to the /data/log_data and /data/song_data folders, respectively
In the next step the file create_tables.py (call python3 create_tables.py) creates the tables in the postgresql database.
The process of conversion from JSON file to the Postgresql database is started with:
python3 etl.py

## Description of the code files
create_tables.py    Creates all the required postgresql tables in the database    
etl.ipynb           Shows the flow of the ETL Pipeline based on 1 dataset. Can be used for debugging/extension of functions
etl.py              Automated ETL flow where all functions are included for the whole dataset
README.md           This file
sql_queries.py      All required query calls in postgresql (will be imported to the etl files)       
test.ipynb          Test file to verify the functionality of the pipeline/database

## DB schema / ETL pipeline
The DB schema is a "Star schema":

_Fact Table_
    songplays - records in log data associated with song plays i.e. records with page NextSong
        songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent

_Dimension Tables_
    users - users in the app
        user_id, first_name, last_name, gender, level
    songs - songs in music database
        song_id, title, artist_id, year, duration
    artists - artists in music database
        artist_id, name, location, latitude, longitude
    time - timestamps of records in songplays broken down into specific units
        start_time, hour, day, week, month, year, weekday

All the items are automatically extracted from the JSON files and added to the database according to above scheme.






