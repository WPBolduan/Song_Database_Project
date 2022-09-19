# DROP TABLES

songplay_table_drop = "DROP table if exists songplays"
user_table_drop = "Drop table if exists users"
song_table_drop = "Drop table if exists songs"
artist_table_drop = "Drop table if exists artists"
time_table_drop = "Drop table if exists time"

# CREATE TABLES

songplay_table_create = "CREATE TABLE IF NOT EXISTS songplays \
    (songplay_id varchar PRIMARY KEY, start_time varchar, user_id varchar, \
    level varchar, song_id varchar, artist_id varchar, session_id varchar, user_agent varchar);" 

user_table_create = "CREATE TABLE IF NOT EXISTS users \
    (user_id varchar PRIMARY KEY, first_name varchar, last_name varchar, \
    gender varchar, level varchar);"

song_table_create = "CREATE TABLE IF NOT EXISTS songs \
    (song_id varchar PRIMARY KEY, title varchar, artist_id varchar, year int, duration float);"

artist_table_create = "CREATE TABLE IF NOT EXISTS artists \
    (artist_id varchar PRIMARY KEY, name varchar, location varchar, \
    latitude varchar, longitude varchar);"

time_table_create = "CREATE TABLE IF NOT EXISTS time \
    (start_time varchar, hour varchar, \
    day varchar, week varchar, month varchar, year varchar, weekday varchar);"

# INSERT RECORDS 
songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = "INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s)"

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]