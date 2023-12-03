import threading
import time
import mysql.connector
import random
import uuid
import faker
import config

fake = faker.Faker()
tablenames = [
    "Nice",
    "Corona Vacacine",
    "Acetaminophen",
    "Adderall",
    "Amlodipine",
    "Ativan",
]


def insert():
    start = time.time()
    conn = mysql.connector.connect(
        host=config.host,
        username=config.username,
        password=config.password,
        database=config.database,
    )
    for i in range(1001000, 1010000):
        try:
            my_cursor = conn.cursor()
            my_cursor.execute(
                "insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    random.choice(tablenames),  # self.Nameoftablets.get(),
                    str(uuid.uuid4()),  # self.ref.get(),
                    str(fake.text())[:40],  # self.Dose.get(),
                    random.choice(range(6)),  # self.NumberofTablets.get(),
                    str(fake.text())[:40],  # self.Lot.get(),
                    fake.date(),  # self.Issuedate.get(),
                    fake.date(),  # self.ExpDate.get(),
                    str(fake.text())[:40],  # self.DailyDose.get(),
                    str(fake.text())[:40],  # self.StorageAdvice.get(),
                    fake.phone_number(),  # self.nhsNumber.get(),
                    fake.name(),  # self.Patientname.get(),
                    fake.date_of_birth(),  # self.DateOfBirth.get(),
                    str(fake.address()),  # self.PatientAddress.get()
                    i,
                ),
            )
            conn.commit()
            if i % 1000 == 0:
                print("Inserted ", i, " records")
                end = time.time()
                print("Time taken is: ", end - start)
        except Exception as e:
            print(e)
    end = time.time()
    print("Time taken to insert 1 million records is: ", end - start)


def select():
    start = time.time()
    conn = mysql.connector.connect(
        host=config.host,
        username=config.username,
        password=config.password,
        database=config.database,
    )
    for i in range(100000):
        try:
            my_cursor = conn.cursor()
            my_cursor.execute("select * from hospital where id=%s", (i,))
            myresult = my_cursor.fetchall()
            print("Selected ", i, " records")
            end = time.time()
            print("Time taken is: ", end - start)
        except Exception as e:
            print(e)
    end = time.time()
    print("Time taken to select 1 million records is: ", end - start)


def update():
    start = time.time()
    conn = mysql.connector.connect(
        host=config.host,
        username=config.username,
        password=config.password,
        database=config.database,
    )
    for i in range(100000):
        try:
            my_cursor = conn.cursor()
            my_cursor.execute(
                "update hospital set Nameoftablets=%s, dose=%s, Numbersoftablets=%s, lot=%s, issuedate=%s, expdate=%s, dailydose=%s, storage=%s, nhsnumber=%s, patientname=%s, DOB=%s, patientaddress=%s where id=%s",
                (
                    random.choice(tablenames),  # self.Nameoftablets.get(),
                    str(fake.text())[:40],  # self.Dose.get(),
                    random.choice(range(6)),  # self.NumberofTablets.get(),
                    str(fake.text())[:40],  # self.Lot.get(),
                    fake.date(),  # self.Issuedate.get(),
                    fake.date(),  # self.ExpDate.get(),
                    str(fake.text())[:40],  # self.DailyDose.get(),
                    str(fake.text())[:40],  # self.StorageAdvice.get(),
                    fake.phone_number(),  # self.nhsNumber.get(),
                    fake.name(),  # self.Patientname.get(),
                    fake.date_of_birth(),  # self.DateOfBirth.get(),
                    str(fake.address()),  # self.PatientAddress.get()
                    i,
                ),
            )
            conn.commit()
            print("Updated ", i, " records")
            end = time.time()
            print("Time taken is: ", end - start)
        except Exception as e:
            print(e)
    end = time.time()
    print("Time taken to update 1 million records is: ", end - start)


# Tạo hai đối tượng Thread
user1 = threading.Thread(target=insert)
user2 = threading.Thread(target=select)
user3 = threading.Thread(target=update)
user4 = threading.Thread(target=select)
user5 = threading.Thread(target=insert)
user6 = threading.Thread(target=update)
user7 = threading.Thread(target=insert)
user8 = threading.Thread(target=select)
user9 = threading.Thread(target=update)
# Bắt đầu thực hiện các Thread
user1.start()
user2.start()
user3.start()
user4.start()
user5.start()
user6.start()
user7.start()
user8.start()
user9.start()

# Chờ cho tất cả các thread hoàn thành
user1.join()
user2.join()
user3.join()
user4.join()
user5.join()
user6.join()
user7.join()
user8.join()
user9.join()

print("Kết thúc chương trình")
