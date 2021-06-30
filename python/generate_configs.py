from random import randint
import copy
import json

config_template = {"weights": {"safety": 0, "comfort": 0, "efficiency": 0, "violations": 0}, "safety": {"obstacleHazardCost":100}, "comfort": {"hardAccelerationPenalty": 10, "hardDecelerationPenalty": 10, "softLateralAccelerationPenalty": 10, "linearLateralAccelerationPenalty": 10, "accelerationChangePenalty": 10}, "efficiency": {"extraTimePenalty": 100}, "violations": {"speedLimitPenalty": 100}, "stimulus_created": False}

def generate_random_weights():
    l = [randint(1, 10) for i in range(4)]
    weight_list = [(i / sum(l)) * 10 for i in l] 
    return [("safety", weight_list[0]), ("comfort", weight_list[1]), ("efficiency", weight_list[2]), ("violations", weight_list[3])]

def generate_config_params(weights):
    config = copy.deepcopy(config_template)
    for type, weight in weights:
        baseline = config_template[type]
        num_subtypes = len(baseline.keys())
        for key, value in config[type].items():
            if key == "weights":
                continue
            config[type][key] = config_template[type][key] * weight
            config["weights"][type] = weight
    return config

config_id = 3
for i in range(100):
    config_id += 1 
    config = generate_config_params(generate_random_weights())
    config["id"] = config_id
    with open(f"../js/db/json/configs/{config_id}.json", 'w') as outfile:
        json.dump(config, outfile)


