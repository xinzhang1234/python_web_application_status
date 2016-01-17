import urllib
import re

START_URL = "http://thegradcafe.com"
SUB_URL = "/survey/index.php?q=computer+science&t=a&o=&p="

RESULT_PATH = "tmp.txt"


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getInfo_onepage(url, result):
    #f = open(html)
    f = getHtml(url)
    w = open(RESULT_PATH,"a")
    for line in f.split('\n'):
        if not line.startswith("<tr class=\"row"):
            continue

        cell = line.split("</td><td")
        count = 0;
        school = cell[0][cell[0].index("instcol") + 9 :]
        major = cell[1][1:]
        major = "Phd" if major.find("Phd") >= 0 else "Master"
        detail = [0,0]
        if cell[2].find("strong") >= 0:
            detail = re.findall("<strong>(.*)</strong>(.*)<strong>(.*)</strong>(.*)<strong>(.*)</strong>(.*)", cell[2])
            detail = handle_detail(detail[0])

        if cell[4].find("datecol") >= 0:
            date = cell[4][cell[4].index("datecol") + 9:]
        tmp_ele = (school, date, major, detail[0], detail[1])
        tmp_str = ", ".join(str(j) for j in tmp_ele)
        w.writelines(tmp_str + "\n")
        result.append(tmp_ele)
    w.close()
    return result


def change_date_from_string():
    return


def get_page():
    # /survey/index.php?q=computer+science&amp;t=a&amp;o=&amp;p=2
    # get total result from
    global pages
    url = START_URL + SUB_URL + "1"
    html = getHtml(url)
    pages = int(re.findall("over (.*) pages",html)[0])
    return pages

def get_all_pages():
    #pages = get_page()
    pages = 3
    result = list()
    for i in range(1, pages):
        url = START_URL + SUB_URL + str(i)
        result = getInfo_onepage(url,result)

    return


def handle_detail(cell):
    gpa = cell[1].strip(": ").strip("<br/>")
    gre = cell[3].strip(": ").strip("<br/>")
    return (gpa, gre)

#getInfo_onepage("test.html")

get_all_pages()





#html = getHtml("http://thegradcafe.com/survey/index.php?q=computer+science")
#print html
