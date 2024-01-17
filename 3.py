import re
def convert_number(text):
    pattern = r'(\d{2,4}\\\d{2,5})'
    result = re.findall(pattern, text)

    for num in result:
        parts = num.split('\\')
        good_number = parts[0].zfill(4) + '\\' + parts[1].zfill(5)
        print(good_number)

text = "Некоторые особенные номера: 5467\\456, 405\\549"
convert_number(text)