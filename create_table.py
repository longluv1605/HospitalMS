import mysql.connector
import config

conn = mysql.connector.connect(
    host=config.host,
    username=config.username,
    password=config.password,
    database=config.database,
)

try:
    my_cursor = conn.cursor()
    my_cursor.execute(
        """CREATE TABLE hospital (
            Nameoftablets varchar(45) NOT NULL,
            Reference_No varchar(255) NOT NULL,
            dose varchar(45) NOT NULL,
            Numbersoftablets varchar(45) DEFAULT NULL,
            lot varchar(45) DEFAULT NULL,
            issuedate date DEFAULT NULL,
            expdate date DEFAULT NULL,
            dailydose varchar(45) DEFAULT NULL,
            storage varchar(45) DEFAULT NULL,
            nhsnumber varchar(45) DEFAULT NULL,
            patientname varchar(45) DEFAULT NULL,
            DOB date DEFAULT NULL,
            patientaddress varchar(255) DEFAULT NULL,
            id varchar(45) NOT NULL,
            PRIMARY KEY (Reference_No,id)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci"""
    )
    conn.commit()
    conn.close()
except Exception as e:
    print(e)
