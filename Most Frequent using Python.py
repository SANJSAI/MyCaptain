Str= input("Enter a string: ")
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d
 
N_3 = most_frequent(Str)
List =[(k,v) for k, v in N_3.items()]
List.sort(key=lambda i:i[1],reverse=True)
print(List)
