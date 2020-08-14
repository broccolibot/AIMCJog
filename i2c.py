from serializer import *
from struct import *
from smbus2 import SMBus


i2c_bus = 0
address = 0x0F

def set_bus(bus_val, address_val):
    i2c_bus = bus_val
    address = address_val


def get():
    with SMBus(i2c_bus) as bus:
        #Read a block of 16 bytes from address 80, offset 0
        block = bytes(bus.read_i2c_block_data(address, 0, 16))
        #Returned value is a list of 16 bytes
        out = unpack("<ffff", block)
        return out


def send_reset():
    with SMBus(i2c_bus) as bus:
        bus.write_block_data(address, 0, bytes(mode_pnumatic()))
    #print("reset")


def send_pid(p, i, d):
    with SMBus(i2c_bus) as bus:
        if p != None:
            bus.write_block_data(address, 0, bytes(set_kp(p)))

        if i != None:
            bus.write_block_data(address, 0, bytes(set_ki(i)))

        if d != None:
            bus.write_block_data(address, 0, bytes(set_kd(d)))


def send_limits(pwm, max, min):
    with SMBus(i2c_bus) as bus:
        if pwm != None:
            bus.write_block_data(address, 0, bytes(limit_pwm(pwm)))

        if max != None:
            bus.write_block_data(address, 0, bytes(limit_target_max(max)))

        if min != None:
            bus.write_block_data(address, 0, bytes(limit_target_min(min)))


def send_enable(state):
    with SMBus(i2c_bus) as bus:
        bus.write_block_data(address, 0, bytes(enable(state)))
    #print(state)


def send_mode_pwm():
    with SMBus(i2c_bus) as bus:
        bus.write_block_data(address, 0, bytes(mode_pwm()))
    #print("pwm")


def send_mode_pid():
    with SMBus(i2c_bus) as bus:
        bus.write_block_data(address, 0, bytes(mode_pid()))
    #print("pid")


def send_mode_pnumatic():
    with SMBus(i2c_bus) as bus:
        bus.write_block_data(address, 0, bytes(mode_pnumatic()))
    #print("pnu")


def send_target(value):
    with SMBus(i2c_bus) as bus:
        bus.write_block_data(address, 0, bytes(set_target(value)))
    #print(value)


def send_homing_speed(value):
    with SMBus(i2c_bus) as bus:
        bus.write_block_data(address, 0, bytes(set_home(value)))
    #print(value)

def send_encoder_pol(value):
    #print(value)
    with SMBus(i2c_bus) as bus:
        bus.write_block_data(address, 0, bytes(encoder_polarity(value)))
    


def send_encoder_polarity(value):
    with SMBus(i2c_bus) as bus:
        bus.write_block_data(address, 0, encoder_polarity(set_home(value)))
    #print(value)
