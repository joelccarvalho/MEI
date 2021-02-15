import cx_Oracle
import json
from sshtunnel import SSHTunnelForwarder
import pymongo
import sys


# variables         
MONGO_HOST = ('localhost', 2222)
MONGO_USER = "root"
MONGO_PASS = "uminho!2020"
MONGO_DB = "HR"
MONGO_COLLECTION1 = "employees"
MONGO_COLLECTION2 = "departments"

# define ssh tunnel
server = SSHTunnelForwarder(
    MONGO_HOST,
    ssh_username = MONGO_USER,
    ssh_password = MONGO_PASS,
    remote_bind_address = ('127.0.0.1', 27017)
)

employees = '''select 
            JSON_OBJECT (
                'employee_id' VALUE e.employee_id, 
                'first_name' VALUE e.first_name,
                'last_name' VALUE e.last_name,
                'email' VALUE e.email, 
                'phone_number' VALUE e.phone_number,
                'hire_date' VALUE e.hire_date,
                'salary' VALUE e.salary,
                'commission_pct' VALUE e.commission_pct,
                'manager_id' VALUE e.manager_id,
                'job' VALUE ( 
                    SELECT JSON_OBJECT(
                        'job_id' VALUE j.job_id,
                        'job_title' VALUE j.job_title,
                        'min_salary' VALUE j.min_salary,
                        'max_salary' VALUE j.max_salary
                        )
                    
                    from jobs j
                    where j.job_id = e.job_id
                ),
                'job_history' VALUE ( 
                    SELECT JSON_ARRAYAGG(
                        JSON_OBJECT(
                        'start_date' VALUE jh.start_date,
                        'end_date' VALUE jh.end_date,
                        'department_id' VALUE jh.department_id,
                        'jobs' VALUE ( 
                                SELECT JSON_OBJECT(
                                    'job_id' VALUE j.job_id,
                                    'job_title' VALUE j.job_title,
                                    'min_salary' VALUE j.min_salary,
                                    'max_salary' VALUE j.max_salary
                                    )
                                
                                from jobs j
                                where j.job_id = jh.job_id
                            ) 
                        )
                    )
                    from job_history jh
                    where jh.employee_id = e.employee_id
                ),
                'department_id' VALUE e.department_id
            )
            from employees e'''

departments = '''select 
            JSON_OBJECT (
                'department_id' VALUE d.department_id,
                'department_name' VALUE d.department_name,
                'manager_id' VALUE d.manager_id,
                'location' VALUE (
                    SELECT 
                        JSON_OBJECT(
                        'location_id' VALUE l.location_id,
                        'street_adresss' VALUE l.street_address,
                        'postal_code' VALUE l.postal_code,
                        'city' VALUE l.city,
                        'state_province' VALUE l.state_province,
                        'country' VALUE ( 
                                SELECT JSON_OBJECT(
                                    'country_id' VALUE c.country_id,
                                    'country_name' VALUE c.country_name,
                                    'region' VALUE ( 
                                            SELECT JSON_OBJECT(
                                                'region_id' VALUE r.region_id,
                                                'region_name' VALUE r.region_name
                                                )
                                            from regions r
                                            where r.region_id = c.region_id
                                        ) 
                                    )
                                from countries c
                                where c.country_id = l.country_id
                            ) 
                        )
                    
                    from locations l
                    where l.location_id = d.location_id
                )
            )
            from departments d'''





def oracle2Mongo(conn, collection, option, string):
    try:
        cur = conn.cursor()
        cur.execute(option)

        for row in cur:
            data = json.loads(row[0])
            collection.insert_one(data)
        
        print("Completed collection %s!" %(string))
        
    except Exception as err:
        error = "Error while inserting collection " + string + ": " + err
        print(error)
        sys.exit(1)
    finally:
        cur.close()


if __name__ == '__main__':

    try:
        # start ssh tunnel
        server.start()

        connection = pymongo.MongoClient('127.0.0.1', 27017)
        db = connection[MONGO_DB]
        collection1 = db[MONGO_COLLECTION1]
        collection2 = db[MONGO_COLLECTION2]

        try:
            cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\Bruno-Santos\Desktop\BDNSQL\BlackBoard\ficha2\instantclient_19_9")
            conn = cx_Oracle.connect("hr", "hr", "localhost:1521/orclpdb1.localdomain", encoding="UTF-8")

            oracle2Mongo(conn, collection1, employees, "employees")
            oracle2Mongo(conn, collection2, departments, "departments")


        except Exception as err:
            print('Error while connecting to OracleDB: ', err)
            sys.exit(2)
        finally:
            conn.close()
            sys.exit(0)
    except  Exception as err:
            print('Error while connecting to MongoDB: ', err)
            sys.exit(3)

