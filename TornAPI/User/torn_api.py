import requests, json, os

def add_to_obj(from_obj, to_obj, key):
    if key in from_obj:
        to_obj[key] = from_obj[key]

# Create your tests here.
def lookup_user():
    config = ""
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    conf_path = os.path.join(BASE_DIR, 'User', 'config.json')
    with open(conf_path) as conf_file:
        config = json.load(conf_file)
    key = config['torn_api_key']
    url = f"https://api.torn.com/user/?key={key}"
    ret = requests.get(url)
    if ret.status_code == 200:
        data = json.loads(ret.content)
    else:
        data = "Unable to contact the Torn API"
    trimmed_data = {}
    add_to_obj(data, trimmed_data, "level")
    add_to_obj(data, trimmed_data, "gender")
    #trimmed_data = json.dumps(trimmed_data, indent=2)
    return trimmed_data


if __name__=="__main__":
    print(lookup_user())
