import tkinter as tk
from tkinter import ttk, scrolledtext
from tkinter import Menu
import threading
from tkinter import messagebox as msg
import __init__ as app
from __init__ import home


class GUI:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Demo Electric Meter Simulator")
        self.win.resizable(False, False)
        self.tap_control = ttk.Notebook(self.win)
        self.tap_control.pack(expand=1, fill="both")
        self.total_wattage_input = tk.StringVar()
        self.configure_tap()
        self.reads_tap()
        self.p_bar()
        self.bool = True
        self.refresher()

    def create_window(self):
        window = tk.Toplevel(self.win)
        window.geometry("300x200")
        lap = ttk.Label(window, text="Increase total wattage :")
        lap.grid(column=0, row=1, pady=10, padx=5)

        inc_wattage = tk.IntVar()
        enterWidget = tk.Entry(window, width=12, textvariable=inc_wattage)
        enterWidget.grid(column=0, row=2, sticky="W", padx=10)
        n = inc_wattage.get()
        incButton = ttk.Button(window, text="Increase", command=home.increase_wattage(n))
        incButton.grid(column=1, row=2, )

    def start_button_fun(self):
        self.start_button.configure(text="calculating")
        self.start_button.config(state="disabled")
        self.stop_button.config(state="enabled")

        if self.total_wattage_input.get() != "":
            wattage = int(self.total_wattage_input.get())
        elif self.bool:
            self.bool = False
            wattage = home.init_random_home()
            self.total_wattage_input.set(wattage)
            self.Refresh_text()

        home.set_total_wattage(wattage)
        self.start_threads()
        self.run_progressbar()

    def stop_button_fun(self):
        self.stop_button.configure(text="Stop")
        self.stop_button.config(state="disabled")
        self.start_button.config(state="enabled")
        home.run = False
        self.progress_bar.stop()

    def refresher(self):
        # todo add hours function
        hours = 0
        min = app.minutes
        if app.minutes % 60 == 0:
            ++hours
            min = 0
        # self.reads_tap_frame.configure(text="{} : {} : {}".format(hours, min, int(app.seconds)))
        self.total_watt_label.configure(text="{} Watt".format(home.total_wattage))
        self.units_label.configure(text="{} KWH".format(home.getUnits()))
        self.bill_label.configure(text="{}  EGP".format(home.getBill()))
        self.reads_tap_frame.after(1000, self.refresher)  # every second...

    def Refresh_text(self):
        self.scrol_on.insert(tk.INSERT, home.show_running_devices())
        self.scrol_off.insert(tk.INSERT, home.show_of_devices())

    def start_threads(self):
        t = threading.Thread(target=app.main)
        t2 = threading.Thread(target=self.run_progressbar)
        home.run = True
        t.start()
        t2.start()

    def configure_tap(self):
        configure_tap = ttk.Frame(self.tap_control)
        self.tap_control.add(configure_tap, text='Configure')

        main_frame = ttk.LabelFrame(configure_tap)
        main_frame.grid(column=0, row=0, sticky="W")

        a_label = ttk.Label(main_frame, text="Enter total wattage :")
        a_label.grid(column=0, row=0, sticky="W", padx=10, pady=3)

        # todo create function that creates lapels and buttons
        enterWidget = tk.Entry(main_frame, width=12, textvariable=self.total_wattage_input)
        enterWidget.grid(column=0, row=1, sticky="W", padx=10)

        self.start_button = ttk.Button(main_frame, text="Start", command=self.start_button_fun)
        self.start_button.grid(column=1, row=1, )

        self.stop_button = ttk.Button(main_frame, text="Stop", command=self.stop_button_fun)
        self.stop_button.grid(column=2, row=1, )

        # todo trry to put conttrol_b_frame in main_frame
        control_buttons_frame = ttk.LabelFrame(configure_tap, text="Controls")
        control_buttons_frame.grid(column=0, row=3, padx=0, pady=10, sticky="W")

        add_appliance_B = ttk.Button(control_buttons_frame, text="Add", command=self.create_window)
        add_appliance_B.grid(column=0, row=0, sticky="W", padx=10)

        turn_on_B = ttk.Button(control_buttons_frame, text="Turn ON", command=self.create_window)
        turn_on_B.grid(column=1, row=0, padx=10)

        turn_off_B = ttk.Button(control_buttons_frame, text="Turn OFF", command=self.create_window)
        turn_off_B.grid(column=2, row=0, )

        increase_B = ttk.Button(control_buttons_frame, text="Increase", command=self.create_window)
        increase_B.grid(column=3, row=0, padx=10)

        decrease_B = ttk.Button(control_buttons_frame, text="Decrease", command=self.create_window)
        decrease_B.grid(column=4, row=0, )

        # todo check also devices_frame
        devices_frame = ttk.LabelFrame(configure_tap)
        devices_frame.grid(column=0, row=2, padx=0, pady=10)

        runLabel = ttk.Label(devices_frame, text="ON Appliance")
        runLabel.grid(column=0, row=0, )

        runLabelOff = ttk.Label(devices_frame, text="OFF Appliance")
        runLabelOff.grid(column=3, row=0)

        # todo customize this
        scrol_w = 30
        scrol_h = 3

        self.scrol_on = scrolledtext.ScrolledText(devices_frame, width=scrol_w,
                                                  height=scrol_h, wrap=tk.WORD)
        self.scrol_on.grid(column=0, row=1, sticky='W', columnspan=3, padx=10, pady=5)

        self.scrol_off = scrolledtext.ScrolledText(devices_frame, width=scrol_w,
                                                   height=scrol_h, wrap=tk.WORD)
        self.scrol_off.grid(column=3, row=1, sticky='E', columnspan=3)

    def reads_tap(self):
        self.reads_tap_frame = ttk.Frame(self.tap_control)
        self.tap_control.add(self.reads_tap_frame, text='Reads')

        output_frame = ttk.LabelFrame(self.reads_tap_frame)
        output_frame.grid(column=0, row=2, padx=(150, 40), pady=(100, 10), sticky="WE", )

        a_label = ttk.Label(output_frame, text=" Total wattage : ", font=("Times", 20))
        a_label.grid(column=0, row=3, sticky="W")

        a_label2 = ttk.Label(output_frame, text="consumption : ", font=("Times", 20))
        a_label2.grid(column=0, row=4)

        a_label4 = ttk.Label(output_frame, text="bill : ", font=("Times", 20))
        a_label4.grid(column=0, row=5, )

        self.total_watt_label = ttk.Label(output_frame, text=home.total_wattage)
        self.total_watt_label.grid(column=1, row=3, sticky="W")

        self.units_label = ttk.Label(output_frame, text=home.units, )
        self.units_label.grid(column=1, row=4)

        self.bill_label = ttk.Label(output_frame, text=home.bill)
        self.bill_label.grid(column=1, row=5, )

    def run_progressbar(self):
        self.progress_bar["maximum"] = 60
        while True:
            i = app.seconds
            self.progress_bar["value"] = i  # increment progressbar
            self.progress_bar.update()  # have to call update() in loop
        progress_bar["value"] = 0  # reset/clear progressbar

    def p_bar(self):
        prog_label = ttk.LabelFrame(self.reads_tap_frame)
        prog_label.grid(column=0, row=4, pady=3, padx=(110, 0))

        self.progress_bar = ttk.Progressbar(prog_label,
                                            orient='horizontal',
                                            length=286,
                                            mode='determinate')
        self.progress_bar.grid(column=0, row=0)


oop = GUI()
oop.win.mainloop(0)
