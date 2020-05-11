from peewee import *
import datetime

db = SqliteDatabase('orm_practice.db')


class BaseModel(Model):
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


class Store(BaseModel):   
    name = CharField(unique=True)

'''This Store class has been inherited from the BaseModel class so once we apply query(db.create_tables([Store, Warehouse, Product])) in python interpreter ''
to create store table then we can see the BaseModel declared columns(created_at, updated_at columns) in store table as well '''
class Warehouse(BaseModel):
    store = ForeignKeyField(Store, backref='warehouses')
    location = TextField()


class Product(BaseModel):
    name = CharField()
    description = TextField()
    warehouse = ForeignKeyField(Warehouse, backref='products')
