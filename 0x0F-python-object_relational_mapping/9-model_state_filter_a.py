#!/usr/bin/python3

'''prints all cities that contain letter 'a' '''

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

    states = session.query(State).filter(State.name.contains("a")).
    order_by(State.id)

    for state in states:
        print(f"{state.id}: {state.name}")

    session.commit()
