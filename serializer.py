import struct


def enable(value): 
    if value:
        return struct.pack("<BI", 1, 1)
    else:
        return struct.pack("<BI", 1, 0)


def set_target(value):  
    return struct.pack("<Bf", 2, float(value))


def reset():  
    return struct.pack("<BI", 3, 0)


def mode_pwm(): 
    return struct.pack("<BI", 4, 0)


def mode_pid():  
    return struct.pack("<BI", 5, 0)


def mode_pnumatic():  
    return struct.pack("<BI", 6, 0)


def set_kp(value):  
    return struct.pack("<Bf", 7, float(value))


def set_ki(value):  
    return struct.pack("<Bf", 8, float(value))


def set_kd(value):  
    return struct.pack("<Bf", 9, float(value))


def set_home(value):  
    return struct.pack("<Bi", 10, int(value))


def limit_pwm(value):  
    return struct.pack("<BI", 11, int(value)) #+ 2**32


def limit_target_min(value):  
    return struct.pack("<Bf", 12, float(value))


def limit_target_max(value):  
    return struct.pack("<Bf", 13, float(value))


def encoder_polarity(value):
    return struct.pack("<BI", 14, int(value)) #+ 2**32

