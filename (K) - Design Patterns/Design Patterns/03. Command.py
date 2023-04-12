# # 3. Command:


# Create class Window and class Document.
# The Window class will have an exit method.
# The Document class will have a save method:


import sys


class Window:
    def exit(self):
        sys.exit(0)


class Document:
    def __init__(self, filename):
        self.filename = filename
        self.contents = "This file cannot be modified"

    def save(self):
        with open(self.filename, "w") as file:
            file.write(self.contents)


# Next, we will create the classes ToolbarDocument, MenuItem, and KeyboardShortcut.
# The ToolbarDocument and the MenuItem will have a method click.
# The KeyboardShortcut should have a method called keypress.


class ToolbarDocument:
    def __init__(self, name, iconname):
        self.name = name
        self.iconname = iconname

    def click(self):
        self.command.execute()


class MenuItem:
    def __init__(self, menu_name, item_name):
        self.menu_name = menu_name
        self.item_name = item_name

    def click(self):
        self.command.execute()


class KeyboardShortcut:
    def __init__(self, key, modifier):
        self.key = key
        self.modifier = modifier

    def keypress(self):
        self.command.execute()


# Finally, we will create two command classes SaveCommand and ExitCommand
# which will have the execute methods implemented in them:


class SaveCommand:
    def __init__(self, document):
        self.document = document

    def execute(self):
        self.document.save()


class ExitCommand:
    def __init__(self, window):
        self.window = window

    def execute(self):
        self.window.exit()
