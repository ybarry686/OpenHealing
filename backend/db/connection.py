from contextlib import contextmanager # context manager
from sqlalchemy import create_engine, event
from sqlalchemy.orm import declarative_base, sessionmaker
from backend.config import Config

engine = create_engine(f"sqlite:///{Config.DATABASE_PATH}")
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)

# foreign-keys block, runs every time a new db connection is opened
@event.listens_for(engine, "connect")
def _enable_foreign_keys(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


@contextmanager # turns function into something you can use with a with statement
def session_scope():
    '''
    with session_scope() as session:
        session.add(new_post) #example
    :return: None
    '''
    session = SessionLocal()
    try:
        yield session # hand control to user code
        session.commit()
    except Exception:
        session.rollback() # undo since error occurred
        raise # show error
    finally:
        session.close()