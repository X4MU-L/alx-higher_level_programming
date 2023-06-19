#!/usr/bin/python3
"""query a database using sqlalchemy
   get all state names count passed to command
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == "__main__":
    try:
        engine = create_engine(
            f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}",
            pool_pre_ping=True
        )
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        state_name = argv[4]
        state = session.query(
                State).filter(
                    State.name == (state_name)).order_by(State.id).first()
        if state:
            print(f"{state.id}")
        else:
            print("Not found")
        session.close()
    except Exception as e:
        if type(e) == IndexError:
            print(f"USAGE: {argv[0]} user passwd database state_name")
        else:
            print(e)
        exit(1)
