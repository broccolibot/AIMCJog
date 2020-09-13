from serializer import *
from struct import *
from smbus2 import SMBus, i2c_msg


i2c_bus = 0
address = 0x0f

def set_bus(bus_val, address_val):
    i2c_bus = bus_val
    address = address_val
    print(i2c_bus, address)

def get():
    with SMBus(i2c_bus) as bus:
        block = bytes(bus.read_i2c_block_data(address, 1, 16))
        out = unpack("<ffff", block)
        return out


def send_reset():
    with SMBus(i2c_bus) as bus:
        msg = i2c_msg.write(address, reset())
        bus.i2c_rdwr(msg)


def send_pid(p, i, d):
    with SMBus(i2c_bus) as bus:
        if p != None:
            #bus.write_block_data(address, 0, bytes(set_kp(p)))
            msg = i2c_msg.write(address, set_kp(p))
            bus.i2c_rdwr(msg)

        if i != None:
            msg = i2c_msg.write(address, set_ki(i))
            bus.i2c_rdwr(msg)

        if d != None:
            msg = i2c_msg.write(address, set_kd(d))
            bus.i2c_rdwr(msg)


def send_limits(pwm, max, min):
    print(pwm)
    with SMBus(i2c_bus) as bus:
        if pwm != None:
            msg = i2c_msg.write(address, limit_pwm(pwm))
            bus.i2c_rdwr(msg)

        if max != None:
            msg = i2c_msg.write(address, limit_target_max(max))
            bus.i2c_rdwr(msg)

        if min != None:
            msg = i2c_msg.write(address, limit_target_min(min))
            bus.i2c_rdwr(msg)


def send_enable(state):
    with SMBus(i2c_bus) as bus:
        msg = i2c_msg.write(address, enable(state))
        bus.i2c_rdwr(msg)


def send_mode_pwm():
    with SMBus(i2c_bus) as bus:
        msg = i2c_msg.write(address, mode_pwm())
        bus.i2c_rdwr(msg)


def send_mode_pid():
    with SMBus(i2c_bus) as bus:
        msg = i2c_msg.write(address, mode_pid())
        bus.i2c_rdwr(msg)


def send_mode_pnumatic():
    with SMBus(i2c_bus) as bus:
        msg = i2c_msg.write(address, mode_pnumatic())
        bus.i2c_rdwr(msg)


def send_target(value):
    with SMBus(i2c_bus) as bus:
        msg = i2c_msg.write(address, set_target(value))
        bus.i2c_rdwr(msg)
    

def send_homing_speed(value):
    with SMBus(i2c_bus) as bus:
        msg = i2c_msg.write(address, set_home(value))
        bus.i2c_rdwr(msg)
    

def send_encoder_pol(value):
    with SMBus(i2c_bus) as bus:
        msg = i2c_msg.write(address, encoder_polarity(value))
        bus.i2c_rdwr(msg)
