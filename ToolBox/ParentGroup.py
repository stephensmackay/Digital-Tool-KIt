import maya.cmds as cmds


class GroupParent():

    def __init__(self):

        self.stringWindow = 'ParentGroup'
        self.main_row = ""
        self.buttonIn = ""

    def delete(self):
        if cmds.window(self.stringWindow, exists=True):
            cmds.deleteUI(self.stringWindow)

    def create(self):

        self.delete()

        self.stringWindow = cmds.window(self.stringWindow,
                                        title='Parent Groups',
                                        widthHeight=[300,100])

        self.main_row = cmds.rowLayout(parent=self.stringWindow,
                                       numberOfColumns=1)
        self.buttonIn = cmds.button(parent=self.main_row,
                                    width=300,
                                    c=lambda *x: self.Grouper(),
                                    label="Parent")
        cmds.showWindow(self.stringWindow)

    def Grouper(self):
        sels = cmds.ls(selection=True)

        for s in sels:
            groups = cmds.group(em=True)
            cmds.parent(s, groups)
