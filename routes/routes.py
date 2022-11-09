
import uuid
from flask import Blueprint, jsonify, request, Flask
from schemas import User, People, Planets, Fav_Char, Fav_Planets, db
from werkzeug.security import generate_password_hash, check_password_hash

bpUser = Blueprint('bpUser', __name__)
bpPeople = Blueprint('bpPeople', __name__)
bpPlanets = Blueprint('bpPlanets', __name__)
bpFav_Char = Blueprint('bpFav_Char', __name__)
bpFav_Planets= Blueprint('bpFav_Planets', __name__)

@bpPeople.route('/people', methods=['GET'])
def get_all_people():
     people = People.query.all()
     if not people: return jsonify({ "msg": "Empty route. You may need to post some data."}), 404
     people = list(map(lambda people: people.serialize(), people))
     return jsonify(people), 200

@bpPeople.route('/people/<int:id>', methods=['GET'])
def get_people(id):
     people = People.query.get(id)
     return jsonify(people.serialize()), 200

@bpPeople.route('/people', methods=['POST']) 
def add_people():
    #id = request.json.get('id')
    name = request.json.get('name')
    age = request.json.get('age')
    species = request.json.get('species')
    born = request.json.get('born')

    people = People()
    people.name = name
    people.age = age
    people.species = species
    people.born = born
 
    # Save people
    people.save()

    return jsonify(people.serialize()), 201

@bpPeople.route('/people/<int:id>', methods=['PUT'])
def update_people(id):
    id = request.json.get('id')
    name = request.json.get('name')
    age = request.json.get('age')
    species = request.json.get('species')
    born = request.json.get('born')

    people = People.query.get(id)
    people.name = name
    people.age = age
    people.species = species
    people.born = born

    # Save people 
    people.update()

    return jsonify(people.serialize()), 200

@bpPeople.route('/people/<int:id>', methods=['DELETE'])
def delete_people(id):
    id = request.json.get('id')
    name=request.json.get('name')
    age=request.json.get('age')
    species=request.json.get('species')
    born=request.json.get('born')

    people = People.query.get(id)
    people.name=name
    people.age =age
    people.species=species
    people.born=born
    
  
     # Delete people
    people.delete()

    return jsonify(people.serialize()), 200


@bpPlanets.route('/planets', methods=['GET'])
def get_planets():
    planets = Planets.query.all()
    if not planets: return jsonify({ "msg": "Empty route. You may need to post some data."}), 404
    planets = list(map(lambda planet: planet.serialize(), planets))
    return jsonify(planets), 200

@bpPlanets.route('/planets/<int:id>', methods=['GET'])
def get_planet(id):
     planet = Planets.query.get(id)
     return jsonify(planet.serialize()), 200

@bpPlanets.route('/planets', methods=['POST']) 
def add_planet():
    id = request.json.get('id')
    name = request.json.get('name')
    galaxy = request.json.get('galaxy')

    planet = Planets()
    planet.id = id
    planet.name = name
    planet.galaxy = galaxy

    # Save planet
    planet.save()

    return jsonify(planet.serialize()), 201


@bpPlanets.route('/planets/<int:id>',methods=['PUT'])
def update_planet(id):
    id = request.json.get('id')
    name = request.json.get('name')
    galaxy = request.json.get('galaxy')

    planet = Planets.query.get(id)
    planet.id = id
    planet.name = name
    planet.galaxy = galaxy

    # Update planet
    planet.update()

    return jsonify(planet.serialize()), 201

@bpPlanets.route('/planets/<int:id>', methods =['DELETE'])
def delete_planet(id):
    id = request.json.get('id')
    name = request.json.get('name')
    galaxy = request.json.get('galaxy')

    planet = Planets.query.get(id)
    planet.id = id
    planet.name = name
    planet.galaxy = galaxy

    # Delete planet
    planet.delete()

    return jsonify(planet.serialize()), 201



@bpUser.route('/users', methods=['POST']) 
def add_user():
    #id = request.json.get('id')
    username= request.json.get('username')
    name= request.json.get('name')
    lastname = request.json.get('lastname')
    email = request.json.get('email')

    user = User()
    #user.id = id
    user.username = username
    user.name = name
    user.lastname = lastname
    user.email = email
 
    # Save user
    user.save()

    return jsonify(user.serialize()), 201


@bpUser.route('/users', methods=['GET'])
def get_users():
     users = User.query.all()
     users = list(map(lambda user: user.serialize(), users))
     return jsonify(users), 200

@bpUser.route('/users/favorites', methods=['GET'])
def get_favs_users():
     favs = User.query.all()
     favs= list(map(lambda fav: fav.serialize_with_favs(), favs))
     return jsonify(favs), 200


@bpFav_Char.route('/favorite/people/<int:id>', methods=['POST'])
def add_fav_char(id):
    id_user = 1

    fav_char = Fav_Char()
    fav_char.id_user = id_user
    fav_char.people_id = id


    # Save fav_people
    fav_char.save()

    return jsonify(fav_char.serialize()), 201


@bpFav_Planets.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_fav_planet(planet_id):
    id_user = request.json.get('id_user')

    fav_planet = Fav_Planets()
    fav_planet.id_user = id_user
    fav_planet.planet_id = planet_id


    # Save fav_planet
    fav_planet.save()

    return jsonify(fav_planet.serialize()), 201


@bpFav_Char.route('/favorite/people/<int:id>', methods=['DELETE'])
def delete_fav_char(id):

    fav_char = Fav_Char.query.filter_by(id_user=1,people_id=id).first()

     # Delete fav_people
    fav_char.delete()

    return jsonify({"mensaje":"Favorite Character deleted."}), 200


@bpFav_Planets.route('/favorite/planet/<int:id>', methods=['DELETE'])
def delete_fav_planet(id):
    fav_planet = Favorite_Planets.query.filter_by(id_user=1,planet_id=id).first()

     # Delete_fav_planet
    fav_planet.delete()

    return jsonify({"mensaje":"Favorite Planet deleted."}), 200
