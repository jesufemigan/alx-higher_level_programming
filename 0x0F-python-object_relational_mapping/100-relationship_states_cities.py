#!/usr/bin/python3

'''creates state California with the city San Franciso'''

if __name__ == "__main__":
    from relationship_state import State, Base
    from relationship_city import City
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    import sys

    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    state1 = State(name='California')
    city = City(name='San Francisco')
    state1.cities.append(city)

    session.add_(state_1)
    session.add(city)
    session.commit()
