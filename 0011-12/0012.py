def intead(str1):
    f = open('filtered_words.txt')
    lines = f.read().split()
    for word in lines:
        if word in str1:
            str1 = str1.replace(word, "*"*len(word))
    print(str1)


if __name__ == '__main__':
    str1 = input()
    intead(str1)
