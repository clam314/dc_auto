# -*- encoding=utf8 -*-
__author__ = "woods"

import base64
import requests
import time
import logging

from airtest.core.api import *

logger = logging.getLogger("airtest")
logger.setLevel(logging.INFO)

# auto_setup(__file__,devices=["Android://127.0.0.1:5037/emulator-5554"])
# auto_setup(__file__,devices=["Android://192.168.0.106:37838/192.168.0.106:37838"])
# init_device(platform="Android", uuid="88c1ffac")
auto_setup(__file__,devices=["Android:///"])

START_TIME = time.time()

start_page = Template(r"tpl1630892352832.png", record_pos=(-0.003, 0.649), resolution=(1440, 3200))

start_page_btn = Template(r"tpl1630891902365.png", record_pos=(0.331, 0.885), resolution=(1440, 3200))

home_page_dialog = Template(r"tpl1630894330652.png", record_pos=(-0.003, -0.97), resolution=(1440, 3200))

img_sr = Template(r"tpl1630416664320.png", record_pos=(0.114, -0.16), resolution=(1920, 1080))
card0 = Template(r"tpl1630778003042.png", threshold=0.9000000000000001, rgb=False, record_pos=(0.374, -0.48),
                 resolution=(1440, 3200))

home_btn = Template(r"tpl1630416962500.png", record_pos=(0.395, 0.035), resolution=(1080, 1920))

list_page = Template(r"tpl1630417399729.png", record_pos=(-0.241, -0.652), rgb=True, resolution=(1080, 1920))

fire_list_header = Template(r"tpl1630643739157.png", record_pos=(0.03, -0.667), resolution=(1440, 3200))

card_add = Template(r"tpl1630777945720.png", record_pos=(0.428, -0.477), resolution=(1440, 3200))

start_fire_btn = Template(r"tpl1630677461148.png", threshold=0.4, rgb=False, record_pos=(0.375, -0.4),
                          resolution=(1440, 3200))

page_status = 0
card_zero = False
error_num = 5
packageName = "com.NextFloor.DestinyChild"


def getImageText(imagePath):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    # 二进制方式打开图片文件
    f = open(imagePath, 'rb')
    params = {"image": base64.b64encode(f.read())}
    access_token = "24.c26374e1930470d248a112256cc9e94f.2592000.1633274618.282335-24798449"
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print(response.json())


def netAgain(try_num=5):
    if try_num < 0:
        try_num = 5
        return
    else:
        try_num = try_num - 1
    if exists(Template(r"tpl1630838602759.png", record_pos=(-0.001, -0.051), resolution=(1440, 3200))):
        touch(Template(r"tpl1630838616881.png", record_pos=(0.19, 0.187), resolution=(1440, 3200)))
        sleep(5)
        netAgain(try_num)
    else:
        return


def tryNet():
    netAgain()


def goList():
    try:
        return wait(Template(r"tpl1630417399729.png", record_pos=(-0.241, -0.652), resolution=(1080, 1920)))
    except Exception as e:
        print(e)
        return False


def isZero():
    return exists(card0)


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
    elif exists(start_fire_btn):
        touch(start_fire_btn)
        sleep(1)
        return 0
    else:
        return 0


def goFire():
    try:
        touch(img_sr)
        sleep(2)
        wait(fire_list_header)
        touch(wait(Template(r"tpl1630418313475.png", record_pos=(-0.008, -0.089), resolution=(1080, 1920))))
        sleep(5)
        touch(wait(start_fire_btn))
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
    elif exists(start_page):
        return -1
    elif exists(home_page_dialog):
        return -2


def error_cal():
    global error_num
    error_num = error_num - 1
    logger.error("错误：%s" % error_num)
    if error_num < 0:
        error_num = 5
        stop_app(packageName)
        sleep(1)
        start_app(packageName)
        logger.error("重启 APP")


while True:
    # 超过5个小时就自动停止
    if time.time() - START_TIME > 60 * 60 * 5:
        logger.info("finish for timeout")
        break
    page_status = getPageStatus()
    if page_status == 0:
        touch(home_btn)
        if goList():
            page_status = 1
            continue
    elif page_status == 1:
        if not isZero():
            result_fire = goFire()
            if result_fire == -1:
                keyevent('BACK')
                sleep(60*5)
                continue
            elif result_fire == "raid over":
                logger.info("FIRE RAID OVER")
                continue
            elif result_fire == 0:
                logger.info("FIRE FINISH")
                sleep(60 * 3)
                continue
            else:
                logger.info("FIRE SLEEP")
                sleep(60 * 10)
        else:
            logger.info("CARD ZERO TO SLEEP")
            sleep(60 * 10)
    elif page_status == -1:
        try:
            touch(wait(start_page_btn, timeout=60))
        except Exception as e:
            logger.error(e)
            error_cal()
    elif page_status == -2:
        keyevent("BACK")
        sleep(3)
        continue
    else:
        error_cal()

logger.info("finish")

