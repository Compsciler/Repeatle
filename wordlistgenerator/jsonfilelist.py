try:
    import simplejson as json
except (ImportError,):
    import json

def json_file_to_list(json_file):
    with open(json_file, 'r') as json_file_r:
        json_file_string = json_file_r.read()
        return json.loads(json_file_string)

def list_to_json_file(list_, json_file):
    with open(json_file, 'w') as json_file_w:
	    json.dump(list_, json_file_w, indent=2)

