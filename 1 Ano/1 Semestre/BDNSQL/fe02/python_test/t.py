import cx_Oracle

try:
    cx_Oracle.init_oracle_client(lib_dir=r"/Applications/instantclient_19_8")
    connection = cx_Oracle.connect("uminho", "uminho2020", "localhost:1521/orclpdb1.localdomain", encoding="UTF-8")
    print(connection.version)
except Exception as err:
    print('Error while creating the connection ', err)









    

    
