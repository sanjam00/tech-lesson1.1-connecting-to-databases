import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

cur = conn.cursor()
# We have created a connection object within our notebook and assigned it to conn
# A cursor object is what can actually execute SQL commands. You create it by calling .cursor() on the connection:cur = conn.cursor()

# Execute the query

# (This is a special query for finding the table names. You don't need to memorize it.)

# SQLite databases all have a sqlite_master table that stores the schema information

cur.execute("""SELECT name FROM sqlite_master WHERE type = 'table';""")

# Fetch the result and store it in table_names
table_names = cur.fetchall()
print(table_names)


# If we want to get all information about the offices table, we might do something like this (* means all columns):
offices = cur.execute("""SELECT * FROM offices""").fetchall()
# cur.fetchall()
print(offices)

# This data is useful, since it's a list of tuples rather than one giant string. 
# If you wanted to select the phone number for the first office, for example, that would just be [0] [2] tacked on to the end of the previous Python statement.

# Information about the column names can be retrieved from the cursor. 
# Since the most recent query was SELECT * FROM offices;, the cursor will contain information about the offices table:
offices_descr = cur.description
print(offices_descr)

# If we wanted to combine the previous two steps to make a dataframe with the right column names, that would look like this:
data_table = pd.DataFrame(
    data=cur.execute("""SELECT * FROM offices;""").fetchall(),
    columns=[x[0] for x in cur.description]
)
print(data_table)