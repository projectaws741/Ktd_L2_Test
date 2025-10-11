import cx_Oracle
import numpy as np
import csv
from datetime import datetime
import time
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

PATH = '/app'
input_path = PATH + '/data/input'
output_path = PATH + '/data/output'

time_stamp = datetime.now().strftime('%Y%m%d')
output_file_name = time_stamp + '_' + 'testOutput.txt'

cx_Oracle.init_oracle_client(lib_dir='/opt/oracle/instantclient_21_3')

dsn = cx_Oracle.makedsn(
    host='oracle-db',
    port=1521,
    service_name='ORCLPDB1'
)
connection = cx_Oracle.connect(
    user=os.getenv('ORACLE_USER'),
    password=os.getenv('ORACLE_PASSWORD'),
    dsn=dsn
)

query = """ SELECT * FROM C_DUNS_V """

df_mda = pd.read_sql(query, con=connection)

df_mda.to_csv(output_path + '/' + output_file_name, sep="\t")

connection.close()
