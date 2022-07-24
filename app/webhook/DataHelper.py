

from datetime import datetime


def push_func(content):
    return {
        "request_id" : content["head_commit"]["id"],
        "author" :  content["pusher"]["name"],
        "action" : 'PUSH',
        "to_branch" : content['ref'].split('/')[-1],
        "timestamp" : datetime.utcfromtimestamp(content["repository"]["pushed_at"]).strftime("%d %B %Y - %I:%M %p UTC"),
    }


def pull_req_func(content):
    if content["action"] == "opened" and content["pull_request"]["merged_at"] == None:
        action = "PULL_REQUEST"
        timestamp = datetime.strptime(content["pull_request"]["created_at"],'%Y-%m-%dT%I:%M:%SZ').strftime("%d %B %Y - %I:%M %p UTC")
    elif content["action"] == "closed" and content["pull_request"]["merged_at"] != None:
        action = "MARGE"
        timestamp = datetime.strptime(content["pull_request"]["merged_at"],'%Y-%m-%dT%I:%M:%SZ').strftime("%d %B %Y - %I:%M %p UTC")


    return{
        'request_id' : content["pull_request"]["id"],
        'author' : content["pull_request"]["user"]["login"],
        'action' : action,
        'from_branch' : content["pull_request"]["head"]["ref"],
        'to_branch' : content["pull_request"]["base"]["ref"],
        'timestamp' : timestamp
    }
    