import json

with open('sarkari_data_event_less.json', "r") as ffile:
  file_content = ffile.read()

data = json.loads(file_content)

new_data = []
for d in data:
  if d['model'] != "sarkari.impdates" and d['model'] != "sarkari.implinks" and d['model'] != "sarkari.impupdates":
    new_data.append(d)

with open('sarkari_data_imp_field_less.json', 'w') as ffile:
  ffile.write(json.dumps(new_data))