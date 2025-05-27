import json
import copy
import editdistance
import click
import os

import numpy as np

from constants import coco_json_template, part_labels, part_map

def process_json(data):
    filtered = filter(lambda x: len(x) == 7, data)
    d = {e[2]: {'x': e[3], 'y': e[4], 'valid': e[5], 'occluded': e[6]}
         for e in filtered}
    return d


def get_len(d):
    return int(d['data'][-1][2]) + 1


def get_partid(part):
    edit_distances = np.array([editdistance.eval(part, lbl)
                               for lbl in part_labels])
    pn = np.where(edit_distances <= 2)[0]
    if len(pn) == 0 or len(pn) > 1:
        return None
    return part_map[part_labels[pn[0]]]

def annotations_to_skeletons(instance_json):
    num_frames = get_len(instance_json[0])
    hit_name = instance_json[0]['hit_name']
    skeletons = [dict() for i in range(num_frames)]

    for task_json in instance_json:
        processed_data = process_json(task_json['data'])
        assert task_json['hit_name'] == hit_name
        task_name = task_json['task_name']

        chunks = task_name.split('_')
        if len(chunks) != 2:
            continue

        pid = int(chunks[0][1:])
        body_part = chunks[1]

        bp_id = get_partid(body_part)
        if bp_id is None:
            print(f'Invalid task name {task_name}, filename = {file}')
            continue

        for fn, frame_data in processed_data.items():
            if fn >= len(skeletons):
                # print((root, file, fn, len(skeletons)))
                continue

            if pid not in skeletons[fn]:
                skeletons[fn][pid] = {
                    "num_keypoints": 0,
                    "keypoints": [None] * 34,
                    "occluded": [None] * 17,
                    "image_id": fn,
                    "category_id": 1,
                    "id": pid
                }

            skeletons[fn][pid]['keypoints'][bp_id*2] = frame_data['x']
            skeletons[fn][pid]['keypoints'][bp_id*2+1] = frame_data['y']
            skeletons[fn][pid]['occluded'][bp_id] = frame_data['occluded']
            skeletons[fn][pid]['num_keypoints'] += 1
    return skeletons

@click.command()
@click.option('--input', help='covfee input json')
@click.option('--output', help='file path to write hit annotations to')
def cmd_process(input, output):
    # get the number of frames in the files (should be the same for all)

    instance_json = json.load(open(input))
    
    skeletons = annotations_to_skeletons(instance_json)
    coco_json = copy.deepcopy(coco_json_template)
    coco_json['annotations']['skeletons'] = skeletons
    with open(os.path.join(output), 'w') as f:
        json.dump(coco_json, f, indent=4)
    
if __name__ == '__main__':
    cmd_process()
