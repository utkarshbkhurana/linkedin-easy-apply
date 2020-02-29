import json
USERNAME = PASSWORD = ''
JOBS = FOLLOWERS = 0
SEARCHTEXT = ''

def init():
    global USERNAME, PASSWORD , JOBS, FOLLOWERS, SEARCHTEXT
    # read file
    data = None
    with open('settings.json', 'r') as myfile:
        data = myfile.read()
    obj = json.loads(data)
    USERNAME = obj['linkedin']['user']
    PASSWORD = obj['linkedin']['pass']
    FOLLOWERS = obj['config']['min_company_followers']
    SEARCHTEXT = obj['config']['keywords']