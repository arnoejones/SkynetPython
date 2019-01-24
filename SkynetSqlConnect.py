import pandas.io.sql as psql
from sqlalchemy import create_engine

#Skynet production db
def getData():
    ServerName = 'rnop-ctpa02'
    Database = 'FTA'
    Driver = "driver=SQL Server Native Client 11.0"

    engine = create_engine('mssql+pyodbc://' + ServerName + '/' + Database + "?" + Driver)
    # sql = "SELECT GameName AS 'Games Tested', " \
    #       "COUNT(GameName) AS 'Games Tested Amount' " \
    #       "FROM GameLogs WHERE GameName <> '' " \
    #       "GROUP BY GameName " \
    #       "ORDER BY '# of Games Tested' " \
    #       "DESC"
    sql = "SELECT COUNT(GameName) AS 'Game Name Count', GameName AS 'Game Name', Denom AS 'Denom', Bet AS 'Bet', AI AS 'AI' " \
          "FROM GameLogs " \
          "WHERE GameName != '' " \
          "GROUP BY Bet, GameName, AI, Denom " \
          "ORDER BY GameName " \
          "ASC"
    df = psql.read_sql(sql, engine)
    return df

df2 = getData()
print(df2)
