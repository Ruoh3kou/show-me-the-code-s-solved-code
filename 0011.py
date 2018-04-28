def verify(word):
    f = open('filtered_words.txt')
    lines = f.read().split('\n')
    if word in lines:
        print('Human Rights')
    else:
        print(word)


if __name__ == '__main__':
    word = input()
    verify(word)
