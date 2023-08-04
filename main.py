import customtkinter as ctk

root = ctk.CTk()
root._set_appearance_mode("Dark")
root.title("Pathfinder")

#Create the main grid for the path
gridFrame = ctk.CTkFrame(root)
gridFrame.grid(row=1, column=0)
for row in range(10):
    for column in range(20):
        childFrame = ctk.CTkFrame(gridFrame, fg_color="light blue", width=20, height=20)
        childFrame.grid(row=row, column=column, padx=0.5, pady=0.5)


root.mainloop()