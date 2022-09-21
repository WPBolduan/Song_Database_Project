todo: add comment that decided to DOTHINING when the entry is updated on same id
add the comment to the feedback that it would be better to build song and artist db completely before the last step in etl.ipynb
the fact that I add the conversion of the timestamp to the dataframe allows to use the same format for the songplay table
commment giving func in function was new to me. very convenient

cur.execute(song_table_insert, song_data)
conn.commit()

why is conn.commit() missing in the etl.py file?