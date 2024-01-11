
import requests
import json

class GetPrograms:

  def get_programs(self):
    # the endpoint 
    URL = "https://data.cityofchicago.org/resource/ydr8-5enu.json"

    response = requests.get(URL)
    return response.content
  
  def program_agencies(self):
    # we use the JSON library to parse the API response into nicely formatted JSON
      programs_list = []
      programs = json.loads(self.get_programs())
      return json.dumps(programs, indent=3, sort_keys=True)

programs = GetPrograms().program_agencies()
print(programs)