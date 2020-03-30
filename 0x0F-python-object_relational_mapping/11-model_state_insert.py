#!/usr/bin/python3
""" List 1st state"""

from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(
                               argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    """ Select * from state where id=1 """
    new = State(name = "Louisiana")
    session.add(new)
    session.commit()
    print(new_state.id)
    session.close()
