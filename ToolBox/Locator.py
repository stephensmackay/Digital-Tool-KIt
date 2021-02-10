import maya.cmds as cmds


class CreateLocatators():

    def __init__(self):

        self.stringWindow = 'Create Locators and Joints'
        self.main_row = ""
        self.two_row = ""
        self.buttonIn = ""
        self.two_button = ""

    def delete(self):
        if cmds.window(self.stringWindow, exists=True):
            cmds.deleteUI(self.stringWindow)

    def create(self):

        self.delete()

        self.stringWindow = cmds.window(self.stringWindow,
                                        title='Create Locator',
                                        widthHeight=[300,100])

        self.main_row = cmds.rowLayout(parent=self.stringWindow,
                                       numberOfColumns=2)
        self.buttonIn = cmds.button(parent=self.main_row,
                                    width=300,
                                    c=lambda *x: self.create_locator(),
                                    label="Create Locator")
        self.two_button = cmds.button(width=300,
                                      c=lambda *x: self.Create_Joints(),
                                      label="Create Joints")
        cmds.showWindow(self.stringWindow)

    def Create_Joints(self):
        sels = cmds.ls(sl=True)

        for s in sels:
            jnt = cmds.joint(s, r=True)
            cmds.select(jnt)
            cmds.parent(w=True)

    def create_locator(self):
        sels = cmds.ls(sl=True)

        bbox = cmds.exactWorldBoundingBox(sels)
        x_pos = (bbox[0] + bbox[3]) / 2
        y_pos = (bbox[1] + bbox[4]) / 2
        z_pos = (bbox[2] + bbox[5]) / 2

        loc = cmds.spaceLocator()[0]
        cmds.xform(loc, worldSpace=True, translation=[x_pos, y_pos, z_pos])

        cmds.select(loc, r=True)

        return loc


