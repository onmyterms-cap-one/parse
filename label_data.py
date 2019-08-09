import json
import csv
import collections
import xlsxwriter
from os import walk
import re

def removeHTML(str):
    p = re.compile(r'<.*?>')
    return p.sub('', str)

def removeNewLine(str):
    p = re.compile(r'\\n')
    return p.sub('', str)

f = []

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', '2015', '2016', '2017', '2018', '2019']

for (dirpath, dirnames, filenames) in walk("service/"):
    f.extend(filenames)
    break
# workbook = xlsxwriter.Workbook('training.xlsx')
# worksheet = workbook.add_worksheet()
# row = 0
# col = 0
for JSON in f:
    with open(("service/" + JSON), "r", encoding="utf8") as file:
        with open("onefile.jsonl", "a") as file2:
            data = json.load(file)
            data = data['pointsData']
            count = 1
            for key in data.keys():
                obj = data[key]
                if isinstance(obj, collections.Mapping) and "quoteText" in obj:
                    desc = obj['quoteText']
                    desc = removeHTML(desc)
                    desc = removeNewLine(desc)
                    hasDate = False
                    for month in months:
                        if month.lower() in desc.lower():
                            hasDate = True
                    rating = obj['tosdr']['point']
                    if not hasDate and desc != "" and desc != " " and desc != "Generated through the annotate view":
                        print(desc)
                        # print(obj['id'])
                        jsonl = {
                            "text_snippet":
                              {"content": desc}
                          }
                        json.dump(jsonl, file2)
                        file2.write("\n")
                        count += 1
                        # worksheet.write(row, col, desc)
                        # worksheet.write(row, col+1, rating)
                        # worksheet.write(row, col+2, obj['id'])
                        # row += 1
# workbook.close()

