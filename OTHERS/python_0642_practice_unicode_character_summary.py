'''
Requirement:
Read a sentence from console, summarize how many letters / spaces / digits / others character in total.
'''

'''
2 Points:
1) unicode
2) dict
'''

def solution():

    sentence = input("Sentence: ")

    count_summary = {
        'letter' : 0,
        'space' : 0,
        'digit' : 0,
        'others' : 0
    }

    for c in sentence:
        print(c, ord(c))
        if 'A' <= c <= 'Z' or 'a' <= c <= 'z':
            count_summary['letter'] += 1
        elif c == ' ':
            count_summary['space'] += 1
        elif '0' <= c <= '9':
            count_summary['digit'] += 1
        else:
            count_summary['others'] += 1

    print(count_summary)

solution()




