def create_datastructure(data_list):
  new_dict = {}
  for d in data_list:
    new_dict[d['_id']] = {
      'state' : d['state'],
      'city' : d['city'],
      'longitude' : d['loc'][0],
      'latitude' : d['loc'][1]
    }
  return new_dict

