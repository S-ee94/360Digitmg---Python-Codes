# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



# -*- coding: utf-8 -*-
"""Connect to SQL.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1l3oFqsqDtb1JnthzOJ0y15qT4eZ66_zL
"""

# pip install pypyodbc - use this in collab

import pypyodbc as odbc

DRIVER_NAME = 'PostgreSQL35W'
SERVER_NAME = 'PostgreSQL 15'
DATABASE_NAME= 'ClassTraining'

connection_string = f"""
    DRIVER = {DRIVER_NAME};
    SERVER = {SERVER_NAME};
    DATABASE = {DATABASE_NAME};
    Trust_Connection=yes;

"""

conn = odbc.connect(connection_string)
print(conn)

# pip install pyodbc

# Import libraries
import pandas as pd
import sys
import pyodbc
from sqlalchemy import create_engine, MetaData, Table, select, engine

print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)

# Parameters
TableName = "courses"

DB = {
    'drivername': 'mssql+pyodbc',
    'servername': 'PostgreSQL 15',
    #'port': '5432',
    #'username': 'lynn',
    #'password': '',
    'database': 'ClassTraining',
    'driver'}