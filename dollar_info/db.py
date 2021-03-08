from re import L
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dollar_info.models import Base, Entry
from datetime import datetime


class DbConnection():
    """DbConnection - Creates a connection to the underlying database.
    """
    def __init__(self):
        self.engine = None
        self.session = None
        self.init()
        self.create_schema()
        self.start_session()

    def init(self):
        """init - initializes the engine.
        """
        self.engine = create_engine('sqlite:///db.sqlite', echo=True)

    def create_schema(self):
        """create_schema - creates the primary schema if not created.
        """
        Base.metadata.create_all(self.engine)

    def start_session(self):
        """start_session - starts the session to do operations with the database.
        """
        Sess = sessionmaker()
        Sess.configure(bind=self.engine)
        self.session = Sess()

    def save(self, entity):
        self.session.add(entity)
        self.session.commit()

    def sample_data(self):
        """sample_data - creates sample data for the database.
        """
        entry = Entry(date=datetime.now(), sell_price=19.0, buy_price=19.0)
        self.session.add(entry)
        self.session.commit()


class Repository():
    def __init__(self, db, model):
        self.db = db
        self.model = model
    
    def save(self, entity):
        self.db.session.add(entity)
        self.db.session.commit()

    def get(self, id):
        return self.db.session.query(self.model).filter(self.model.id == id).first()

    def get_all(self):
        return self.db.session.query(self.model)

    def filter(self, *args):
        return self.db.session.query(self.model).filter(*args)

    def remove(self, entity):
        self.db.session.delete(entity)
        self.db.session.commit()

    def update(self, entity):
        self.db.session.commit()


class EntryRepository(Repository):
    def __init__(self, db):
        super().__init__(db, Entry)


class UnitOfWork():
    def __init__(self):
        self.db = DbConnection()
        self.entries = EntryRepository(self.db)