from tkinter import *
import pygame

root = Tk()

#initialize pygame mixer
pygame.mixer.init()

#create playlist box
song_box = Listbox(root, bg="black", fg="green", width=60)
song_box.pack(pady=20)

#define player control button
back_btn_img = PhotoImage(file="back_btn.png")
forward_btn_img = PhotoImage(file="forward_btn.png")
play_btn_img = PhotoImage(file="play_btn.png")
pause_btn_img = PhotoImage(file="pause_btn.png")
stop_btn_img = PhotoImage(file="stop_btn.png")

#create player control frame
controls_frame = Frame(root)
controls_frame.pack()

#create player control buttons
back_button =Button(controls_frame,image=back_btn_img,borderwidth=0,padx=10, pady=10)
forward_button =Button(controls_frame,image=forward_btn_img,borderwidth=0,padx=10, pady=10)
play_button = Button(controls_frame,image=play_btn_img,borderwidth=0,padx=10, pady=10)
pause_button =Button(controls_frame,image=pause_btn_img,borderwidth=0,padx=10, pady=10)
stop_button =Button(controls_frame,image=stop_btn_img,borderwidth=0,padx=10, pady=10)

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1,padx=10)
play_button.grid(row=0, column=2,padx=10)
pause_button.grid(row=0, column=3,padx=10)
stop_button.grid(row=0, column=4,padx=10)

root.mainloop()
