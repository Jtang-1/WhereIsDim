from . import db
from sqlalchemy.sql import func

class UserModel (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    # first_name = db.Column(db.String(50), nullable=False)
    # last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    lng = db.Column(db.Integer, nullable=False)
    lat = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(200), nullable=False)
    country = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default = func.now())
    
    #user.id points to User class. One to many relation (one user, many to do)
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 

    def __repr__(self):
        return f"<User#({self._id}), first_name = ({self.first_name}), last_name = ({self.last_name})>"

    @property
    def serialize(self):
       """Return object data in easily serializable format"""
       return {
        #    'id'         : self.id,
           'email'      : self.email,
        #    'city'       : self.city,
        #     'country'   : self.country,
            'lng'       : self.lng,
            'lat'       : self.lat,
           'date_created': dump_datetime(self.date_created)
       }
    

def dump_datetime(value):
    """Deserialize datetime object into string form for JSON processing."""
    if value is None:
        return None
    return [value.strftime("%Y-%m-%d"), value.strftime("%H:%M:%S")]