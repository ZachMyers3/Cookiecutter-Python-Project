from sqlalchemy import (
    event,
    Table,
    create_engine,
    String,
    Integer,
    Column,
    DateTime,
    Float,
)
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base, DeferredReflection

Base = declarative_base(cls=DeferredReflection)


@event.listens_for(Table, "column_reflect")
def reflect_col(inspector, table, column_info):
    column_info["key"] = column_info["name"].replace(" ", "_")


def get_sqlalchemy_session(connection_string: str):
    print(f"{connection_string=}")
    if connection_string is None:
        print("Unable to get connection string, exiting")
        raise BaseException("Unable to get connection string, exiting")
    print("Establishing connection with SQL database")
    # get Base for sqlalch, this base automaps the database
    # create a connection to the sql database
    engine = create_engine(connection_string)
    # reflect the tables
    Base.prepare(engine)

    db_session = Session(engine)

    print("SQL connection established")
    return db_session

