#!/usr/bin/python3

'''deletes all states object with a name containing letter a'''

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys
    from model_state import State, Base

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    session.query(State).filter(State.name.contains('a')).delete()
    session.commit()
