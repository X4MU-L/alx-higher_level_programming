#!/usr/bin/python3
"""query a database using sqlalchemy print all state and cities"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    try:
        engine = create_engine(
            f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}",
            pool_pre_ping=True
        )
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()

        for states, cities in session.query(State, City).filter(
                State.id == City.state_id).order_by(City.id).all():
            print(f"{states.name}: ({cities.id}) {cities.name}")

        session.close()
    except Exception as e:
        if type(e) == IndexError:
            print(f"USAGE: {argv[0]} user passwd database")
        else:
            print(e)
        exit(1)
