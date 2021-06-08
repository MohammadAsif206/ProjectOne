
N = [ 2, 5, 8, 10, 4] # k = 4 , we need 6
k = 4
i = 1
while i < 12:
    result = f'{( 2 * i +1 ) *"*" }{str(i)}{( 2 * i -1 ) *"*"}'
    print(result)
    i+=1

string = "this is my name asif mohammad"
vowels = "aeiou"
count = 0
for v in string:
    if v in vowels:
        count+=1
print(count)

while True:
    k+=1
    if not k in N:
        print(k)
        break
