# -*- encoding=utf8 -*-
__author__ = "woods"

from airtest.core.api import *
# auto_setup(__file__,devices=["Android://127.0.0.1:5037/emulator-5554"])
# connect_device("Android://192.168.0.106:41523/192.168.0.106:41523")
# init_device(platform="Android",uuid="192.168.0.106:41523")
auto_setup(__file__,devices=["Android:///"])

    
img_sr = Template(r"tpl1630416664320.png", record_pos=(0.114, -0.16), resolution=(1920, 1080))
card0 = Template(r"tpl1630416777231.png", threshold=0.95, rgb=True, target_pos=3, record_pos=(0.381, -0.353), resolution=(1080, 1920))
home_btn = Template(r"tpl1630416962500.png", record_pos=(0.395, 0.035), resolution=(1080, 1920))

list_page = Template(r"tpl1630417399729.png", record_pos=(-0.241, -0.652), resolution=(1080, 1920))

page_status = 0
card_zero = False


def goList():
    try:
        return wait(Template(r"tpl1630417399729.png", record_pos=(-0.241, -0.652), resolution=(1080, 1920)))
    except Exception:
        return False

def isZero():
    return exists(card0)

def noRaid():
    if exists(Template(r"tpl1630422099805.png", record_pos=(0.002, -0.092), resolution=(1080, 1920))):
        touch(Template(r"tpl1630422130088.png", record_pos=(-0.005, 0.123), resolution=(1080, 1920)))
        sleep(2)
        touch(Template(r"tpl1630422193402.png", record_pos=(0.421, -0.826), resolution=(1080, 1920)))
        sleep(10)
        touch(wait(Template(r"tpl1630422290265.png", record_pos=(-0.001, 0.681), resolution=(1080, 1920))))
        return True
    elif exists(Template(r"tpl1630422565542.png", record_pos=(-0.015, -0.075), resolution=(1080, 1920))):
        touch(Template(r"tpl1630422130088.png", record_pos=(-0.005, 0.123), resolution=(1080, 1920)))
        return True
    else:
        return False
    


def goFire():
    try:
        touch(img_sr)
        sleep(2)
        touch(wait(Template(r"tpl1630418313475.png", record_pos=(-0.008, -0.089), resolution=(1080, 1920))))
        sleep(5)
        touch(wait(Template(r"tpl1630418388808.png", record_pos=(0.381, -0.256), resolution=(1080, 1920))))
        sleep(5)
        if noRaid():
            return False
        rdmenu = Template(r"tpl1630421270129.png", record_pos=(0.407, 0.371), resolution=(1080, 1920))
        finish = Template(r"tpl1630418698012.png", record_pos=(-0.002, -0.396), resolution=(1080, 1920))
        sleep(60*3)
        wait(Template(r"tpl1630421845095.png", record_pos=(0.002, 0.364), resolution=(1080, 1920)),60*7)
        if exists(rdmenu):
            touch(rdmenu)
        else:
            touch(finish)
        return True
    except Exception:
        return False
    
def getPageStatus():
    if exists(Template(r"tpl1630419199039.png", record_pos=(-0.244, -0.636), resolution=(1080, 1920))):
        return 1
    elif exists(home_btn):
        return 0

    
while True:
    page_status = getPageStatus()
    if page_status == 0:
        touch(home_btn)
        if(goList):
            page_status = 1
            continue
    if page_status == 1:
        card_num = isZero
        if card_num:
            if not goFire():
                sleep(60*20)
        else:
            sleep(60*15)
            
        
        

