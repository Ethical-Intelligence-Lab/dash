import json
import os

config_files = [f for f in os.listdir("../js/db/json/configs/") if ".json" in f]
annotate_files = [f for f in os.listdir("../psychophy/data/") if ".json" in f]

configs = []
annotations = []

for c in config_files:
    with open(f"../js/db/json/configs/{c}") as f:
        configs.append(json.load(f))

for a in annotate_files:
    with open(f"../psychophy/data/{a}") as f:
        annotations.append(json.load(f))

weight_annotate_dict = {}

agg_annotations = [item for sublist in annotations for item in sublist]

for a in agg_annotations:
    weight_annotate_dict[f"{a['config']}_{a['user']}"] = {"config": a["config"], "score": a["response"]}

for c in configs:
    try:
        weight_annotate_dict[f"{c['id']}_mike"]["weights"] = c["weights"]
        weight_annotate_dict[f"{c['id']}_sonia"]["weights"] = c["weights"]
    except:
        continue
with open("annotations_weights.json", "w") as f:
    json.dump(weight_annotate_dict, f)

