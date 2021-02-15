from sshtunnel import SSHTunnelForwarder
import pymongo
import requests

# variables
MONGO_HOST = ('localhost', 2222)
MONGO_USER = "root"
MONGO_PASS = "uminho!2020"
MONGO_DB = "FE02_bd"
MONGO_COLLECTION = "FE02_col"

# define ssh tunnel
server = SSHTunnelForwarder(
    MONGO_HOST,
    ssh_username = MONGO_USER,
    ssh_password = MONGO_PASS,
    remote_bind_address = ('127.0.0.1', 27017)
)

try:
    # start ssh tunnel
    server.start()

    connection = pymongo.MongoClient('127.0.0.1', 27017)
    db = connection[MONGO_DB]
    collection = db[MONGO_COLLECTION]

    try:
        # request data
        cardiac_sensors_api = 'http://nosql.hpeixoto.me/api/sensor/300'
        blood_sensors_api = 'http://nosql.hpeixoto.me/api/sensor/400'

        # Insert cardiac data
        for i in range(1,6):
            url = cardiac_sensors_api + str(i)    
            data = requests.get(url).json()
        
            # insert data
            result = collection.insert_one(data)

            print ('Cardiac sensor inserted! ID: ', result.inserted_id)

        # Insert blood data
        for i in range(1,6):
            url = blood_sensors_api + str(i)    
            data = requests.get(url).json()
        
            # insert data
            result = collection.insert_one(data)

            print ('Blood sensor inserted! ID: ', result.inserted_id)

    except Exception as err:
        print('Error while inserting the data ', err)
    finally:
        # stop ssh tunnel
        server.stop()
except Exception as err:
    print('Error while connecting to mongodb ', err) 