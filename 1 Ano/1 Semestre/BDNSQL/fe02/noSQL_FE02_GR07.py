# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 18:05:26 2020

@author: anamr
"""

import requests
import cx_Oracle

try:
    cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\anamr\Downloads\instantclient_12_2")
    conn = cx_Oracle.connect("uminho", "uminho2020", "localhost:1521/orclpdb1.localdomain", encoding="UTF-8")
except Exception as err:
    print('Error while creating the connection ', err)
else:
    print(conn.version)
    try:
        cur = conn.cursor()
        
        sensors_api = 'http://nosql.hpeixoto.me/api/sensor/300'
        for i in range(1,6):
            url = sensors_api + str(i)    
            data = requests.get(url).json()
            
            sql_patient = "INSERT INTO PATIENT VALUES (%d, '%s', TO_DATE('%s','yyyy-mm-dd'), %d)" % (data['patient']['patientid'], data['patient']['patientname'], data['patient']['patientbirthdate'], data['patient']['patientage'])
            cur.execute(sql_patient)
            
            sql_sensor = "INSERT INTO SENSOR VALUES (%d, %d, '%s', %d)" % (data['sensorid'], data['sensornum'], data['type_of_sensor'], data['number_of_sensors'])
            cur.execute(sql_sensor)

            sql_service = "INSERT INTO SERVICE(CODE, NAME) VALUES ('%s', '%s')" % (data['servicecod'], data['servicedesc'])
            cur.execute(sql_service)
            cur.execute("SELECT MAX(SERVICEID) FROM SERVICE")
            serviceid = cur.fetchone()[0]

            sql_bloodpress = "INSERT INTO BLOODPRESS(BLOODPRESSSYS, BLOODPRESSDIS) VALUES (%d, %d)" % (data['bloodpress']['systolic'], data['bloodpress']['diastolic'])
            cur.execute(sql_bloodpress)
            cur.execute("SELECT MAX(BLOODPRESSID) FROM BLOODPRESS")
            bloodpressid = cur.fetchone()[0]

            sql_patientdetails = "INSERT INTO PATIENTDETAILS(ADMDATE, BED, TIMESTAMP, PATIENTID) VALUES (TO_DATE('%s','yyyy-mm-dd'), '%s', TO_TIMESTAMP('%s','yyyy-mm-dd hh24:mi:ss'), %d)" % (data['admdate'], data['bed'], data['timestamp'], data['patient']['patientid'])
            cur.execute(sql_patientdetails)

            sql_team = "INSERT INTO TEAM(NAME) VALUES ('%s')" % ('')
            cur.execute(sql_team)
            cur.execute("SELECT MAX(TEAMID) FROM TEAM")
            teamid = cur.fetchone()[0]

            sql_measurements = "INSERT INTO MEASUREMENTS(BODYTEMP, BLOODPRESSID, BPM, SATO2, PATIENTID, SENSORID, SERVICEID, TEAMID) VALUES (%d, %d, %d, %d, %d, %d, %d, %d)" % (data['bodytemp'], bloodpressid, data['bpm'], data['sato2'], data['patient']['patientid'], data['sensorid'], serviceid, teamid)
            cur.execute(sql_measurements)

            for j in range(0,3):
                cur.execute("SELECT COUNT(DOCTORID) FROM DOCTOR")
                doclen = cur.fetchone()[0]
                cur.execute("SELECT COUNT(DOCTORID) FROM DOCTOR WHERE DOCTORID!=%d" % data['careteam'][j]['id'])
                doc = cur.fetchone()[0]

                if doclen == doc:
                    sql_doctor = "INSERT INTO DOCTOR VALUES (%d, '%s')" % (data['careteam'][j]['id'], data['careteam'][j]['nome'])
                    cur.execute(sql_doctor)

                cur.execute("SELECT COUNT(DOCTORID) FROM CARETEAM")
                ctlen = cur.fetchone()[0]
                cur.execute("SELECT COUNT(DOCTORID) FROM CARETEAM WHERE DOCTORID!=%d AND TEAMID!=%d" % (data['careteam'][j]['id'], teamid))
                ct = cur.fetchone()[0]

                if ctlen == ct:
                    sql_careteam = "INSERT INTO CARETEAM VALUES (%d, %d)" % (data['careteam'][j]['id'], teamid)
                    cur.execute(sql_careteam)
            
    except Exception as err:
        print('Error while inserting the data ', err)
    else:
        print('Insert completed')
finally:
    conn.commit()
    cur.close()
    conn.close()











    

    
