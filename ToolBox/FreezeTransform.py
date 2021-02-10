import maya.cmds as cmds

class HistoryAlter():

    def __init__(self):

        self.window_Name = "AlterHistory"
        self.act_button1 = ""
        self.layout = ""
        self.act_button2 = ""


    def delete(self):
        if cmds.window(self.window_Name, exists=True):
            cmds.deleteUI(self.window_Name)

    def create(self):

        self.delete()

        self.window_Name = cmds.window(self.window_Name,
                                       title="AlterHistory",
                                       widthHeight=[500, 500])
        self.layout = cmds.rowColumnLayout(parent=self.window_Name,
                                           nr=2)
        self.act_button1 = cmds.button(parent=self.layout,
                                       label="Freeze Transform",
                                       width=300,
                                       c=lambda *x: self.FreezeTransform())
        self.act_button2 = cmds.button(parent=self.layout,
                                       label="Delete History",
                                       width=300,
                                       c=lambda *x: self.DeletingHistory())

        cmds.showWindow(self.window_Name)

    def FreezeTransform(self):
        sel = cmds.ls(selection=True)
        for s in sel:
            cmds.makeIdentity(apply=True, t=1, r=1, s=1, n=0, pn=1)

    def DeletingHistory(self):
        sel = cmds.ls(selection=True)
        for s in sel:
            cmds.delete(constructionHistory=True)

