import re
import urllib.request
import csv


url = 'https://msk.spravker.ru/avtoservisy-avtotehcentry/'
response = urllib.request.urlopen(url)
html_content = response.read().decode()

html_content = html_content.replace("Телефон", "ъ")
html_content = html_content.replace("Часы работы", "ъ")
html_content = html_content.replace("location", "ъ")
html_content = html_content.replace(";", "")


RE = r"(?:-link[^>]>)(?P<Name>[^<]+)(?:[^ъ]+[^\s]+[^А-я]+)(?P<Address>[^<\n]+)(?:[^ъ]+[^\s]+[^+]+)(?P<Phone>[^<]+)(?:[^ъ]+[^\s]+[^А-я]+)(?P<Schedule>[^<]+)"

matches = re.findall(RE, html_content)

result_file = 'result.csv'
with open(result_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Address', 'Phone_Number', 'Schedule'])
    writer.writerows(matches)

print(f"Данные успешно сохранены в файл {result_file}.")