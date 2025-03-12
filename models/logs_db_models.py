from peewee import Model, SqliteDatabase, CharField, UUIDField, DateTimeField, ForeignKeyField
import uuid
if __name__ == "__main__": # ДА, ЭТО ОТСТОЙ
    from author_db_models import Post
else:
    from models.author_db_models import Post

db2 = SqliteDatabase('databases/logs.db')


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
    id = UUIDField(primary_key=True)
    datetime = DateTimeField()
    user_login = CharField()
    space_type_id = ForeignKeyField(SpaceType)
    event_type_id = ForeignKeyField(EventType)    
    info_about_post = CharField(null=True)


db2.connect()
db2.create_tables([SpaceType, EventType, Logs])
