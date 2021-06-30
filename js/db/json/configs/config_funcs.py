import json
import os

def print_config(num):
    with open(str(num)+'.json') as f:
        config = json.load(f)
    # print(json.dumps(config,indent=4,sort_keys=True))
    print('accelerationChangePenalty: '+ str(round(config['comfort']['accelerationChangePenalty'],4)))
    print('-\n-\n-\n-\n-\n-')
    print('extraTimePenalty: '+ str(round(config['efficiency']['extraTimePenalty'],4)))
    print('-')
    print('hardAccelerationPenalty: '+ str(round(config['comfort']['accelerationChangePenalty'],4)))
    print('hardDecelerationPenalty: '+ str(round(config['comfort']['accelerationChangePenalty'],4)))
    print('-\n-\n-\n-\n-\n-\n-')
    print('linearLateralAccelerationPenalty: '+ str(round(config['comfort']['accelerationChangePenalty'],4)))
    print('obstacleHazardCost: '+ str(round(config['safety']['obstacleHazardCost'],4)))
    print('-\n-\n-')
    print('softLateralAccelerationPenalty: '+ str(round(config['comfort']['accelerationChangePenalty'],4)))
    print('-')
    print('speedLimitPenalty: '+ str(round(config['violations']['speedLimitPenalty'],4)))

def rename_webm(num):
    os.rename('/Users/sonia/Downloads/screen-capture.webm','/Users/sonia/Downloads/'+str(num)+'.webm')

