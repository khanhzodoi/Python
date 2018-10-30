"""
File: textfielddemo.py
"""
from breezypythongui import EasyFrame

class TextFieldDemo(EasyFrame):
    """Converts an input string to uppercase and displays
        the results."""
    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, width = 300, height = 200, title = "Text Field Demo")

        # Make the window unresizable
        self.setResizable(False)

        # Label and field for the input
        self.addLabel(text = "Input",
                        row = 0, column = 0,
                        sticky = "W")
        self.inputField = self.addTextField(text = "",
                                            row = 0, column = 1,
                                            sticky = "EW")

        # Label and field for the output
        self.addLabel(text = "Output", row = 1, column = 0, sticky = "W",)
        self.outputField = self.addTextField(text = "",
                                            row = 1, column = 1,
                                            sticky = "EW",
                                            state = "readonly")

        # The command button
        self.addButton(text = "Convert",
                        row = 2, column = 0, columnspan = 2,
                        command = self.convert)

    # The event handling method for the button
    def convert(self):
        """Inputs the string, converts it to the uppercase,
        and outputs the result."""
        text = self.inputField.getText()
        result = text.upper()
        self.outputField.setText(result)

def main():
    TextFieldDemo().mainloop()

if __name__ == "__main__":
    main()
