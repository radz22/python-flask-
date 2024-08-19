from flask import jsonify, request
#this is controller function
def loginController():
    try:
       
        data = request.get_json()
        #pang deconstruct ng objects
        name, age = data['name'], data['age']

        if not name and age:
            return jsonify({"error": "No data provided"}), 400
        
        return jsonify({"message": "Data received", "name": name, "age": age}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
def getuser():
    try:
        
        return jsonify({"message": "Data received", "name": "eyy", "age": "ey"}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def getuserparamsid(id):
    try:
        
        return jsonify({"id":id}), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
