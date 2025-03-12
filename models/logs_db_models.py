from peewee import Model, SqliteDatabase, CharField, UUIDField, DateTimeField, ForeignKeyField
import uuid
import os   
    

db_path = 'databases/logs.db'
os.makedirs(os.path.dirname(db_path), exist_ok=True)

db2 = SqliteDatabase(db_path)


class BaseModel(Model):
    class Meta:
        database = db2


class SpaceType(BaseModel):
    # global, log, post
    type = CharField(default="unknown")


class EventType(BaseModel):
    # login, comment, create_post, delete_post, logout
    type = CharField(default='unknown')


class Logs(BaseModel):
    id = UUIDField(primary_key=True, default=uuid.uuid4())
    datetime = DateTimeField()
    user_login = CharField()
    space_type_id = ForeignKeyField(SpaceType)
    event_type_id = ForeignKeyField(EventType)    
    info_about_post = CharField(null=True)


db2.connect()
db2.create_tables([SpaceType, EventType, Logs])
