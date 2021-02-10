import maya.cmds as cmds


class ToggleAxis():

    def __init__(self):

        self.stringWindow = 'Toggle Axis'
        self.main_row = ""
        self.buttonIn = ""

    def delete(self):
        if cmds.window(self.stringWindow, exists=True):
            cmds.deleteUI(self.stringWindow)

    def create(self):

        self.delete()

        self.stringWindow = cmds.window(self.stringWindow,
                                        title='Toggle Axis',
                                        widthHeight=[300,100])

        self.main_row = cmds.rowLayout(parent=self.stringWindow,
                                       numberOfColumns=1)
        self.buttonIn = cmds.button(parent=self.main_row,
                                    width=300,
                                    c=lambda *x: self.Toggled(),
                                    label="Toggle Axis")
        cmds.showWindow(self.stringWindow)

    def Toggled(self):
        sels = cmds.ls(selection=True)

        cmds.toggle(la=True)

        for s in sels:

            cmds.setAttr(s + ".jointOrientX", cb=True)
            cmds.setAttr(s + ".jointOrientY", cb=True)
            cmds.setAttr(s + ".jointOrientZ", cb=True)
            cmds.setAttr(s + ".displayLocalAxis", cb=True)


