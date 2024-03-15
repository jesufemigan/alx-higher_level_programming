#!/usr/bin/python3

'''changes the name of state object'''

if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State
    import sys

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    session.query(State).filter(State.id == 2).update({'name': 'New Mexico'})

    session.commit()
