import os #importing operating system library

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgresql://postgres:2503@localhost:5432/lec03") #'engine' is an object created by sqlalchemy that is used to manage connections in databse.
db = scoped_session(sessionmaker(bind=engine)) #db is an obejct which separates different users performing operation in the database.

def main():
    flights = db.execute("SELECT origin, destination, duration FROM flights").fetchall()
    for flight in flights:
        print(f"{flight.origin} to {flight.destination} in {flight.duration} minutes.") 

if __name__ == "__main__":
    main()
