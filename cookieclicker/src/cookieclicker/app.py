"""
The Cookie Clicker app refreshed
"""

import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
cookies = 0
num = 1 
class CookieClicker(toga.App):
    def startup(self):
        main_box = toga.Box(style=Pack(direction=COLUMN))

        self.cookievalue = toga.Label(
            "0",
            style=Pack(padding=(0, 5))
        )

        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(self.cookievalue)

        
        main_box.add(name_box)
        main_box.add(button)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def clickedcookies(self, widget):
        global cookies
        cookies+=num
        yield 0.1
        self.cookievalue.text = cookies
        
        
def main():
    return CookieClicker()
