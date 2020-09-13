from tkinter import *

from i2c import *


class HelpWindow:
    def __init__(self, master):
        # create widgets
        self.set_target = Label(master, text="Does nothing yet")
        self.set_stuff = Label(master, text="'change_stuff x': changes stuff")

        # place widgets
        self.set_target.grid(row=0, sticky=W)
        self.set_stuff.grid(row=2, sticky=W)

class InitWindow:
    def __init__(self, master):
        # create widgets
        self.bus_label = Label(master, text="I2C Bus:")
        self.address_label = Label(master, text="Address:")
        self.bus_entry = Entry(master)
        self.address_entry = Entry(master)
        self.submit_button = Button(master, text='Submit', command=self.send_bus)

        # place widgets
        self.bus_label.grid(row=0, sticky=W)
        self.address_label.grid(row=2, sticky=W)
        self.bus_entry.grid(row=0, column=1)
        self.address_entry.grid(row=2, column=1)
        self.submit_button.grid(row=4, column=1)

    def send_bus(self):
        bus_val = int(self.bus_entry.get())
        address_val = hex(int(self.address_entry.get(), 16))
        set_bus(bus_val, address_val)
        




class PidWindow:
    def __init__(self, master):
        # create widgets
        self.p_label = Label(master, text="P:")
        self.i_label = Label(master, text="I:")
        self.d_label = Label(master, text="D:")

        self.p_entry = Entry(master)
        self.i_entry = Entry(master)
        self.d_entry = Entry(master)

        self.submit_button = Button(master, text="Submit", command=self.pid_setup)

        # place widgets
        self.p_label.grid(row=0, sticky=E)
        self.i_label.grid(row=2, sticky=E)
        self.d_label.grid(row=4, sticky=E)

        self.p_entry.grid(row=0, column=1)
        self.i_entry.grid(row=2, column=1)
        self.d_entry.grid(row=4, column=1)

        self.submit_button.grid(row=8, column=1)

    def pid_setup(self):
        try:
            p = float(self.p_entry.get())
        except ValueError:
            p = None

        try:
            i = float(self.i_entry.get())
        except ValueError:
            i = None

        try:
            d = float(self.d_entry.get())
        except ValueError:
            d = None
        send_pid(p, i, d)


class LimitsWindow:
    def __init__(self, master):
        self.pwm_label = Label(master, text="PWM Limit:")
        self.limit_target_max_label = Label(master, text="Target Max Limit:")
        self.limit_target_min_label = Label(master, text="Target Min Limit:")

        self.pwm_entry = Entry(master)
        self.limit_target_max_entry = Entry(master)
        self.limit_target_min_entry = Entry(master)

        self.submit_button = Button(master, text="Submit", command=self.limits_setup)

        self.pwm_label.grid(row=0, sticky=E)
        self.limit_target_max_label.grid(row=2, sticky=E)
        self.limit_target_min_label.grid(row=4, sticky=E)

        self.pwm_entry.grid(row=0, column=1)
        self.limit_target_max_entry.grid(row=2, column=1)
        self.limit_target_min_entry.grid(row=4, column=1)

        self.submit_button.grid(row=8, column=1)

    def limits_setup(self):
        try:
            pwm = int(self.pwm_entry.get()) #+ 2**32
        except ValueError:
            pwm = None

        try:
            max = float(self.limit_target_max_entry.get())
        except ValueError:
            max = None

        try:
            min = float(self.limit_target_min_entry.get())
        except ValueError:
            min = None
        send_limits(pwm, max, min)


class AimcJog:
    def __init__(self, master):
        self.check_state = IntVar()
        self.encoder_text = StringVar()
        self.target_text = StringVar()
        self.pid_out_text = StringVar()
        self.limit_switch_text = StringVar()

        # create widgets
        self.enable_label = Label(master, text="Enable:")
        self.encoder = Label(master, text="Encoder:")
        self.encoder_result = Label(master, textvariable=self.encoder_text)
        self.target = Label(master, text="Target:")
        self.target_result = Label(master, textvariable=self.target_text)
        self.pid_out = Label(master, text="PID Out:")
        self.pid_out_result = Label(master, textvariable=self.pid_out_text)
        self.limit_switch = Label(master, text="Limit Switch:")
        self.limit_switch_result = Label(master, textvariable=self.limit_switch_text)
        self.command_entry_label = Label(master, text="Does Nothing Yet:")
        self.target_entry_label = Label(master, text="Target Position:")
        self.homing_speed_entry_label = Label(master, text="Homing Speed:")
        self.modes_label = Label(master, text="Modes:")
        self.encoder_pol_label = Label(master, text="Encoder Polarity:")

        self.enable_check_box = Checkbutton(
            master,
            variable=self.check_state,
            command=lambda: send_enable(self.check_state.get()),
        )
        self.command_entry = Entry(master)
        self.target_entry = Entry(master)
        self.homing_speed_entry = Entry(master)
        self.encoder_pol_entry = Entry(master)

        self.command_submit_button = Button(master, text="Submit")
        self.target_submit_button = Button(
            master, text="Submit", command=lambda: send_target(self.target_entry.get())
        )
        self.homing_speed_submit_button = Button(
            master,
            text="Submit",
            command=lambda: send_homing_speed(self.homing_speed_entry.get()),
        )
        self.encoder_pol_submit_button = Button(
            master,
            text="Submit",
            command=lambda: send_encoder_pol(self.encoder_pol_entry.get()),
        )
        self.mode_pwm_button = Button(master, text="Mode PWM", command=send_mode_pwm)
        self.mode_pid_button = Button(master, text="Mode PID", command=send_mode_pid)
        self.mode_pnumatic_button = Button(
            master, text="Mode Pnumatic", command=send_mode_pnumatic
        )
        self.help_button = Button(
            master, text="?", command=lambda: self.create_window("Help", HelpWindow)
        )
        self.pid_window_button = Button(
            master,
            text="PID Window",
            command=lambda: self.create_window("PID Window", PidWindow),
        )
        self.limits_window_button = Button(
            master,
            text="Limits Window",
            command=lambda: self.create_window("Limits Window", LimitsWindow),
        )
        self.reset_button = Button(master, text="Reset", command=send_reset)

        # place widgets
        self.enable_label.grid(row=2, sticky=E)
        self.encoder.grid(row=4, sticky=E)
        self.encoder_result.grid(row=4, column=1, sticky=W)
        self.target.grid(row=6, sticky=E)
        self.target_result.grid(row=6, column=1, sticky=W)
        self.pid_out.grid(row=8, sticky=E)
        self.pid_out_result.grid(row=8, column=1, sticky=W)
        self.limit_switch.grid(row=10, sticky=E)
        self.limit_switch_result.grid(row=10, column=1, sticky=W)
        self.command_entry_label.grid(row=22, sticky=E)
        self.target_entry_label.grid(row=16, sticky=E)
        self.homing_speed_entry_label.grid(row=18, sticky=E)
        self.modes_label.grid(row=12, sticky=E)
        self.encoder_pol_label.grid(row=20, sticky=E)

        self.enable_check_box.grid(row=2, column=1, sticky=W)
        self.command_entry.grid(row=22, column=1)
        self.target_entry.grid(row=16, column=1)
        self.homing_speed_entry.grid(row=18, column=1)
        self.encoder_pol_entry.grid(row=20, column=1)

        self.command_submit_button.grid(row=22, column=2, sticky=W)
        self.target_submit_button.grid(row=16, column=2, sticky=W)
        self.homing_speed_submit_button.grid(row=18, column=2, sticky=W)
        self.encoder_pol_submit_button.grid(row=20, column=2, sticky=W)
        self.help_button.grid(row=22, column=3)
        self.pid_window_button.grid(row=0, column=1)
        self.limits_window_button.grid(row=0, column=2)
        self.reset_button.grid(row=14, column=1, sticky=W)
        self.mode_pwm_button.grid(row=12, column=1)
        self.mode_pid_button.grid(row=12, column=2)
        self.mode_pnumatic_button.grid(row=12, column=3)

        self.create_window("Address Select", InitWindow)

    def create_window(self, name, type):
        self.root = Tk()
        self.window = type(self.root)
        self.root.title(name)


root = Tk()
root.title("AIMC_Jog")
window = AimcJog(root)


def load_get():
    output = get()
    window.encoder_text.set(output[0])
    window.target_text.set(output[1])
    window.pid_out_text.set(output[2])
    window.limit_switch_text.set(output[3])

    root.after(1000, load_get)


root.after(1000, load_get)
root.mainloop()