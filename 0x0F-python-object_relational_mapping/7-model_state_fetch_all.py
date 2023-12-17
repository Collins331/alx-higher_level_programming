#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":

    from model_state import Base, State
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    """creates engine"""
    engine = create_engine(
    "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])
        )

    Session = sessionmaker(bind=engine)
    """start a session"""
    session = Session()

    states = session.query(State).order_by(State.id).all()
    """query data from the database"""
    for state in states:
    print("{}: {}".format(state.id, state.name))

    session.close()
