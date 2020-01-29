import json
from datetime import datetime
import os


def save_sim_to_json(ships, owners, ports):
    curpath = os.path.abspath(os.curdir)
    current_time = datetime.now().strftime('%Y-%m-%d_%H;%M;%S')
    with open(f"simulations/{current_time}.json", 'w') as result:
        ships_json = [s.to_dict() for s in ships]
        owners_json = [o.to_dict() for o in owners]
        ports_json = [p.to_dict() for p in ports]
        output = {'ships': ships_json,
                  'owners': owners_json, 'ports': ports_json}
        json.dump(output, result, sort_keys=True, indent=4)
