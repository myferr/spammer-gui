import customtkinter as ctk
import tkinter as tk
import spam
import time

# Sets the appearance of the window
# Supported modes : Light, Dark, System
# "System" sets the appearance mode to 
# the appearance mode of the system
ctk.set_appearance_mode("dark")   
 
# Sets the color of the widgets in the window
# Supported themes : green, dark-blue, blue    
ctk.set_default_color_theme("green")    
 
# Dimensions of the window
appWidth, appHeight = 400, 250
 
 
# App Class
class App(ctk.CTk):
    # The layout of the window will be written
    # in the init function itself
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
 
        self.title("Spammer GUI")   
        self.geometry(f"{appWidth}x{appHeight}")
        self.resizable(0, 0)
 
        # Name Label
        self.nameLabel = ctk.CTkLabel(self,
                                text="")
        self.nameLabel.grid(row=0, column=0,
                            padx=20, pady=20,
                            sticky="ew")
 
        # Name Entry Field
        self.nameEntry = ctk.CTkEntry(self,
                          placeholder_text="Message..")
        self.nameEntry.grid(row=0, column=1,
                            columnspan=3, padx=20,
                            pady=20, sticky="ew")
 
        # Age Label
        self.ageLabel = ctk.CTkLabel(self, text="How many messages?")
        self.ageLabel.grid(row=1, column=0,
                           padx=20, pady=20,
                           sticky="ew")
 
        # Age Entry Field
        self.ageEntry = ctk.CTkEntry(self,
                            placeholder_text="18")
        self.ageEntry.grid(row=1, column=1,
                           columnspan=3, padx=20,
                           pady=20, sticky="ew")
        # Generate Button
        self.generateResultsButton = ctk.CTkButton(self,
                                         text="Run",
                                         command=self.generateResults)
        self.generateResultsButton.grid(row=5, column=1,
                                        columnspan=2, padx=20, 
                                        pady=20, sticky="ew")
 

 
    # This function is used to insert the 
    # details entered by users into the textbox
    def generateResults(self):
 
        # Constructing the text variable
        print(f"{self.nameEntry.get()} : {self.ageEntry.get()}")
        time.sleep(3)
        spam.send(int(self.ageEntry.get()), self.nameEntry.get())


if __name__ == "__main__":
    app = App()
    # Used to run the application
    app.mainloop()   