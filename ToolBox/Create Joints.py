import maya.cmds as cmds



def Create_Joints():
    sels = cmds.ls(sl=True)

    for s in sels:
        jnt = cmds.joint(s, r=True)
        cmds.select(jnt)
        cmds.parent(w=True)


Create_Joints()
