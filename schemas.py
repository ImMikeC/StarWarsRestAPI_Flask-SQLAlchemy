from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    username= db.Column(db.String(80), unique=True, nullable=True)
    name= db.Column(db.String(80), unique=False, nullable=True)
    lastname = db.Column(db.String(80), unique=False, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    fav_people = db.relationship('Fav_Char')
    fav_planet = db.relationship('Fav_Planets')
    

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "username" : self.username,
            "name" :self.name,
            "lastname": self.lastname,
            "email": self.email,
          
        }
    
    def serialize_with_favs(self):
        fav_people = [people.serialize() for people in self.fav_people]
        fav_planet= [planet.serialize() for planet in self.fav_planet]
        
        return {
            "id": self.id,
            "username" : self.username,
            "name" :self.name,
            "lastname": self.lastname,
            "email": self.email,
            "fav_list" : fav_people+fav_planet
        }

    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class People (db.Model):
    __tablename__="people"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    age = db.Column(db.Integer)
    species = db.Column(db.String(50))
    born= db.Column(db.String(50))
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "species": self.species,
            "born" : self.born
        }
    
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Planets (db.Model):
    __tablename__="planet"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    galaxy = db.Column(db.String(50))
   

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "galaxy": self.galaxy
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Fav_Char (db.Model):
    __tablename__="fav_people"
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'), nullable=False)
    people = db.relationship('People')

    def serialize(self):
        return {
            "id": self.id,
            "id_user": self.id_user,
            "name": self.people.name
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Fav_Planets (db.Model):
    __tablename__="fav_planets"
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    fav_planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'), nullable=False)
    planet = db.relationship('Planets')

    def serialize(self):
        return {
            "id": self.id,
            "id_user": self.id_user,
            "name": self.planet.name
        }
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
    