import maya.cmds as cmds


class CreateControlsAndGroups():

    def __init__(self):

        self.stringWindow = 'ControlGroups'
        self.main_row = ""
        self.buttonIn = ""

    def delete(self):
        if cmds.window(self.stringWindow, exists=True):
            cmds.deleteUI(self.stringWindow)

    def create(self):

        self.delete()

        self.stringWindow = cmds.window(self.stringWindow,
                                        title='Create Controls and Groups',
                                        widthHeight=[300,100])

        self.main_row = cmds.rowLayout(parent=self.stringWindow,
                                       numberOfColumns=1)
        self.buttonIn = cmds.button(parent=self.main_row,
                                    width=300,
                                    c=lambda *x: self.createcgroups(),
                                    label="Create Controls")
        cmds.showWindow(self.stringWindow)

    def createcgroups(self):
        sels = cmds.ls(selection=True)

        for s in sels:

            ctrl = cmds.circle(r=2)
            groups = cmds.group(a=True, empty=True, world=True)
            cmds.select(s, add=True)
            cmds.matchTransform(groups, s, pos=True, rot=True)
            cmds.select(groups, d=True)
            cmds.select(s, d=True)
            cmds.select(ctrl, add=True)
            cmds.select(groups, add=True)
            cmds.Parent(ctrl,groups)
            cmds.select(ctrl, replace=True)
            cmds.makeIdentity()
            cmds.select(ctrl)
            cmds.rename(s + "_ctrl")
            cmds.select(groups)
            cmds.rename(s + "_ctrl_Group")


tool = CreateControlsAndGroups()
tool.create()