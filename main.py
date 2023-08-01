import customtkinter as ctk

root = ctk.CTk()
root._set_appearance_mode("Dark")
root.title("Pathfinder")

gridFrame = ctk.CTkFrame(root)
gridFrame.grid(row=1, column=0)


root.mainloop()