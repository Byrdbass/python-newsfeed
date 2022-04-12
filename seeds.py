from app.models import User, Post, Comment, Vote
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

# add the comments post here
db.add_all([
    Comment(comment_text='This is a Udemy course reccomended to me by Juan', user_id=1, post_id=1),
    Comment(comment_text='A website reccomended by Morgan', user_id=1, post_id=2),
    Comment(comment_text='Great for Start ups!', user_id=1, post_id=3),
    Comment(comment_text='this was a highly reccomended site from Leah', user_id=2, post_id=4),
    Comment(comment_text='this is a very common algo site', user_id=3, post_id=5)
])

db.commit()

db.add_all([
    Vote(user_id=1, post_id=2),
    Vote(user_id=1, post_id=4),
    Vote(user_id=2, post_id=4),
    Vote(user_id=3, post_id=4),
    Vote(user_id=4, post_id=2)
])

db.commit()

db.close()