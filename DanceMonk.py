import requests
from lxml import etree
import lxml.html
import csv

def parse(url):
    api = requests.get(url)
    tree = lxml.html.document_fromstring(api.text)
    text_original = tree.xpath('//*[@id="click_area"]/div//*[@class="original"]/text()')
    text_translate = tree.xpath('//*[@id="click_area"]/div//*[@class="translate"]/text()')
    with open("Dancemonk.csv", "w", newline='', encoding = 'utf-8') as csv_file:
        write = csv.writer(csv_file)
        for i in range(len(text_original)):
            write.writerow(text_original[i])
            write.writerow(text_translate[i])

def main():
    parse("https://www.amalgama-lab.com/songs/t/tones_and_i/dance_monkey.html")

if __name__ == '__main__':
    main()