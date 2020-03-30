#!/usr/bin/python3
""" List 1st state"""

from sys import argv
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(
                               argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    new_st = State(name="California")
    session.add(new_st)
    session.commit()
    new_city = City(name="San Francisco", state_id=new_st.id)
    session.add(new_city)
    session.commit()
    session.close()
