import maya.cmds as cmds


class RenameUI():

    def __init__(self):

        self.stringWindow = 'Renaming Sequencer Window'
        self.main_row = ""
        self.textIn = ""
        self.buttonIn = ""

    def delete(self):
        if cmds.window(self.stringWindow, exists=True):
            cmds.deleteUI(self.stringWindow)

    def create(self):

        self.delete()

        self.stringWindow = cmds.window(self.stringWindow,
                                        title='Renaming Sequencer',
                                        widthHeight=[300,100])

        self.main_row = cmds.rowLayout(parent=self.stringWindow,
                                       numberOfColumns=2)
        self.textIn = cmds.textField(parent=self.main_row,
                                     width=200)
        self.buttonIn = cmds.button(parent=self.main_row,
                                    label="Rename",
                                    width=100,
                                    c=lambda *x: self.renamer())
        cmds.showWindow(self.stringWindow)

    def renamer(self):
        input_string = cmds.textField(self.textIn, q=True, text=True)

        num_of_chars = input_string.count("#")

        string_tuple = input_string.partition('#' * num_of_chars)

        tempName = "name"

        replaceValue = '#' * num_of_chars

        if string_tuple[1]:
            sels = cmds.ls(selection=True)
            index = 0
            for sel in sels:
                current_count = str(index)
                tempName = "00" + current_count
                cmds.rename(string_tuple[0] + tempName + string_tuple[2])
                index += 1


        else:
            cmds.error('Input String is not valid. Please enter a name with the formatting of "Name_##_Type"')

