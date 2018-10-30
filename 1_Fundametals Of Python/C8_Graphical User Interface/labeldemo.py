"""
File: labeldemo.py
"""

from breezypythongui import EasyFrame

class LabelDemo(EasyFrame):
    """Displays a greeting in a window."""

    def __init__(self):
        """Sets up the window and the label."""
        EasyFrame.__init__(self, width = 300, height = 200, title = "Label Demo")
        self.addLabel(text = "Hello world!", row = 0, column = 0)
# Window layout
class LayoutDemo(EasyFrame):
    """Displays labels in the quadrants."""

    def __init__(self):
        """Sets up the window and the labels."""
        EasyFrame.__init__(self, width = 300, height = 200, title = "Label Demo")

        # Set the background of the window into blue
        self["background"] = "lightblue"
        # Make the window unresizable
        self.setResizable(False)

        self.addLabel(text = "(0 and 1, 0)", row = 0, column = 0, sticky = "NSEW" , rowspan = 2)
        self.addLabel(text = "(0, 1)", row = 0, column = 1, sticky = "NSEW")
        self.addLabel(text = "(0, 2)", row = 0, column = 2, sticky = "NSEW")
        self.addLabel(text = "(1, 1 and 2)", row = 1, column = 1, sticky = "NSEW", columnspan = 2)




def main():
    """Instantiates and pops up the window."""
    # LabelDemo().mainloop()
    LayoutDemo().mainloop()
if __name__ == "__main__":
    main()









"""
    1. In the __init__ method of a main window class.
        It usually sets up some specific specifications of a main window.
        Technically, it calls a __init__ method if existed to create the window for instance,
        then, a programmer only writes something which he wants to be in the window.

    2. It’s a good idea to make a new class a subclass of an existing class.
        Because, we don't have to reinvent all the methods that are already made
        in class, we just nedd to inherit it and customize it like what we want.
        Moreover, we will save lots of time to do other things than just concentrating on
        the unnescessary things.

"""
