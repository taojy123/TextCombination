#coding=utf8

import pinyin
import urllib2
import re
import time
import os

def get_online_seconds():
    p = urllib2.urlopen("http://www.baidu.com/").read()
    r = re.findall(r'serverTime : "(.*?)"', p)
    if r:
        t = r[0]
    else:
        t = 0
    return int(t)

# t = get_online_seconds()
# if t > 1423363604 + 3600 * 24:
#     raise


def has_chinese(s):
    s = repr(s)
    if r"\u" in s:
        return True
    else:
        return False


def get_numbers(s):
    result = ""
    numbers = "0987654321"
    for c in s:
        if c in numbers:
            result += c
    return result


def get_strings(s):
    result = ""
    strings = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for c in s:
        if c in strings:
            result += c
    return result


def get_chineses(s):
    result = ""
    for c in s:
        if r"\u" in repr(c):
            result += c
    return result


def is_all_chinese(s):
    for c in s:
        if r"\u" not in repr(c):
            return False
    return True


def decoding(s):
    s = s.replace("\xef\xbb\xbf", "").strip()
    try:
        return s.decode("gbk")
    except:
        return s.decode("utf8")
    return s


py = pinyin.PinYin()
py.load_word()

# print py.hanzi2pinyin("欢欢")

t1 = open("./input/1.txt").read()
t2 = open("./input/2.txt").read()
t3 = open("./input/3.txt").read()

t1 = decoding(t1)
t2 = decoding(t2)
t3 = decoding(t3)

tt1 = t1.split("\n")
tt2 = t2.split("\n")
tt3 = t3.split("\n")


for line in tt1:
    try:
        if not line.strip():
            continue
        result = []
        if has_chinese(line):
            if is_all_chinese(line):
                chineses = line
                ps = py.hanzi2pinyin(chineses)
                p1 = "".join(ps)
                p2 = ps[0]
                p3 = "".join([p[0] for p in ps])
                for n in tt2:
                    result.append(p1+n)
                for n in tt2:
                    result.append(p2+n)
                for n in tt2:
                    result.append(p3+n)
            elif get_numbers(line):
                chineses = get_chineses(line)
                numbers = get_numbers(line)
                ps = py.hanzi2pinyin(chineses)
                p1 = "".join(ps)
                p2 = ps[0]
                p3 = "".join([p[0] for p in ps])
                result.append(p1+numbers)
                result.append(p2+numbers)
                result.append(p3+numbers)
                result.append(numbers+p3)
                result.append(numbers+p1)
                for n in tt2:
                    result.append(p1+n)
                for n in tt2:
                    result.append(p2+n)
                for s in tt3:
                    result.append(s+numbers)
                for s in tt3:
                    result.append(numbers+s)
                for n in tt2:
                    result.append(p3+n)
            elif get_strings(line):
                chineses = get_chineses(line)
                strings = get_strings(line)
                ps = py.hanzi2pinyin(chineses)
                p1 = "".join(ps)
                p2 = ps[0]
                p3 = "".join([p[0] for p in ps])
                for n in tt2:
                    result.append(p1+n)
                for n in tt2:
                    result.append(p3+n)
                for n in tt2:
                    result.append(strings+n)
        else:
            strings = get_strings(line)
            numbers = get_numbers(line)
            if strings:
                for n in tt2:
                    result.append(strings+n)
                for n in tt2:
                    result.append(n+strings)
            if numbers:
                for s in tt3:
                    result.append(s+numbers)
                for s in tt3:
                    result.append(numbers+s)
            r = strings + numbers
            if r != line:
                result.append(r)
            r =  numbers + strings
            if r != line:
                result.append(r)
    except:
        print "Error:", line

    result = [r for r in result if len(r) >=6 and len(r) <= 12]
    result = "\n".join(result)
    if not result:
        result = "123456"
    line = line.encode("gbk")
    if os.path.exists("./output/" + line + ".txt"):
        print "./output/" + line + ".txt"
        print "exists"
    open("./output/" + line + ".txt", "w").write(result)
    print "========", line, "=========="
    print result
    print "============================"


raw_input("OK!")






