def number_inversion(n):
    result = 0
    string = str(n)
    inverse = []
    for i in range(len(string)):
        inverse.append(int(string[len(string)-1-i]))
    for j in range(len(inverse)):
        result += inverse[j]*10**(len(inverse)-j-1)
    return result, 'Luca Lowenbach', 'Lycee International de Londres'

print(number_inversion(234))
assert number_inversion(101) == (101, 'Luca Lowenbach', 'Lycee International de Londres')
assert number_inversion(5493) == (3945, 'Luca Lowenbach', 'Lycee International de Londres')


def palindrome_finder(n):
    results = []
    palindromic = []
    if number_inversion(n) == (n, 'Luca Lowenbach', 'Lycee International de Londres'):
        results.append(n)
    for i in range(1, n):
        if number_inversion(n-i) == (n-i, 'Luca Lowenbach', 'Lycee International de Londres') and number_inversion(i) == (i, 'Luca Lowenbach', 'Lycee International de Londres'):
           results.append([n-i, i])
           palindromic.append(n-i)
           palindromic.append(i)
        elif number_inversion(n-i) == (n-i, 'Luca Lowenbach', 'Lycee International de Londres'):
            palindromic.append(n-i)
        elif number_inversion(i) == (i, 'Luca Lowenbach', 'Lycee International de Londres'):
            palindromic.append(i)
    for i in range(len(palindromic)):
        minus = n - palindromic[i]
        for j in range(1, minus):
            if number_inversion(minus-j) == (minus-j, 'Luca Lowenbach', 'Lycee International de Londres') and number_inversion(j) == (j, 'Luca Lowenbach', 'Lycee International de Londres'):
                results.append([minus-j, j, palindromic[i]])
    if len(results) == 1:
        return results[0], 'Luca Lowenbach', 'Lycee International de Londres'
    lowest = ['no palindrome']
    lowest_number = 1000000
    for i in range(len(results)):
        if results[i] == n:
            del results[i] 
        for j in range(len(results[i])):
            if lowest_number == results[i][j]:
                lowest.append(results[i])
            elif lowest_number > results[i][j]:
                lowest_number = results[i][j]
                lowest = [results[i]]
    if len(lowest) > 1:
        highest = []
        highest_number = 0
        for i in range(len(lowest)):
            for j in range(len(lowest[i])):
                if highest_number == lowest[i][j]:
                    highest.append(lowest[i])
                elif highest_number < lowest[i][j]:
                    highest_number = lowest[i][j]
                    highest = lowest[i]
        return highest[3], 'Luca Lowenbach', 'Lycee International de Londres'
    return lowest[3], 'Luca Lowenbach', 'Lycee International de Londres'
        
print(palindrome_finder(54))
print(palindrome_finder(1031))

assert palindrome_finder(54) == ([9, 44, 1], 'Luca Lowenbach', 'Lycee International de Londres')
assert palindrome_finder(1031) == ([101, 929, 1], 'Luca Lowenbach', 'Lycee International de Londres')

