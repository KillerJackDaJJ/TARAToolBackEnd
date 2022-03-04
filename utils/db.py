from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(64), index=True)
    password = db.Column(db.String(64),  index=True)
    pub_key = db.Column(db.String(512), index=True, default='')
    imei = db.Column(db.String(20), index=True, default='')
    vc = db.Column(db.String(11), index=True, default='')
    rsakey = db.Column(db.String(6000), index=True, default='')


class Car(db.Model):
    __tablename__ = 'car'
    car_id = db.Column(db.Integer, primary_key=True)
    cid = db.Column(db.String(64), index=True, unique=True)
    cpassword = db.Column(db.String(64), index=True)
    owner = db.Column(db.Integer, index=True)
    status = db.Column(db.Integer, index=True, default=0)
    command = db.Column(db.Integer, index=True, default=0)
    session_key = db.Column(db.String(100), index=True, default='')
    pub_key = db.Column(db.String(512), index=True, default='')
    tmp = db.Column(db.Integer, index=True, default=0)
    tmp2 = db.Column(db.String(100), index=True, default='')

    def to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = str(getattr(self, key))
            else:
                result[key] = getattr(self, key)
        return result

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = str(getattr(self, key))
            else:
                result[key] = getattr(self, key)
        return result

    # 配合todict一起使用
    def to_json(self):
        v = [ven.dobule_to_dict() for ven in self]
        return v




