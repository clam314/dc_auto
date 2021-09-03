# -*- encoding=utf8 -*-
__author__ = "woods"

import time
import logging
from airtest.core.api import *

logger = logging.getLogger("airtest")
logger.setLevel(logging.INFO)

# auto_setup(__file__,devices=["Android://127.0.0.1:5037/emulator-5554"])
# auto_setup(__file__,devices=["Android://192.168.0.106:38409/192.168.0.106:38409"])
init_device(platform="Android", uuid="88c1ffac")
# auto_setup(__file__, devices=["Android://127.0.0.1:5073/88c1ffac"])
auto_setup(__file__)

START_TIME = time.time()

img_sr = Template(r"tpl1630416664320.png", record_pos=(0.114, -0.16), resolution=(1920, 1080))
card0 = Template(r"tpl1630416777231.png", threshold=0.95, rgb=True, target_pos=3, record_pos=(0.381, -0.353),
                 resolution=(1080, 1920))
home_btn = Template(r"tpl1630416962500.png", record_pos=(0.395, 0.035), resolution=(1080, 1920))

list_page = Template(r"tpl1630417399729.png", record_pos=(-0.241, -0.652), rgb=True, resolution=(1080, 1920))

fire_list_header = Template(r"tpl1630643739157.png", record_pos=(0.03, -0.667), resolution=(1440, 3200))

card_add = Template(r"tpl1630649378153.png", threshold=0.49999999999999983, rgb=True, record_pos=(0.431, -0.477),
                    resolution=(1440, 3200))

page_status = 0
card_zero = False


def goList():
    try:
        return wait(Template(r"tpl1630417399729.png", record_pos=(-0.241, -0.652), resolution=(1080, 1920)))
    except Exception as e:
        print(e)
        return False


def isZero():
    return exists(card_add)


def noRaid():
    if exists(Template(r"tpl1630422099805.png", threshold=0.95, record_pos=(0.002, -0.092), resolution=(1080, 1920))):
        for i in range(0, 3):
            keyevent("BACK")
            sleep(1)
        logger.info("START BUT CARD ZERO")
        return "card 0"
    elif exists(Template(r"tpl1630422565542.png", record_pos=(-0.015, -0.075), resolution=(1080, 1920))):
        logger.info("START A OVER FIRE")
        keyevent("BACK")
        sleep(1)
        return "raid over"
    else:
        return 0


def goFire():
    try:
        touch(img_sr)
        sleep(2)
        wait(fire_list_header)
        touch(wait(Template(r"tpl1630418313475.png", record_pos=(-0.008, -0.089), resolution=(1080, 1920))))
        sleep(5)
        touch(wait(Template(r"tpl1630418388808.png", record_pos=(0.381, -0.256), resolution=(1080, 1920))))
        sleep(5)
        result_raid = noRaid()
        if result_raid != 0:
            return result_raid
        rdmenu = Template(r"tpl1630421270129.png", record_pos=(0.407, 0.371), resolution=(1080, 1920))
        finish = Template(r"tpl1630418698012.png", record_pos=(-0.002, -0.396), resolution=(1080, 1920))
        logger.info("START FIRE")
        sleep(60 * 3)
        wait(Template(r"tpl1630421845095.png", record_pos=(0.002, 0.364), resolution=(1080, 1920)), 60 * 7)
        if exists(rdmenu):
            touch(rdmenu)
        else:
            touch(finish)
        return 0
    except Exception as e:
        logger.error(e)
        return -1


def getPageStatus():
    if exists(Template(r"tpl1630419199039.png", record_pos=(-0.244, -0.636), resolution=(1080, 1920))):
        return 1
    elif exists(home_btn):
        return 0


while True:
    # 超过5个小时就自动停止
    if time.time() - START_TIME > 60*60*5:
        logger.info("finish for timeout")
        break
    page_status = getPageStatus()
    if page_status == 0:
        touch(home_btn)
        if goList():
            page_status = 1
            continue
    if page_status == 1:
        if not isZero():
            result_fire = goFire()
            if result_fire == -1:
                continue
            elif result_fire == "raid over":
                logger.info("FIRE RAID OVER")
                continue
            elif result_fire == 0:
                logger.info("FIRE FINISH")
                continue
            else:
                logger.info("FIRE SLEEP")
                sleep(60 * 20)
        else:
            logger.info("CARD ZERO TO SLEEP")
            sleep(60 * 15)

logger.info("finish")
