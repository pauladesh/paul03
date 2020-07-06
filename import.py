import csv
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:2503@localhost:5432/lec03")
db = scoped_session(sessionmaker(bind=engine))

def main():
    f = open("flights.csv") # opening flights.csv file and calling it "f".
    reader = csv.reader(f) # csv is python's built-in module
    for origin, destination, duration in reader:
        db.execute("INSERT INTO flights (origin, destination, duration) VALUES (:origin, :destination, :duration)",#:origin type is the place holder for origin.
                    {"origin": origin, "destination": destination, "duration": duration}) #python dictionary is provided to fill in the placeholders.
        print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
    db.commit()

if __name__ == "__main__":
    main()
