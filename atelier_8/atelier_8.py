from maya import cmds

cmds.cutKey('pCube1', clear=True) # clears the keys before creating new ones
k = 0 # initial position of the cube
j = 0 # initialisint time value

for i in range(5): # number of keys that will be placed, value is between the ()
    cmds.setKeyframe('pCube1', attribute='translateZ', time=j, value=k) # sets keyframes
    k += 10 # nb of cm the cube moves at the placed keyframe
    j += 25 # time between keyframes

cmds.playbackOptions(min=0, max=100) # sets min and max values for the playback