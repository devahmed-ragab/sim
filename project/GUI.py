import tkinter as tk
from tkinter import ttk, scrolledtext
from tkinter import Menu
import threading
from tkinter import messagebox as msg
import __init__ as app
from __init__ import home

win = tk.Tk()
counter = 1


def _quit():
    tap1.quit()
    tap1.destroy()
    exit()


def start_button():
    global counter
    startButton.configure(text="calculating")
    startButton.config(state="disabled")
    stop_action.config(state="enabled")
    if enterStaring.get() != "":
        gui_total_wattage = int(enterStaring.get())
        home.set_total_wattage(gui_total_wattage)
    elif counter == 1:
        gui_total_wattage = home.init_random_home()
        counter += 1
        home.set_total_wattage(gui_total_wattage)
    t = threading.Thread(target=app.main)
    t2 = threading.Thread(target=run_progressbar)
    home.run = True
    t.start()
    t2.start()
    Refresh_text()


def stop_button():
    stop_action.configure(text="Stop")
    stop_action.config(state="disabled")
    startButton.config(state="enabled")
    home.run = False
    Refresh_text()
    stop_progressbar()


def Refresher():
    # todo add hours function
    hours = 0
    min = app.minutes
    if app.minutes % 60 == 0:
        ++hours
        min = 0
    output_frame.configure(text="{} : {} : {}".format(hours, min, int(app.seconds)))
    total_watt_label.configure(text="{} Watt".format(home.total_wattage))
    units_label.configure(text="{} KWH".format(home.getUnits()))
    bill_label.configure(text="{}  EGP".format(home.getBill()))
    output_frame.after(1000, Refresher)  # every second...


def Refresh_text():
    scrol_on.insert(tk.INSERT, home.show_running_devices())
    scrol_off.insert(tk.INSERT, home.show_of_devices())


def increase():
    msg.ABORT


def run_progressbar():
    progress_bar["maximum"] = 60
    while True:
        i = app.seconds
        progress_bar["value"] = i  # increment progressbar
        progress_bar.update()  # have to call update() in loop
    progress_bar["value"] = 0  # reset/clear progressbar


def stop_progressbar():
    progress_bar.stop()


def create_window():
    window = tk.Toplevel(win)
    window.geometry("300x200")
    lap = ttk.Label(window, text="Increase total wattage :")
    lap.grid(column=0, row=1, pady=10, padx=5)

    inc_wattage = tk.IntVar()
    enterWidget = tk.Entry(window, width=12, textvariable=inc_wattage)
    enterWidget.grid(column=0, row=2, sticky="W", padx=10)
    n=inc_wattage.get()
    incButton = ttk.Button(window, text="Increase", command=home.increase_wattage(n))
    incButton.grid(column=1, row=2, )


# creating menu bar
main_bar = Menu(win)
win.configure(menu=main_bar)
win.iconbitmap('logo.ico')

# add menu items
file_menu = Menu(main_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=_quit)
file_menu.add_separator()
main_bar.add_cascade(label="File!", menu=file_menu)

# add another menu items
help_menu = Menu(main_bar, tearoff=0)
help_menu.add_command(label="About")
main_bar.add_cascade(label="Help", menu=help_menu)
# tap
tapControl = ttk.Notebook(win)
# tap control
tap1 = ttk.Frame(tapControl)
# create tap
tapControl.add(tap1, text="Configure")
# add tap
tap2 = ttk.Frame(tapControl)
tapControl.add(tap2, text="Reads")
tapControl.pack(expand=1, fill="both")
# show app taps

# Add a title
win.title("Demo Electric Meter Simulator")
main_frame = ttk.LabelFrame(tap1, )
main_frame.grid(column=0, row=0, sticky="W")

a_label = ttk.Label(main_frame, text="Enter total wattage :")
a_label.grid(column=0, row=0, sticky="W", padx=10, pady=3)

enterStaring = tk.StringVar()
enterWidget = tk.Entry(main_frame, width=12, textvariable=enterStaring)
enterWidget.grid(column=0, row=1, sticky="W", padx=10)
var = tk.IntVar()

# Displaying it

# ------------------------------------------------------------------------------------
startButton = ttk.Button(main_frame, text="Start", command=start_button)
startButton.grid(column=1, row=1, )

stop_action = ttk.Button(main_frame, text="Stop", command=stop_button)
stop_action.grid(column=2, row=1, )

# ------------------------------------------------------------------------------------

control_buttons_frame = ttk.LabelFrame(tap1, text="Controls")
control_buttons_frame.grid(column=0, row=3, padx=0, pady=10, sticky="W")

add_appliance_B = ttk.Button(control_buttons_frame, text="Add", command=create_window)
add_appliance_B.grid(column=0, row=0, sticky="W", padx=10)
turn_on_B = ttk.Button(control_buttons_frame, text="Turn ON", command=create_window)
turn_on_B.grid(column=1, row=0, padx=10)
turn_off_B = ttk.Button(control_buttons_frame, text="Turn OFF", command=create_window)
turn_off_B.grid(column=2, row=0, )
increase_B = ttk.Button(control_buttons_frame, text="Increase", command=create_window)

increase_B.grid(column=3, row=0, padx=10)
decrease_B = ttk.Button(control_buttons_frame, text="Decrease", command=create_window)
decrease_B.grid(column=4, row=0, )

# ------------------------------------------------------------------------------------
devices_frame = ttk.LabelFrame(tap1, )
devices_frame.grid(column=0, row=2, padx=0, pady=10)

runLabel = ttk.Label(devices_frame, text="ON Appliance")
runLabel.grid(column=0, row=0, )
runLabelOff = ttk.Label(devices_frame, text="OFF Appliance")
runLabelOff.grid(column=3, row=0)

scrol_w = 30
scrol_h = 3
scrol_on = scrolledtext.ScrolledText(
    devices_frame, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scrol_on.grid(column=0, row=1, sticky='W', columnspan=3, padx=10, pady=5)

scrol_off = scrolledtext.ScrolledText(
    devices_frame, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scrol_off.grid(column=3, row=1, sticky='E', columnspan=3)

# ----------------------------------------------------------------------------
output_frame = ttk.LabelFrame(tap2, )
output_frame.grid(column=0, row=2, padx=(150, 40), pady=(100, 10), sticky="WE", )

a_label = ttk.Label(output_frame, text=" Total wattage : ", font=("Times", 20))
a_label.grid(column=0, row=3, sticky="W")
total_watt_label = ttk.Label(output_frame, text=home.total_wattage)
total_watt_label.grid(column=1, row=3, sticky="W")

a_label2 = ttk.Label(output_frame, text="consumption : ", font=("Times", 20))
a_label2.grid(column=0, row=4)
units_label = ttk.Label(output_frame, text="", )
units_label.grid(column=1, row=4)

a_label4 = ttk.Label(output_frame, text="bill : ", font=("Times", 20))
a_label4.grid(column=0, row=5, )
bill_label = ttk.Label(output_frame, text="")
bill_label.grid(column=1, row=5, )

prog_label = ttk.LabelFrame(tap2, )
prog_label.grid(column=0, row=4, pady=3, padx=(110, 0))

progress_bar = ttk.Progressbar(
    prog_label, orient='horizontal', length=286, mode='determinate')
progress_bar.grid(column=0, row=0)

# ------------------------------------------------------------------------------------


win.resizable(False, False)
# Start GUI

Refresher()
tap1.mainloop()
