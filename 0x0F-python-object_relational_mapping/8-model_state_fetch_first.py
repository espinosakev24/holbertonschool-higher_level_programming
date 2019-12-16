#!/usr/bin/python3
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    a1, a2, a3 = argv[1], argv[2], argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}'
                           '@localhost/{}'
                           .format(a1, a2, a3, pool_pre_ping=True))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        print('{}: {}'.format(instance.id, instance.name))
        break
    session.close()
