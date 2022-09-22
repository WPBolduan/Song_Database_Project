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
create_tables.py        
etl.ipynb           



## DB schema / ETL pipeline

todo: add comment that decided to DOTHINING when the entry is updated on same id
add the comment to the feedback that it would be better to build song and artist db completely before the last step in etl.ipynb
the fact that I add the conversion of the timestamp to the dataframe allows to use the same format for the songplay table
commment giving func in function was new to me. very convenient

cur.execute(song_table_insert, song_data)
conn.commit()

why is conn.commit() missing in the etl.py file?





