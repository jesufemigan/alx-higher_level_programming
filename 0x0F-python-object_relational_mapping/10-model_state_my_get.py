#!/usr/bin/python3

'''prints the state obect with name passed as argument'''

if __name__ == '__main__':
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State
    import sys

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(bind=engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like(sys.argv[4])).all()

    if len(states) > 0:
        for state in states:
            print(state.id)
    else:
        print("Not found")

    session.commit()
