import maya.cmds as cmds
import random

#<editor-fold desc="Description">
class Randomizer():

    def __init__(self):

        self.window_Name = "Randomizer"
        self.act_button = ""
        self.layout = ""
        self.numOfDups = ""
        self.minXField = ""
        self.maxXField = ""
        self.minYField = ""
        self.maxYField = ""
        self.minZField = ""
        self.maxZField = ""

    def delete(self):
        if cmds.window(self.window_Name, exists=True):
            cmds.deleteUI(self.window_Name)

    def create(self):

        self.delete()

        self.window_Name = cmds.window(self.window_Name,
                                       title="Randomizer",
                                       widthHeight=[500, 500])
        self.layout = cmds.rowColumnLayout(parent=self.window_Name,
                                           nr=2)
        self.numOfDups = cmds.intField(parent=self.layout,
                                       ann="Number of Duplicates",width=300)
        self.act_button = cmds.button(parent=self.layout,
                                      label="Submit",
                                      width=300,
                                      c=lambda *x: self.DuplicateAndScatter())
        self.minXField = cmds.intField(parent=self.layout,
                                       ann="Min X",
                                       width=300)
        self.maxXField = cmds.intField(parent=self.layout,
                                       ann="Max X",
                                       width=300)
        self.minYField = cmds.intField(parent=self.layout,
                                       ann="Min Y",
                                       width=300)
        self.maxYField = cmds.intField(parent=self.layout,
                                       ann="Max Y",
                                       width=300)
        self.minZField = cmds.intField(parent=self.layout,
                                       ann="Min Z",
                                       width=300)
        self.maxZField = cmds.intField(parent=self.layout,
                                       ann="MaxZ",
                                       width=300)
        cmds.showWindow(self.window_Name)

    def DuplicateAndScatter(self):
        numOfDuplicates = cmds.intField(self.numOfDups, q=True, value=True)
        minX = cmds.intField(self.minXField, q=True, value=True)
        maxX = cmds.intField(self.maxXField, q=True, value=True)
        minY = cmds.intField(self.minYField, q=True, value=True)
        maxY = cmds.intField(self.maxYField, q=True, value=True)
        minZ = cmds.intField(self.minZField, q=True, value=True)
        maxZ = cmds.intField(self.maxZField, q=True, value=True)

        sels = cmds.ls(selection=True)

        for item in range(len(cmds.ls(selection=True))):
            index = item

            for items in range(numOfDuplicates):
                tempObj = (cmds.duplicate(sels[index], rr=True))
                randX = random.uniform(minX, maxX)
                randY = random.uniform(minY, maxY)
                randZ = random.uniform(minZ, maxZ)

                cmds.select(tempObj)
                cmds.xform(worldSpace=True, translation=[randX, randY, randZ])

#</editor-fold>