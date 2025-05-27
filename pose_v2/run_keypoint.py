import os

path = '/tudelft.net/staff-bulk/ewi/insy/SPCDataSets/conflab-mm/processed/annotation/keypoints/'

files = [f for f in os.listdir(path) if f.endswith('.json')]

print(files)

commands = []

for file in files:
	filename = file[:-5]
	command = 'python keypoint_post.py ' + '--input='+path+file  + ' --output=' +filename + '_coco.json'
	commands.append(command)
print(commands)
print("total commands: ", len(commands))

#Actual run:
for c in range(0,len(commands)):
	print("----RUNNING------:", command)
	os.system(commands[c])
	print("*************** FINISHED*********")


