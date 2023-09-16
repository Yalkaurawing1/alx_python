"""Write a script that lists all State
objects that contain the letter a from
the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    from model_state import State, Base
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    import sys

    path = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3])
    engine = create_engine(path)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()
    for state in states:
        if 'a' in state.name:
            print("{}: {}".format(state.id, state.name))

    session.close()
