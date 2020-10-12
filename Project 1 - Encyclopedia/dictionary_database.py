import mysql.connector

# We need to establish a connector so we use a variable to store that connection object
con = mysql.connector.connect(
    user = 'ardit700_student',
    password = 'ardit700_student',
    host = '108.167.140.122',
    database = 'ardit700_pm1database'
)

#Next we need a cursor object that is used to navigate through the tables in the database
cursor = con.cursor()

word = input('Enter a word: ')
query_statement = 'SELECT * FROM Dictionary WHERE Expression = "{s}"'.format(s=word)

query = cursor.execute(query_statement)
results = cursor.fetchall() #We need to get the actual data queried by using fetch

# Empty lists return FALSE
if results:
    for result in results:
        print(result[1])
else:
    print('No word found!')