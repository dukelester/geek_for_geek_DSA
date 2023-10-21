def count_substrings(string1, string2):
    ''' Get the number of subsctrings in two strings
    '''
    answer = 0
    for i in range(len(string1)):
        result = ''
        for j in range(i, len(string1)):
            result += string1[j]
            if string2.find(result) != -1:
                answer += 1
    return answer
print(count_substrings('aab', 'aaaab'))
print(count_substrings('duke', 'duke lester is here'))
