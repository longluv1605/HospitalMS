import random
import time
import datetime
import uuid
import faker
import mysql.connector
import config


tablenames = [
    "Nice",
    "Corona Vacacine",
    "Acetaminophen",
    "Adderall",
    "Amlodipine",
    "Ativan",
]
fake = faker.Faker()


start = time.time()
conn = mysql.connector.connect(
    host=config.host,
    username=config.username,
    password=config.password,
    database=config.database,
)
for i in range(1000000):
    try:
        my_cursor = conn.cursor()
        my_cursor.execute(
            "insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
            (
                i,
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
            ),
        )
        conn.commit()
        conn.close()
        if i % 1000 == 0:
            print("Inserted ", i, " records")
            end = time.time()
            print("Time taken is: ", end - start)
    except Exception as e:
        continue

end = time.time()

print("Time taken to insert 1 million records is: ", end - start)
