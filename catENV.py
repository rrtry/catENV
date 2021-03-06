
#
# catENV Defintions: HostToIp, percent, deunix, Geocode, translate, input, RandomInt, PlusWrite, Get, ShortUrl, InstallPackage, ReadFF, CallSystem, Run,
# Download, Similar, CreateFile, Reverse, RandomLetter, writeTo, resize_image, convertint
# ВНИМАНИЕ. код не тестировался потому что мне лень
#

#
# Contributors:
#
# Catinka (convertint) - визитная карточка https://vk.com/catinkastep
#

import os
import datetime
import shutil
from PIL import Image, ImageDraw, ImageFont
import random as randd
from random import random
import requests
from requests import get, post, Session
import time
session = requests.Session()
import sys
from googletrans import Translator
translator = Translator()

def convertint(uptime): # Converting seconds to verbal notation, by Catware & Catinka
    seconds = int(uptime);
    minutes = int(uptime / 60);
    hours = int(minutes / 60);
    days = int(hours / 24);
    hours = int(hours - days * 24);
    minutes = int(minutes - (hours * 60 + days * 24 * 60));
    return str(days) + ' дней ' + str(hours) + ' часов ' + str(minutes) + ' минут ' 

def HostToIp(host):
    return gethostbyname(host)

def percent(frst, scnd):
    coef = 100 / frst
    gets = scnd * coef
    return gets

def deunix(integer):
    return datetime.datetime.utcfromtimestamp(integer).strftime('%Y %m %d %H %M %S').split(" ")

def Geocode(address):
    address = address.replace(" ", "+")
    json1 = convertjson(Get("https://nominatim.openstreetmap.org/search?q="+ address + "&format=geojson"))
    json2 = json1["features"][0]["geometry"]["coordinates"]
    f1 = json2[0]
    f2 = json2[1]
    json2 = [f2, f1]
    json3 = json1["features"][0]["properties"]["display_name"]
    json2.append(json3)
    return json2

def translate(text, lang):
    result = translator.translate(text, dest = str(lang))
    return result.text

def RandomInt(first, second):
    return randd.randint(first, second)

def PlusWrite(text, target):
    file = open(str(target), 'a', encoding='utf-8')
    file.write(str(text))
    file.close()

def Get(url): # A get requests
    try:
        return get(url).text
        log("Issued Get() with URL {}".format(url))
    except Exception as e:
        log("Error in Get(). " + str(e))
        return None

def ShortUrl(url):
    return Get("https://clck.ru/--?url=" + url)

def InstallPackage(text): # Install Python Package (PIP)
    a = CallSystem("pip install " + str(text) + ' --user')
    if 'error' not in str(a).lower():
        return 'success'
    else:
        return 'error'

def ReadFF(file): # Read From File
    try:
        Ff = open(file, 'r', encoding='UTF-8')
        Contents = Ff.read()
        Ff.close()
        return Contents
    except:
        return None

def CallSystem(command): # Call system shell
    return str(check_output(str(command), shell=False))

def Run(file): # Запустить питоновский скрипт в рамках DEFa (а нахуя это кстати я не знаю.)
    exec(ReadFF(str(file)))

def Download(url, fn): # Download a file from any URL
    f = open(fn, 'wb')
    f.write(get(url).content)
    f.close()

def Similar(first, second): # Similar strings
    if not len(first) == len(second):
        return False
    if len(first) - sum(l1==l2 for l1, l2 in zip(first, second)) > 3:
        return False
    return True

def TextToBits(text, encoding='utf-8', errors='surrogatepass'): # Text to 101010010100101
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def TextFromBits(bits, encoding='utf-8', errors='surrogatepass'): # Text from 10101001010101
    try:
        n = int(bits, 2)
        return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
    except Exception:
        return 'error'

def CreateFile(name): # Create a file
    k = name
    f = open(str(k), 'w')
    f.close()

def Reverse(s): # Reverse text (Text -> txeT)
    return s[::-1]

def RandomLetter():
    letters = ['q', 'Q', 'w', 'W', 'e', 'E', 'r', 'R', 't', 'T', 'y', 'Y', 'u', 'U', 'i', 'I', 'o', 'O', 'p', 'P', 'a', 'A', 's', 'S', 'd', 'D', 'f', 'F', 'g', 'G', 'h', 'H', 'j', 'J', 'k', 'K', 'l', 'L', 'z', 'Z', 'x', 'X', 'c', 'C', 'v', 'V', 'b', 'B', 'n', 'N', 'm', 'M', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    return randd.choice(letters)

def writeTo(text, target):
    file = open(str(target), 'w', encoding='utf-8')
    file.write(str(text))
    file.close()

def resize_image(input_image_path, output_image_path, size):
    try:
        original_image = Image.open(input_image_path)
        width, height = original_image.size
        resized_image = original_image.resize(size)
        width, height = resized_image.size
        resized_image.save(output_image_path)
        return "ok"
    except Exception as e:
        return str(e)
