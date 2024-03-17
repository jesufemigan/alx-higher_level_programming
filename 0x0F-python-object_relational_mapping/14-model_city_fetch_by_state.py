#!/usr/bin/python3

'''a scripts that prints all city'''

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_city import City
    from model_state import Base, State
    import sys

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    cities = session.query(City, State).filter(City.state_id ==
                                               State.id).order_by(City.id)\
        .all()

    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")
