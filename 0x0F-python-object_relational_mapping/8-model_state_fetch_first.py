#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    """
    lists all State objects from the database hbtn_0e_6_usa
    """
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

    # Query to retrieve the first State object based on states.id order
    first_state = session.query(State).order_by(State.id).first()

    # Display the result or print "Nothing" if the table is empty
    if first_state:
        print("{}: {}".format(first_state.id, first_state.name))
    else:
        print("Nothing")

    session.close()
