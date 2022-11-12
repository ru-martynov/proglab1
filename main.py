import json


# Подсчитывает общее количество символов в файле
def lenFile(file):
    infile = open(file, 'r')
    content = infile.read()
    print(len(content))
    infile.close()


# Подсчитывает общее количесто символов без пробелов и знаков препинания
def lenFileWithoutPunctuation(file):
    infile = open(file, 'r')
    content = infile.read()
    content = content.replace(' ', '')
    content = content.replace('.', '')
    content = content.replace(',', '')
    content = content.replace('!', '')
    content = content.replace('?', '')
    content = content.replace('(', '')
    content = content.replace(')', '')
    content = content.replace(':', '')
    content = content.replace(';', '')
    content = content.replace('\'', '')
    content = content.replace('\"', '')
    print(len(content))
    infile.close()


# Выводит название покемона с самым длинным описанием в json
def fileLongestDescription(file):
    # print longest description
    infile = open(file, 'r')
    data = json.load(infile)
    longest = 0
    for i in data:
        for j in i:
            if j == 'description':
                if len(i[j]) > longest:
                    longest = len(i[j])
                    name = i['name']
    print(name)
    infile.close()


# Определяет названия умений, которые содержат больше всего слов (abilities)
def fileLargestNumberOfWordsAbilities(file):
    # print largest number of words in abilities
    infile = open(file, 'r')
    data = json.load(infile)
    largest = 0
    for i in data:
        for j in i:
            if j == 'abilities':
                for k in i[j]:
                    if len(k.split()) > largest:
                        largest = len(k.split())
                        name_abilities = k
    print(name_abilities)
    infile.close()


def main():
    file = 'pokemon_full.json'
    lenFile(file)
    lenFileWithoutPunctuation(file)
    fileLongestDescription(file)
    fileLargestNumberOfWordsAbilities(file)


main()
