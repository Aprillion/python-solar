"""Read and write JSON files"""

import json

with open('./original.json') as original, \
     open('./output.json', 'w') as output:
    config = json.load(original)
    config["133"] = config["134"]
    del config["134"]
    json.dump(config, output)
