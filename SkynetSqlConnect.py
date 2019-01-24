import pyodbc
from pandas import DataFrame
import pandas as pd
import pandas.io.sql as psql
from sqlalchemy import create_engine

#Skynet production db
def getData():
    ServerName = 'rnop-ctpa02'
    Database = 'FTA'
    Trusted_Connection = 'yes'
    Driver = "driver=SQL Server Native Client 11.0"

    engine = create_engine('mssql+pyodbc://' + ServerName + '/' + Database + "?" + Driver)
    sql =  "select distinct IP from GameLogs"
    df = psql.read_sql(sql, engine)
    return df

df2 = getData()
print(df2)
