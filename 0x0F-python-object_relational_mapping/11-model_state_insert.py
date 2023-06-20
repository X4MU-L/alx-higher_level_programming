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

        state = State(name="Louisiana")
        session.add(state)
        session.commit()
        print(state.id)
        session.close()
    except Exception as e:
        if type(e) == IndexError:
            print(f"USAGE: {argv[0]} user passwd database state_name")
        else:
            print(e)
        exit(1)
