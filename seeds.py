from app.models import User, Post
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
    User(username='DempCSees', email='illusionsOfGrandjeur@bootcamp.com', password='myHusbandHatesMe411'),
    User(username='notValidnametest', email='jimmyjohns@jimmy.com', password='allgf'),
])

db.commit()

# we need to run the posts after the users are created because the Post model requires valid user_id fields

db.add_all([
    Post(title='Algorithm sites', post_url='https://www.udemy.com/course/js-algorithms-and-data-structures-masterclass/', user_id=1),
    Post(title='Tech Jobs!', post_url='https://app.otta.com/', user_id=1),
    Post(title='more tech jobs!', post_url='https://angel.co/jobs', user_id=1),
    Post(title='Algoexpert', post_url='https://www.algoexpert.io/product?r=ads', user_id=2),
    Post(title='HackerRank', post_url='https://www.hackerrank.com/dashboard', user_id=3)
])

db.commit()

db.close()