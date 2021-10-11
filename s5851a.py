from machine import I2C

p21 = Pin(21,Pin.IN,Pin.PULL_UP)
p22 = Pin(22,Pin.IN,Pin.PULL_UP)
i2c =I2C(scl=Pin(22), sda=Pin(21))

def readU5():
    readtemp = i2c.readfrom_mem(0x48,0,1)
    readtemp = int.from_bytes(readtemp,'little') & 0xFF
    return readtemp

def raw_temp():
    readtemp = readU5()
    T = ( readtemp << 8 | readU5() )>> 4
    return T


temp = raw_temp() * 0.0625
print(temp)