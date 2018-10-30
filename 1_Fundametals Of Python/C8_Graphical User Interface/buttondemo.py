"""
File: buttondemo.py
"""

from breezypythongui import EasyFrame

class ButtonDemo(EasyFrame):
    """Illustrates command buttons and user events."""

    def __init__(self):
        """Sets up the window, label, buttons."""
        EasyFrame.__init__(self)

        # A single label in the first row.
        self.label = self.addLabel(text = "Hello world!", row = 0,
                        column = 0, columnspan = 2, sticky = "NSEW")

        # Two command buttons in the second row
        self.clearBtn = self.addButton(text = "Clear",
                                            row = 1, column = 0,
                                            command = self.clear)
        self.restoreBtn = self.addButton(text = "Restore",
                                            row = 1, column = 1,
                                            state = "disabled",
                                            command = self.restore)

    # Methods to handle user events.
    def clear(self):
        """Resets the label to the empty string and updates
        the button states."""
        self.label["text"] = ""
        self.clearBtn["state"] = "disabled"
        self.restoreBtn["state"] = "normal"

    def restore(self):
        """Resets the label to 'Hello world!' and updates
        the button states."""
        self.label["text"] = "Hello world!"
        self.clearBtn["state"] = "normal"
        self.restore["state"] = "disabled"

def main():
    ButtonDemo().mainloop()

if __name__ == "__main__":
    main()
