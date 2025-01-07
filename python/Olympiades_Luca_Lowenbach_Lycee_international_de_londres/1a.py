def number_inversion(n):
    result = 0
    string = str(n)
    inverse = []
    for i in range(len(string)):
        inverse.append(string[len(string)-1-i])
    for j in range(len(inverse)):
        result += inverse[j]*10**(len(inverse)-j)
    return result, 'Luca Lowenbach', 'Lycee International de Londres'




def palindrome_finder(n):
    if number_inversion(n) == n:
        return n
    
string = 'ababa'
