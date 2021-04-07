import math
import time
import pyautogui
import serial
import struct


def map_val(x2, in_min, in_max, out_min, out_max):
    return (x2 - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


arduinodata = serial.Serial("/dev/ttyACM0", 9600)


def cin(x0, y0, x1, y1, r0, r1):
    d = math.sqrt(x1 ** 2 + y1 ** 2)
    orc = False
    irc = False
    ob = False
    Q2c = math.sqrt(((x1+r0)**2)+((y1-0)**2))
    Q3c = math.sqrt(((x1-0)**2)+((y1-r0)**2))
    Q4c = math.sqrt(((x1-r0)**2)+((y1-0)**2))
    Q1inv = math.sqrt(((x1-0)**2)+((y1-r0)**2))

    if d > r0+r1:
        orc = True
        print("outside of circle")
        an1 = 255
        an2 = 255
        an3 = 255
        return an1, an2, an3;
    if d < r0-r1:
        irc = True
        print("inside of circle")
        an1 = 255
        an2 = 255
        an3 = 255
        return an1, an2, an3;
    if orc or irc:
        ob = True
    if ob == False:
        area = (0.25)*(math.sqrt((d+r0+r1)*(d+r0-r1)*(d-r0+r1)*(-d+r0+r1)))
        apoX = ((x0+x1)/(2))+(((x1-x0)*(r0**2-r1**2))/(2*(d**2)))-(2*(y0-y1)/(d**2)*area)
        x3 = ((x0 + x1) / (2)) + (((x1 - x0) * (r0 ** 2 - r1 ** 2)) / (2 * (d ** 2))) + (2 * (y0 - y1) / (d ** 2) * area)

        y3 = ((y0 + y1) / (2)) + (((y1 - y0) * (r0 ** 2 - r1 ** 2)) / (2 * (d ** 2))) - (2 * (x0 - x1) / (d ** 2) * area)
        bpoY = ((y0 + y1) / (2)) + (((y1 - y0) * (r0 ** 2 - r1 ** 2)) / (2 * (d ** 2))) + (2 * (x0 - x1) / (d ** 2) * area)
        if x1 > 0 and y1 > 0:
          if Q1inv > r1:
            an1 = 180 - math.atan(abs(y3) / abs(x3)) * (180 / math.pi)
            an2 = math.acos((math.pow(r1, 2) + math.pow(r0, 2) - math.pow(d, 2)) / (2 * r0 * r1)) * (180 / math.pi)
            an3 = an1 + math.acos((math.pow(d, 2) + math.pow(r0, 2) - math.pow(r1, 2)) / (2 * r0 * d)) * (
            180 / math.pi) + math.acos((pow(r1, 2) + math.pow(d, 2) - math.pow(r0, 2)) / (2 * r1 * d)) * (
            180 / math.pi)
            print("Q1")
            return an1, an2, an3;
          else:
              an1 = math.atan(abs(y3) / abs(x3)) * (180 / math.pi)
              an2 = math.acos((math.pow(r1, 2) + math.pow(r0, 2) - math.pow(d, 2)) / (2 * r0 * r1)) * (180 / math.pi)
              an3 = an1 + math.acos((math.pow(d, 2) + math.pow(r0, 2) - math.pow(r1, 2)) / (2 * r0 * d)) * (
              180 / math.pi) + math.acos((pow(r1, 2) + math.pow(d, 2) - math.pow(r0, 2)) / (2 * r1 * d)) * (
              180 / math.pi)
              print("Q1")
              return an1, an2, an3;

        if x1 < 0 and y1 > 0:
            if Q2c > r1:
                an1 = math.atan(abs(y3) / abs(x3)) * (180 / math.pi)
                an2 = math.acos((math.pow(r1, 2) + math.pow(r0, 2) - math.pow(d, 2)) / (2 * r0 * r1)) * (180 / math.pi)
                an3 = an1 + math.acos((math.pow(d, 2) + math.pow(r0, 2) - math.pow(r1, 2)) / (2 * r0 * d)) * (
                180 / math.pi) + math.acos((pow(r1, 2) + math.pow(d, 2) - math.pow(r0, 2)) / (2 * r1 * d)) * (
                180 / math.pi)
                print("Q2")
                return an1, an2, an3;
            else:
                print("Q2 out of bounds")
                an1 = 255
                an2 = 255
                an3 = 255
                return an1, an2, an3;
        if x1 < 0 and y1 < 0:
            print("Q3")
            an1 = 255
            an2 = 255
            an3 = 255
            return an1, an2, an3;
        if x1 > 0 and y1 < 0:
            if Q4c < r1:
                an1 = 180 - math.atan(abs(y3) / abs(x3)) * (180 / math.pi)
                an2 = math.acos((math.pow(r1, 2) + math.pow(r0, 2) - math.pow(d, 2)) / (2 * r0 * r1)) * (180 / math.pi)
                an3 = an1 + math.acos((math.pow(d, 2) + math.pow(r0, 2) - math.pow(r1, 2)) / (2 * r0 * d)) * (
                180 / math.pi) + math.acos((pow(r1, 2) + math.pow(d, 2) - math.pow(r0, 2)) / (2 * r1 * d)) * (
                180 / math.pi)
                print("Q4")
                return an1, an2, an3;
            else:
                print("Q4 out of bounds")
                an1 = 255
                an2 = 255
                an3 = 255
                return  an1, an2 , an3;
        if x1 == 0 and y1 > 0:
            an1 = math.atan(abs(y3) / abs(x3)+0.1) * (180 / math.pi)
            an2 = math.acos((math.pow(r1, 2) + math.pow(r0, 2) - math.pow(d, 2)) / (2 * r0 * r1)) * (180 / math.pi)
            an3 = an1 + math.acos((math.pow(d, 2) + math.pow(r0, 2) - math.pow(r1, 2)) / (2 * r0 * d)) * (
            180 / math.pi) + math.acos((pow(r1, 2) + math.pow(d, 2) - math.pow(r0, 2)) / (2 * r1 * d)) * (
            180 / math.pi)
            print("+y")
            return an1, an2, an3;
        if x1 < 0 and y1 == 0:
            print("-x")
            an1 = 255
            an2 = 255
            an3 = 255
            return an1, an2, an3;
        if x1 == 0 and y1 < 0:
            print("-y")
            an1 = 255
            an2 = 255
            an3 = 255
            return an1, an2, an3;
        if x1 > 0 and y1 == 0:
            an1 = 180 - math.atan(abs(y3) / abs(x3)) * (180 / math.pi)
            an2 = math.acos((math.pow(r1, 2) + math.pow(r0, 2) - math.pow(d, 2)) / (2 * r0 * r1)) * (180 / math.pi)
            an3 = an1 + math.acos((math.pow(d, 2) + math.pow(r0, 2) - math.pow(r1, 2)) / (2 * r0 * d)) * (
            180 / math.pi) + math.acos((pow(r1, 2) + math.pow(d, 2) - math.pow(r0, 2)) / (2 * r1 * d)) * (
            180 / math.pi)
            print("+x")
            return an1, an2, an3;



start_time = time.time()
while True:
    if 3>(time.time() - start_time):
     time.sleep(1)
     x1, y1 = pyautogui.position()
     x2 = int(map_val(x1, 610, 1320, -30.9, 30.9))
     y2 = int(map_val(y1, 180, 890, 30.9, -30.9))
     x, y, z = cin(0, 0, x2, y2, 18.3, 12.7)
     z = map_val(z, 0, 360, 0, 254)
     x_, y_, z_ = int(x), int(y), int(z)
     print(str(x2) + "    " + str(y2)+"            "+str(x_) + "    " + str(y_) + "   " + str(z_))
     arduinodata.write(struct.pack('>BBB', x_, y_, z_))
    else:
         time.sleep(0.01)
         x1, y1 = pyautogui.position()
         x2 = int(map_val(x1, 610, 1320, -30.9, 30.9))
         y2 = int(map_val(y1, 180, 890, 30.9, -30.9))
         x, y, z = cin(0, 0, x2, y2, 18.3, 12.7)
         z = map_val(z, 0, 360, 0, 254)
         x_, y_, z_ = int(x), int(y), int(z)
         print(str(x2) + "    " + str(y2) + "            " + str(x_) + "    " + str(y_) + "   " + str(z_))
         arduinodata.write(struct.pack('>BBB', x_, y_, z_))
