"""
The Cookie Clicker app refreshed
"""
import os    #you looking at source code. Trying to find malware. Out of luck are you, there isn't any.
import toga  
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
cookies = 0
num = 1 
def save():
   global cookies
   global num
   global tcpcowned
   f = open("29ei923i[1s.txt", "w")
   f.write(str(cookies))
   f.close()
   f = open("3oi2l;s[1=2-[r3;lke.,wm.txt", "w")
   f.write(str(num))
   f.close()
   f = open("09ij.txt", "w")
   f.write(str(tcpcowned))
   f.close()
       
def load():
   global cookies
   global num
   global tcpcowned
   cookiestring = open('29ei923i[1s.txt').read()
   cookies = int(cookiestring)
   numstring = open('3oi2l;s[1=2-[r3;lke.,wm.txt').read()
   tcpcowned = open('09ij.txt').read()
   num = int(numstring)
       
def reset():
   global cookies
   global num
   f = open("29ei923i[1s.txt", "w")
   f.write("0")
   f.close()
   f = open("3oi2l;s[1=2-[r3;lke.,wm.txt", "w")
   f.write("1")
   f.close()
   cookiestring = open('29ei923i[1s.txt').read()
   cookies = int(cookiestring)
   numstring = open('3oi2l;s[1=2-[r3;lke.,wm.txt').read()        
   num = int(numstring)

def clickedcookie():
   global cookies
   cookies += num
   counter.value = cookies
   save()

def openhome():
   notenoughmoney.hide()
   notenoughmoney.disable()
   counter.show()
   counter.enable()
   cookie.show()
   cookie.enable()
   ymotcp.hide()
   ymotcp.disable()


def tcpc():
   global num
   global cookies
   global tcpcprice
   global tcpc
   global tcpcowned
   if cookies >= 10:
      num = 2
      cookies -= 10
      tcpc.destroy()
      tcpcowned = 1
      f.close()
      counter.value = cookies
      save()
   else:
      notenoughmoney.show()
      notenoughmoney.enable()


def fcpc():
   global fcpc
   global cookies
   global num
   global tcpcowned
   global fcpcowned
   if cookies >= 100 :
     if tcpcowned == 1: 
        num = 4
        cookies -= 120
        fcpc.destroy()
        fcpcowned = 1
        counter.value = cookies
        openhome()
     else:
        ymotcp.enable()
        ymotcp.show()
   else:
     notenoughmoney.show()
     notenoughmoney.enable()


def tncpc():
   global tncpc
   global cookies
   global num
   global tnpcowned
   if cookies >= 10000:
      if tcpcowned == 1:
         num = 10
         cookies -= 10000
         tncpc.destroy()
         tnpcowned = 1
         counter.value = cookies
      else:
         ymotcp.enable()
         ymotcp.show()
   else:
     notenoughmoney.show()
     notenoughmoney.enable()


def ncpc():
   global ncpc
   global cookies
   global num
   global tnpcowned
   if cookies >= 1000000:
      if tnpcowned == 1:
        num = 1
        cookies -= 1000000
        yield 0.1
        self.cookievalue.text = cookies 
      else:
        ymotcp.enable()
        ymotcp.show()
   else:
      yield 0.1
      self.cookievalue.text = "Sorry you cannot buy this"

    
class CookieClicker(toga.App):


   def startup(self):
        try:
           load()
        except:
           reset()
        main_box = toga.Box(style=Pack(direction=COLUMN))
        self.cantbuy = toga.Label(
            "",
            style=Pack(padding=(0, 5))
        )
        self.cookievalue = toga.Label(
            cookies,
            style=Pack(padding=(0, 5))
        )
        cookie = toga.Button(
            "cookie!",
            on_press=self.clickedcookies,
            style=Pack(padding=5)
        )
        name_box = toga.Box(style=Pack(direction=ROW, padding=5))
        name_box.add(self.cookievalue)
        main_box.add(name_box)
        main_box.add(cookie)
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

   def clickedcookies(self, widget):
       global save
       global cookies
       cookies+=num
       yield 0.1
       self.cookievalue.text = cookies
       save()
        
    
def main():
    return CookieClicker()
