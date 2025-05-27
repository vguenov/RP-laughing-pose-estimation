from datetime import datetime

coco_json_template = {
    "info": {
        "description": "The CONFLAB dataset is the first multimodal dataset of in-the-wild social interaction recorded during a conference. This file contains skeleton data for the recorded subjects, annotated from top-down videos of the interaction space.",
        "url": "",
        "version": "0.1.0",
        "year": "2021",
        "date_created": datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    },
    "annotations": {

    },
    "categories": [{
        "supercategory": "person",
        "name": "person",
        "skeleton": [[0, 1], [0, 2], [2, 3], [2, 6], [3, 4], [4, 5], [6, 7], [7, 8], [2, 9], [9, 10], [10, 11], [11, 15], [2, 12], [12, 13], [13, 14], [14, 16]],
        "keypoints": [
            'head',             # 0
            'nose',             # 1
            'neck',             # 2
            'rightShoulder',    # ...
            'rightElbow',
            'rightWrist',       # 5
            'leftShoulder',
            'leftElbow',
            'leftWrist',
            'rightHip',
            'rightKnee',        # 10
            'rightAnkle',
            'leftHip',
            'leftKnee',
            'leftAnkle',
            'rightFoot',        # 15
            'leftFoot'],
        "id": 1
    }]
}

part_labels = [
    'head',
    'nose',
    'neck',
    'rightShoulder',
    'rightElbow',
    'rightWrist',
    'leftShoulder',
    'leftElbow',
    'leftWrist',
    'rightHip',
    'rightKnee',
    'rightAnkle',
    'leftHip',
    'leftKnee',
    'leftAnkle',
    'rightFoot',
    'leftFoot'
]
part_map = {e: i for i, e in enumerate(part_labels)}

