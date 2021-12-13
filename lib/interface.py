from lib.multithreading import VideoWriterWidget
import tkinter as tk
import time

main_win = tk.Tk()
main_win.title("控制面板")
main_win.geometry('400x100') # 寬*高

def start_save():
    VideoWriterWidget.saveFrameflag = True

def end_save():
    VideoWriterWidget.saveFrameflag = False
    # main_win.destroy()

def show_control_panel():
    start_save_btn = tk.Button(main_win, text='開始儲存',width=20, command=start_save).place(x=10, y=10)
    end_save_btn = tk.Button(main_win, text='結束儲存',width=20, command=end_save).place(x=240, y=10)

    prev_frame_btn = tk.Button(main_win, text='<F',width=20, command="").place(x=10, y=50)
    next_frame_btn = tk.Button(main_win, text='F>',width=20, command="").place(x=240, y=50)

    main_win.mainloop()
