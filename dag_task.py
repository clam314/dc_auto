__author__ = "woods"

import base64
import requests
import time
import logging
from airtest.core.api import *

logger = logging.getLogger("airtest")
logger.setLevel(logging.INFO)

# auto_setup(__file__,devices=["Android://127.0.0.1:5037/emulator-5554"])
# auto_setup(__file__,devices=["Android://192.168.0.106:38409/192.168.0.106:38409"])
# init_device(platform="Android", uuid="88c1ffac")
auto_setup(__file__,devices=["Android:///"])

day_btn = Template(r"tpl1630719218920.png", record_pos=(0.386, 0.578), resolution=(1440, 3200))

spa_btn = Template(r"tpl1630719310446.png", record_pos=(0.206, -0.487), resolution=(1440, 3200))
 

finish_flag = Template(r"tpl1630719349253.png", record_pos=(0.302, -0.557), resolution=(1440, 3200))

activity_btn = Template(r"tpl1630719393940.png", record_pos=(-0.21, 0.892), resolution=(1440, 3200))

devil_rumble = Template(r"tpl1630719474338.png", record_pos=(-0.202, -0.131), resolution=(1440, 3200))


spa1 = Template(r"tpl1630721925719.png", record_pos=(0.069, -0.083), resolution=(1440, 3200))

spa2 = Template(r"tpl1630721949622.png", record_pos=(-0.253, 0.092), resolution=(1440, 3200))

spa3 =Template(r"tpl1630721961516.png", record_pos=(0.327, 0.122), resolution=(1440, 3200))
spa4 = Template(r"tpl1630721969821.png", record_pos=(-0.004, 0.461), resolution=(1440, 3200))

spa_lsit = [spa1,spa2,spa3,spa4]


def finished_spa():
    flags = find_all(finish_flag)
    logger.info(flags)
    if flags and len(flags) > 0:
        for flag in flags:
            if flag.get("result")[1] < 1000:
                return "finish spa"
    return "no finish spa"

            
def spa_task(s):
    touch(s)
    if exists(finish_flag):
        touch(wait(Template(r"tpl1630720567725.png", record_pos=(-0.001, 0.445), resolution=(1440, 3200))))
        sleep(5)
        touch(wait(Template(r"tpl1630720601626.png", record_pos=(0.416, -0.513), resolution=(1440, 3200))))
        sleep(6)
        for i in range(0,5):
            sleep(1)
            if exists(Template(r"tpl1630722474095.png", record_pos=(0.018, -0.333), resolution=(1440, 3200))):
                keyevent("BACK")
                sleep(2)
            touch(wait(Template(r"tpl1630722560332.png", record_pos=(-0.174, 0.742), resolution=(1440, 3200))))
            sleep(2)
            if exists(Template(r"tpl1630722695383.png", record_pos=(-0.004, -0.051), resolution=(1440, 3200))):
                keyevent("BACK")
                sleep(1)
                keyevent("BACK")
                sleep(3)
#             if exists(Template(r"tpl1630815489905.png", record_pos=(0.001, 0.152), resolution=(1440, 3200))):
#                 keyevent("BACK")
#                 sleep(1)

    else:
        keyevent("BACK")
        sleep(3)


def go_spa():
    ff = finished_spa()
    if ff == "finish spa":
        touch(spa_btn)
        sleep(2)
        wait(Template(r"tpl1630721293766.png", record_pos=(0.4, -0.465), resolution=(1440, 3200)))
        sleep(3)
        for s in spa_lsit:
            spa_task(s)
        keyevent("BACK")
        sleep(3)
        go_spa()


def go_activity():
    touch(activity_btn)
    sleep(2)
    touch(Template(r"tpl1630723153028.png", record_pos=(0.4, -0.724), resolution=(1440, 3200)))
    sleep(1)
    touch(Template(r"tpl1630723186057.png", record_pos=(0.184, 0.635), resolution=(1440, 3200)))

go_spa()    
go_activity()


