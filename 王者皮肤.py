import requests
import random
import json
import re
import time


def camouflage_browser():
    ur1 = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE/10.0.2410.0'
    ur_list = ur1

    headers = {
        'user-agent': random.choice(ur_list)
    }
    return headers


def get_id():
    id_list = []
    id_url = 'https://pvp.qq.com/web201605/js/herolist.json'
    id_str = requests.get(id_url, camouflage_browser())
    dict_id = json.loads(id_str.text)
    for ename in dict_id:
        id = ename["ename"]
        name = ename["cname"]
        id_list.append({"name": name, "id": id})
    return id_list


def visit_hero_url():
    id_list = get_id()
    for hero_id in id_list:
        hero_url = "https://pvp.qq.com/web201605/herodetail/{}.shtml".format(hero_id["id"])
        print("The url of " + hero_id["name"] + " is " + hero_url)
        html = requests.get(hero_url, camouflage_browser())
        pattern = 'pic-pf-list pic-pf-list3" data-imgname=(.*?)>'
        skins = re.findall(pattern, html.content.decode("gbk"))[0]
        skins = re.sub("&|[0-9]{0,5}|\"", "", skins)
        for index, name in enumerate(skins.split("|")):
            print(index, name)
            download_skin(hero_id["id"], index + 1, name)


def download_skin(hero_id, index, name):
    # The URL of the hero skin
    skin_url = 'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{}/{}-bigskin-{}.jpg'.format(hero_id, hero_id,
                                                                                                       index)
    print("The url of skin is " + skin_url)
    pic_html = requests.get(skin_url, camouflage_browser())
    time.sleep(0.5)
    with open(name + ".jpg", "wb") as f:
        f.write(pic_html.content)


if __name__ == '__main__':
    visit_hero_url()
