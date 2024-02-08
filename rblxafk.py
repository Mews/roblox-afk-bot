from win32gui import GetWindowText, GetForegroundWindow
import tkinter as tk
import keyboard as kb
import random as rand
from time import sleep as wait

INPUTS = ["w", "a", "s", "d", "space"]

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("300x100+100+100")
        self.title("Roblox afk bot")

        self.enabled = False

        self.activeLabel = tk.Label(self, font=("Cascadia Code", 15), text="Bot is disabled!", foreground="red")
        self.activeLabel.pack(pady=(10,0))

        self.toggleButton = tk.Button(self, text="Enable!", foreground="green", font=("Cascadia Code", 8), command=self.toggle)
        self.toggleButton.pack(pady=5)

        self.loop()


    def loop(self):
        if self.enabled:
            activeWindow = GetWindowText(GetForegroundWindow())

            if activeWindow == "Roblox":
                self.activeLabel.config(text="Bot is running!", foreground="green")
                
                inp = rand.choice(INPUTS)

                action = "q+"+inp

                kb.press(action)
                wait(0.5)
                kb.release(action)

            else:
                self.activeLabel.config(text="Bot is not running!", foreground="red")

        self.after(1000, self.loop)


    def toggle(self):
        if self.enabled:
            self.toggleButton.config(text="Enable!", foreground="green")
            self.activeLabel.config(text="Bot is disabled!", foreground="red")
        else:
            self.toggleButton.config(text="Disable!", foreground="red")
            self.activeLabel.config(text="Bot is not running!", foreground="red")

        self.enabled = not self.enabled


if __name__ == "__main__":
    App().mainloop()