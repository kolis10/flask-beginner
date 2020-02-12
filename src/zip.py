import requests
import json

def create_datastructure():
  new_dict = {}
  for d in data:
    new_dict[d['_id']] = {
      'state' : d['state'],
      'city' : d['city'],
      'longitude' : d['loc'][0],
      'latitude' : d['loc'][1],
      'population' : d['pop'],
      'zip' : d['_id']
    }
  return new_dict

def find_new_city(a):
    info = []
    for key in datas.keys():
        if datas[key]['city'] == a:
            info.append({
                'zip_code': key,
                **datas[key]
            })
    return info


















data = requests.get('https://assets.breatheco.de/apis/fake/zips.php').json()

datas = create_datastructure()

with open('src/zipcodes.json', 'w') as f:
    json.dump(datas, f)