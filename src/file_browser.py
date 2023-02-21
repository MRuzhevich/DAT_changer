import os
from tkinter import (
    filedialog,
    Tk,
    Label,
    Button,
)
from typing import Iterable


class FileBrowser:
    """Selects a file from the user's computer"""

    # path to file
    filenames: Iterable[str] | None = None
    curr_directory = os.getcwd()

    def __init__(self):
        self.file_explorer()

    def file_explorer(self):
        """Function for opening the file explorer window"""

        def browseFiles():
            self.filenames = filedialog.askopenfilenames(
                initialdir=self.curr_directory,
                title="Select a File",
                filetypes=(
                    ("DAT files", "*.dat*"),
                    ("all files", "*.*"),
                ),
            )

            # Change label contents
            label_file_explorer.configure(
                text=f"File Opened: {str(self.filenames)}"
            )
            close_window()

        def close_window():
            print(self.filenames)
            window.destroy()
            return

        def exit():
            window.destroy()
            return

        print(self.filenames)

        # Create the root window
        window = Tk()

        # Set window title
        window.title("File Explorer")

        # Set window size
        window.geometry("700x100")

        # Set window background color
        window.config(background="white")

        # Create a File Explorer label
        label_file_explorer = Label(
            window,
            text="File Explorer for DAT changer",
            width=100,
            height=4,
            fg="blue",
        )

        button_explore = Button(
            window, text="Browse Files", command=browseFiles
        )

        # button_open = Button(window,
        # 						text = "Open graph",
        # 						command = close_window)

        button_exit = Button(window, text="Exit", command=exit)

        label_file_explorer.grid(column=1, row=2, columnspan=1000)

        button_explore.grid(column=1, row=1)

        # button_open.grid(column = 2, row = 1)

        button_exit.grid(column=3, row=1)

        # Let the window wait for any events
        window.mainloop()


if __name__ == "__main__":
    hello = FileBrowser()
