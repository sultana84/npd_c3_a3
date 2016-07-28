from json import loads, dumps

class MySerializer(object):

  @classmethod
  def deseralize(cls, jsonstr):
    json_dict = loads(json_str)
    cls = loads(json_str)
    #load from json to dict
    #initialize object, return
    return cls(**d)

  def serialize(self):
    #interate over seld.my_attrs
    #get attrs, set into dictionary
    #return dumps(dictionary) 
    pass 
