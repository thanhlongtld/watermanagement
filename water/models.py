import mongoengine as db


class Client(db.Document):
    clientCode = db.StringField()
    name = db.StringField()
    email = db.StringField()
    phone = db.StringField()
    nationalID = db.StringField()


class Usage(db.Document):
    month = db.IntField()
    year = db.IntField()
    totalCBM = db.IntField()
    useCBM = db.IntField()
    client = db.ReferenceField(Client)


class User(db.Document):
    name = db.StringField()
    username = db.StringField()
    password = db.StringField()


class Payment(db.Document):
    provider = db.StringField()
    type = db.StringField()
    message = db.StringField()
    note = db.StringField()
    payDate = db.DateTimeField()


class Bill(db.Document):
    totalPrice = db.FloatField()
    status = db.StringField()
    usage = db.ReferenceField(Usage)
    payment = db.ReferenceField(Payment)
    createdAt = db.DateTimeField()


class Type(db.Document):
    name = db.StringField()


class Location(db.Document):
    address = db.StringField()
    type = db.ReferenceField(Type)
    client = db.ReferenceField(Client)


class Level(db.Document):
    name = db.StringField()
    min = db.IntField()
    max = db.IntField()


class PriceLevel(db.Document):
    clientType = db.ReferenceField(Type)
    level = db.ReferenceField(Level)
    price = db.FloatField()


# class Email(db.Document):
