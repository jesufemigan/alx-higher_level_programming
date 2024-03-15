#!/usr/bin/python3

'''adds a new object to the database'''

if __name__ == '__main__':
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State
    import sys

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()
    new_state = State()
    new_state.name = "Louisiana"
    session.add(new_state)
    print(session.query(State).filter(State.name.like("Louisiana")).first().id)
    session.commit()
