import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    '''
    Uploads the extracted data from the song file to the song table and to the artist table of the database.

            Parameters:
                    cur: cursor to the opened database 
                    filepath: filepath of the json song_file to be extracted

            Returns:
                    None, directly updates the postgresql database for song and artist data
    '''
    df = pd.read_json(filepath, lines=True)
    song_data = df[['song_id', 'title', 'artist_id', 'year', 'duration']].values
    song_data = song_data.tolist()[0]
    cur.execute(song_table_insert, song_data)
    
    artist_data = df[['artist_id', 'artist_name', 'artist_location', 'artist_latitude', 'artist_longitude']].values
    artist_data = artist_data.tolist()[0]
    cur.execute(artist_table_insert, artist_data)


def process_log_file(cur, filepath):
    '''
    Uploads the extracted data from the log file to the time table, user table and songplay table of the database.

            Parameters:
                    cur: cursor to the opened database 
                    filepath: filepath of the json log_file to be extracted

            Returns:
                    None, directly updates the postgresql database for time, user and songplay information
    '''

    df = pd.read_json(filepath, lines=True)
    df = df[df['page']=='NextSong']
    df['ts_datetime']=pd.to_datetime(df['ts'], unit='ms')
    df['timestamp'] = df['ts_datetime']
    df['hour'] = df['ts_datetime'].dt.hour
    df['day'] = df['ts_datetime'].dt.day
    df['week_of_year'] = df['ts_datetime'].dt.isocalendar().week
    df['month'] = df['ts_datetime'].dt.month
    df['year'] = df['ts_datetime'].dt.year
    df['weekday'] = df['ts_datetime'].dt.weekday
    time_df = df[['timestamp', 'hour', 'day', 'week_of_year', 'month', 'year', 'weekday']]

    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))
    user_df = df[['userId', 'firstName','lastName', 'gender', 'level']]

    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

    for index, row in df.iterrows():
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None
        songplay_data = [row.timestamp, row.userId, row.level, songid, artistid, row.sessionId, row.location, row.userAgent]
        cur.execute(songplay_table_insert, songplay_data)


def process_data(cur, conn, filepath, func):
    '''
    Iterates over the files and calls each function for the data extraction for log files and song files

            Parameters:
                    conn: connection to the postgresql database
                    cur: cursor to the opened database 
                    filepath: filepath of the json log_files to be extracted
                    func: function to be called for extraction of data (process_song_file, process_log_file)

            Returns:
                    None
    '''
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))
    num_files = len(all_files)
    print('{} files found in {}'.format(num_files, filepath))
    for i, datafile in enumerate(all_files, 1):
        func(cur, datafile)
        conn.commit()
        print('{}/{} files processed.'.format(i, num_files))


def main():
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()

    process_data(cur, conn, filepath='data/song_data', func=process_song_file)
    process_data(cur, conn, filepath='data/log_data', func=process_log_file)

    conn.close()


if __name__ == "__main__":
    main()