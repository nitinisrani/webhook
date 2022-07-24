from datetime import datetime
from flask import Blueprint, json, jsonify, render_template, request

from app.extensions import mongo
from app.webhook.DataHelper import pull_req_func, push_func
from bson import json_util
from pymongo import DESCENDING

webhook = Blueprint('Webhook', __name__, url_prefix='/webhook')


@webhook.route('/receiver', methods=["POST"])
def receiver():
    git_event = request.headers.get('X-GitHub-Event')
    print(git_event)
    content = request.get_json()

    if git_event == 'push':
        mongo.db.gitdata.insert_one(push_func(content)) 

    if git_event == 'pull_request':
        mongo.db.gitdata.insert_one(pull_req_func(content))

    return {}, 200


@webhook.route('/presenter', methods=["GET"])
def presenter():
    
    data_objects = {'data':[]} 
    for obj in mongo.db.gitdata.find().sort('_id',DESCENDING).limit(10):
        data_objects['data'].append(json.loads(json_util.dumps(obj)))
        # print(datetime.strptime(obj["timestamp"],'%Y-%m-%dT%I:%M:%S'))
    return jsonify(data_objects)