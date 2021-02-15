# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 18:05:26 2021

@author: Bruno Santos
"""

import requests
import cx_Oracle  #modulo de python permite ligar à base de dados oracle 
import csv
import json
import sys

countries = '''SELECT country_id AS COUNTRY_ID, 
                      country_name AS COUNTRY_NAME, 
                      region_id AS REGION_ID
          FROM countries'''

regions = '''SELECT region_id AS REGION_ID,
                    region_name AS REGION_NAME
          FROM REGIONS''' 

departments = '''SELECT department_id AS DEPARTMENT_ID,
                        department_name AS DEPARTMENT_NAME,
                        manager_id AS MANAGER_ID,
                        location_id AS LOCATION_ID
          FROM departments''' 

#

employees = '''SELECT employee_id AS EMPLOYEE_ID,
                      first_name AS FIRST_NAME, 
                      last_name AS LAST_NAME, 
                      email AS EMAIL,
                      phone_number AS PHONE_NUMBER,
                      hire_date AS HIRE_DATE,
                      job_id AS JOB_ID,
                      salary AS SALARY,
                      commission_pct AS COMISSION_PCT,
                      manager_id AS MANAGER_ID,
                      department_id AS DEPARTMENT_ID
               FROM employees''' 

job_history = '''SELECT employee_id AS EMPLOYEE_ID,
                        start_date AS START_DATE,
                        end_date AS END_DATE,
                        job_id AS JOB_ID,
                        department_id AS DEPARTMENT_ID
          FROM job_history''' 

jobs = '''SELECT job_id AS JOB_ID,
                 job_title AS JOB_TITLE,
                 min_salary AS MIN_SALARY,
                 max_salary AS MAX_SALARY
          FROM jobs'''

locations = '''SELECT location_id AS LOCATION_ID,
                      street_address AS STREET_ADDRESS,
                      postal_code AS POSTAL_CODE,
                      city AS CITY,
                      state_province AS STATE_PROVINCE,
                      country_id AS COUNTRY_ID
          FROM locations''' 

locations = '''SELECT location_id AS LOCATION_ID,
                      street_address AS STREET_ADDRESS,
                      postal_code AS POSTAL_CODE,
                      city AS CITY,
                      state_province AS STATE_PROVINCE,
                      country_id AS COUNTRY_ID
          FROM locations''' 

departments_employees_jobs = '''  
                                SELECT *
                                FROM employees
                                INNER JOIN departments ON employees.department_id=departments.department_id
                                INNER JOIN jobs ON employees.job_id=jobs.job_id
                            '''

# join entre o job_history, department e jobs
# para tirar as informaçoes do job_history
job_history_departments_jobs = '''SELECT employee_id AS EMPLOYEE_ID,
                                         start_date AS START_DATE,
                                         end_date AS END_DATE,
                                         department_name AS DEPARTMENT_NAME,
                                         manager_id AS MANAGER_ID,
                                         job_title AS JOB_TITLE,
                                         min_salary AS MIN_SALARY,
                                         max_salary AS MAX_SALARY
                                FROM job_history
                                INNER JOIN departments  ON job_history.department_id=departments.department_id
                                INNER JOIN jobs ON job_history.job_id=jobs.job_id
                            ''' 

manager = '''SELECT DISTINCT manager_id AS MANAGER_ID
             FROM employees
             WHERE manager_id IS NOT NULL
             ''' 


def oracle2csv(query, table, conn):
           
        try:
            cursor = conn.cursor()
            
            cursor.execute(query)
            
            name = "C:/Users/Bruno-Santos/AppData/Local/Neo4j/Relate/Data/dbmss/dbms-0d045cb1-7d0a-46b0-a188-86b7a0841246/import/"+table+".csv"

            columns = [i[0] for i in cursor.description]
            rows = cursor.fetchall()
            # write oracle data to the csv file
            csv_file = open(name, mode='w')
            
            writer = csv.writer(csv_file, delimiter=',', lineterminator="\n", quoting=csv.QUOTE_NONNUMERIC)
            # write column headers to csv file
            
            writer.writerow(columns)
            
            for row in rows:
                writer.writerow(row)   ## write rows to csv file
            
            csv_file.close()
        except Exception as err:
            print('Error while fill the file ' + table + ' ', err)
        else:
            print('complete '+table+'.csv file')
        finally:
            cursor.close()


if __name__ == '__main__':
    try:
        cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\Bruno-Santos\Desktop\BDNSQL\ficha2\instantclient_19_9")
        conn = cx_Oracle.connect("hr", "hr", "localhost:1521/orclpdb1.localdomain", encoding="UTF-8")
        
        oracle2csv(countries,"countries", conn)
        oracle2csv(departments,"departments", conn)
        oracle2csv(employees,"employees", conn)
        oracle2csv(job_history,"job_history", conn)
        oracle2csv(jobs,"jobs", conn)
        oracle2csv(locations,"locations", conn)
        oracle2csv(regions,"regions", conn)
        oracle2csv(job_history_departments_jobs,"job_history_departments_jobs", conn)
        oracle2csv(manager,"manager", conn)

        
    
    except Exception as err:

        print('Error while creating the connection ', err)
        sys.exit(1)
    finally:
        conn.commit()
        conn.close()