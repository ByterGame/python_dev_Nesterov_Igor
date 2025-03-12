from peewee import SqliteDatabase, Model, CharField, TextField, ForeignKeyField, UUIDField
import uuid

db1 = SqliteDatabase('databases/authors.db')


class BaseModel(Model):
    class Meta:
        database = db1


class Author(BaseModel):
    id = UUIDField(primary_key=True)
    login = CharField(max_length=100, unique=True)
    email = CharField(max_length=100, unique=True)


class Blog(BaseModel):
    id = UUIDField(primary_key=True)
    owner = ForeignKeyField(Author, backref='blogs')
    name = CharField(max_length=200)
    description = TextField()


class Post(BaseModel):
    id = UUIDField(primary_key=True)
    header = CharField(max_length=200)
    text = TextField()
    author = ForeignKeyField(Author, backref='posts')
    blog = ForeignKeyField(Blog, backref='posts')


db1.connect()
db1.create_tables([Author, Blog, Post])
