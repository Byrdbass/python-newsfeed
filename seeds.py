from app.models import User
from app.db import Session, Base, engine

#drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

#insert all these users when running the seed file
db.add_all([
    User(username='billyBob', email='billyBob@gmail.com', password='BillysWilly'),
    User(username='jimmyJon', email='jimmyJon@sandwhich.com', password='factoryFood123'),
    User(username='FrankyGuy', email='frank@hotdog.com', password='kosherdills321'),
    User(username='MarthaDempsey', email='imanidiot@dumass.com', password='iBribeClassmates'),
    User(username='DempCSees', email='illusionsOfGrandjeur@bootcamp.com', password='myHusbandHatesMe411')
])

db.commit()

db.close()