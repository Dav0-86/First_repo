
text = '''60b90c1c13067a15887e1ae1,Tayson,3
60b90c2413067a15887e1ae2,Vika,1
60b90c2e13067a15887e1ae3,Barsik,2
60b90c3b13067a15887e1ae4,Simon,12
60b90c4613067a15887e1ae5,Tessi,5'''

try: 
    with open("D:\\cats_file.txt", "w", encoding="utf-8") as file:
        file.write(text) 

except Exception as error:
    print(f"Файл не відкрився правильно, помилка --> {error}")


outlist = []

def get_cats_info(path):
    try:
        with open("D:\\cats_file.txt", "r", encoding="utf-8") as file:
            for split in text.split("\n"):
                split = split.split(",")
                outlist.append({'id': split[0], 'name': split[1], 'age': split[2]})
            return outlist
    except Exception as error:
        print(f"Виникла помилка --> {error}")



cats_info = get_cats_info("D:\\cats_file.txt")
print(cats_info)
