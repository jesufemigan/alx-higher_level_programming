#!/usr/bin/python3

'''lists all cities'''

if __name__ == "__main__":
    import sys
    from relationship_city import City
    from relationship_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    states = session.query(State).order_by(State.id)

    for state in states:
        for city in state.cities:
            print(f"{city.id}: {city.name} -> {state.name}")
