import json
import sys

config = {
  "simulation": {
    "Starting point": 60000,
    "Ending point": 180000,
    "Point interval": 1
  },
  "parameters": {
    "neural_input/x_i": sys.argv[1],
    "neural_input/x_e": sys.argv[2]
  },
  "output": [
    "active_tension/T",
    "neural_input/x_i",
    "neural_input/x_e"
  ]
}

with open('config.json', 'w') as outfile:
    json.dump(config, outfile)
