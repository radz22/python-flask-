from flask import Blueprint, jsonify, request

route = Blueprint('auth', __name__, url_prefix='/auth')
 #import from controller and get function name
from controller.user  import loginController
from controller.user  import getuser
from controller.user  import getuserparamsid

 #routes 
# post 
@route.route('/login', methods=['POST'])
def login():
    return loginController()
# get 
@route.route('/user', methods=['GET'])
def user():
    return getuser()
   # get params id 
@route.route('/user/<id>', methods=['GET'])
def userparams(id):
    return getuserparamsid(id)
   