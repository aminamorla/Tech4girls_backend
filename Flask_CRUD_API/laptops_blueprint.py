from flask import Blueprint, request, jsonify
from werkzeug.exceptions import NotFound, BadRequest
from laptop_crud import Laptop_crud

#define blueprint
laptops_blueprint = Blueprint('laptops', __name__)

laptops = {}

#Route = add a laptop
@laptops_blueprint.route('/laptops/add', methods=['POST'])
def add_laptop():
    data = request.get_json()
    #check if all required fields are present 
    required_fields = ['name', 'laptop_number', 'specifications']
    for field in required_fields:
        if field not in data:
            raise BadRequest(f"Missing required field: {field}")
        
        laptop_number = data['laptop_number']

#check if laptop number is unique
        if laptop_number in laptops:
            raise BadRequest(f"Laptop number {laptop_number} already exists")
        #add the laptop to the storage
        laptops[laptop_number] = {
            'name': data['name'],
            'laptop_number': laptop_number,
            'specifications': data['specifications']
        }
        return jsonify({"message": "Laptop added successfully"}), 201
    
# GET all laptops
@laptops_blueprint.route('/laptops', methods=['GET'])
def get_all_laptops():
    return jsonify(list(laptops.values())), 200

# GET a laptop by Name
@laptops_blueprint.route('/laptops/name/<string:name>', methods=['GET'])
def get_laptop_by_name(name):
    #search for a laptop by its name
    for laptop in laptops.values():
        if laptop['name'].lower() == name.lower():
            return jsonify(laptop), 200
        raise NotFound(f"Laptop with name {name} not found")
    
# GET a laptot by laptop number
@laptops_blueprint.route('/laptops/number/<string:laptop_number>', methods=['GET'])
def get_laptop_by_number(laptop_number):
    #search for a laptop by its laptop_number
    laptop = laptops.get(laptop_number)
    if laptop:
        return jsonify(laptop), 200
    raise NotFound(f"Laptop with number {laptop_number} not found")

#Update a laptop by laptop number
@laptops_blueprint.route('/laptops/update/<string:laptop_number>', methods=['PUT'])
def update_laptop(laptop_number):
    data = request.get_json()
   
    #check if laptop exits
    if laptop_number not in laptops:
        raise NotFound(f"Laptop with number {laptop_number} not found")
    #update the laptop data
    laptop = laptops[laptop_number]
    laptop['name'] = data.get('name', laptop['name'])
    laptop['specifications'] = data.get('specifications', laptop['specifications'])
    return jsonify({"message": "Laptop updated successfully"}), 200
#Delete a laptop by laptop number
@laptops_blueprint.route('/laptops/delete/<string:laptop_number>', methods=['DELETE'])
def delete_laptop(laptop_number):
    #check if lapto exists
    if laptop_number not in laptops:
        raise NotFound(f"Laptop with number {laptop_number} not found")
    #delete the laptop
    del laptops[laptop_number]
    return jsonify({"message": "Laptop deleted successfully"}), 200