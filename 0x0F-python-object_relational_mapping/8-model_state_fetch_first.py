#!/usr/bin/python3
"""query a database using sqlalchemy get the first state"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


if __name__ == "__main__":
    try:
        engine = create_engine(
            f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}"
        )
        Session = sessionmaker(bind=engine)
        session = Session()

        state = session.query(State).order_by(State.id).first()
        if (state):
            print(f"{state.id}: {state.name}")
        else:
            print("Nothing")
        session.close()
    except Exception as e:
        if type(e) == IndexError:
            print(f"USAGE: {argv[0]} user passwd database state_name")
        else:
            print(e)
        exit(1)
