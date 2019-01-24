import pypyodbc
#Skynet local test db
# connection = pypyodbc.connect('Driver={SQL Server};'
#                               'Server=USNVR-W1005006\SKYNETLOCAL;'
#                              'Database=FTA;'
#                              'Trusted_Connection=yes')

#Skynet production db
connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server=rnop-ctpa02;'
                              'Database=FTA;'
                              'Trusted_Connection=yes')
cursor = connection.cursor()

'''
results = the entire result set from the query
'''
results = cursor.execute("select distinct IP from GameLogs Order by IP")

for result in results:
    print(result)

results = cursor.execute("select distinct DateOfTest from GameLogs order by DateOfTest")
for result in results:
    print(result)

connection.close()
