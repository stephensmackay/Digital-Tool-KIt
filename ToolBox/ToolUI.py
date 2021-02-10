import maya.cmds as cmds
import ToolBox


class ToolBoxUI():
    def __init__(self):

        self.tool_window = 'My Tools'
        self.window__rows = ""

    def delete(self):
        if cmds.window(self.stringWindow, exists=True):
            cmds.deleteUI(self.stringWindow)


    def create(self):
        self.delete
        self.tool_window = cmds.window(self.tool_window, title="My Tools",
                                       widthHeight=[500, 500])
        self.window_rows = cmds.rowLayout(parent=self.tool_window,
                                          numberOfColumns=8)
        cmds.button(parent=self.window_rows,
                    label="Renamer",
                    c=lambda *x: self.Renamer())
        cmds.button(parent=self.window_rows,
                    label="Duplicate and Randomize",
                    c=lambda *x: self.Randomizer())
        cmds.button(parent=self.window_rows,
                    label="Alter History",
                    c=lambda *x: self.FreezeTransforms())
        cmds.button(parent=self.window_rows,
                    label="Parent Groups",
                    c=lambda *x: self.ParentGroup())
        cmds.button(parent=self.window_rows,
                    label="Toggle Axis",
                    c=lambda *x: self.ToggleAxis())
        cmds.button(parent=self.window_rows,
                    label="ParentConstrain",
                    c=lambda *x: self.ParentConstrain())
        cmds.button(parent=self.window_rows,
                    label="Create Locator",
                    c=lambda *x: self.Locator())
        cmds.showWindow(self.tool_window)

    def Renamer(self):
        import ToolBox.RenamewithLayout
        reload(ToolBox.RenamewithLayout)
        rename = ToolBox.RenamewithLayout.RenameUI()
        rename.create()

    def Randomizer(self):
        import ToolBox.RandomwithLayout
        reload(ToolBox.RandomwithLayout)
        rando = ToolBox.RandomwithLayout.Randomizer()
        rando.create()

    def FreezeTransforms(self):
        import ToolBox.FreezeTransform
        reload(ToolBox.FreezeTransform)
        freeze = ToolBox.FreezeTransform.HistoryAlter()
        freeze.create()

    def ParentGroup(self):
        import ToolBox.ParentGroup
        reload(ToolBox.ParentGroup)
        const = ToolBox.ParentGroup.GroupParent()
        const.create()

    def ToggleAxis(self):
        import ToolBox.ToggleAxis
        reload(ToolBox.ToggleAxis)
        togl = ToolBox.ToggleAxis.ToggleAxis()
        togl.create()

    def ParentConstrain(self):
        import ToolBox.ParentConstrain
        reload(ToolBox.ParentConstrain)
        pc = ToolBox.ParentConstrain.ParentConstrain()
        pc.create()

    def Locator(self):
        import  ToolBox.Locator
        reload(ToolBox.Locator)
        lc = ToolBox.Locator.CreateLocatators()
        lc.create()



Tools = ToolBoxUI()

Tools.create()