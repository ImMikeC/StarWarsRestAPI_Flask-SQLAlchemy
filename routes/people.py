import uuid
from flask import Blueprint, jsonify, request, Flask
from schemas import User, People, Planets, Fav_Char, Fav_Planets, db
from werkzeug.security import generate_password_hash, check_password_hash

bpPeople = Blueprint('bpPeople', __name__)

@bpPeople.route('/people', methods=['GET'])
def get_people():
     people = People.query.all()
     if not people: return jsonify({ "msg": "Empty route. You may need to post some data."}), 404
     people = list(map(lambda people: people.serialize(), people))
     return jsonify(people), 200

@bpPeople.route('/people/<int:id>', methods=['GET'])
def traer_people(id):
     people = People.query.get(id)
     return jsonify(people.serialize()), 200

@bpPeople.route('/people', methods=['POST']) 
def agregar_people():
    id = request.json.get('id')
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
def borrar_people(id):
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

