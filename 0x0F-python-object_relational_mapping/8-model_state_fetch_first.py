#!/usr/bin/python3

'''prints the first State'''

if __name__ == '__main__':
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sqlalchemy import create_engine
    import sys

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).limit(1).all()
    print(f"{first_state[0].id}: {first_state[0].name}")
    session.commit()
