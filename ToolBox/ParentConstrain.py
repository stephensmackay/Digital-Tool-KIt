import maya.cmds as cmds


class ParentConstrain():

    #Must Select Joint Then the desired child, can select as many pairing as desired, but must complete a pairing group before selecting the next Joint

    def __init__(self):

        self.stringWindow = 'ParentConstrain'
        self.main_row = ""
        self.buttonIn = ""

    def delete(self):
        if cmds.window(self.stringWindow, exists=True):
            cmds.deleteUI(self.stringWindow)

    def create(self):

        self.delete()

        self.stringWindow = cmds.window(self.stringWindow,
                                        title='Parent Constrain',
                                        widthHeight=[300,100])

        self.main_row = cmds.rowLayout(parent=self.stringWindow,
                                       numberOfColumns=1)
        self.buttonIn = cmds.button(parent=self.main_row,
                                    width=300,
                                    c=lambda *x: self.Constrain(),
                                    label="Constrain")
        cmds.showWindow(self.stringWindow)

    def Constrain(self):
        sels = cmds.ls(selection=True)

        if len(sels) % 2 == 1:
            cmds.error("Invalid Selection Pairings")
        else:
            for s in range(0, len(sels), 2):
                cmds.parentConstraint(sels[s], sels[s + 1])
                cmds.scaleConstraint(sels[s], sels[s + 1])


