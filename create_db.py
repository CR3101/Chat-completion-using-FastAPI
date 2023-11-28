from database import Base,engine
import database

Base.metadata.create_all(engine)