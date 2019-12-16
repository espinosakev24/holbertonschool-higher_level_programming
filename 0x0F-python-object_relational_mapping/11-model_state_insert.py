#!/usr/bin/python3
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    a1, a2, a3 = argv[1], argv[2], argv[3]
    a = 0
    engine = create_engine('mysql+mysqldb://{}:{}'
                           '@localhost/{}'
                           .format(a1, a2, a3, pool_pre_ping=True))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    s = Session()
    new = State(name="Louisiana")
    s.add(new)
    s.commit()
    instance = s.query(State).filter_by(name='Louisiana').first()
    print(instance.id)
    s.close()
