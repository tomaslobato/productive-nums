import sys

print("Welcome to productivenums!")
print("What are productive numbers? https://www.youtube.com/shorts/Gg27V7PbRuU")
limit = input("input a limit for productive num finding: ")

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

try:
    int(limit)
except:
    print("limit is not an int number!")
    sys.exit(0)
    

prod_nums = []
for num in range(0, int(limit)):
    if not is_prime(num + 1):
        continue
    num = str(num)
    num = list(num)
    is_productive = True
    
    for ch in range(len(num)):
        ch_and_prev = ''.join(num[:ch + 1])
        digit = int(ch_and_prev)
        rest_str = ''.join(num[ch+1:])
        rest = 0
        
        if rest_str == "":
            continue
        else: rest = int(rest_str)
        
        newnum = int(digit) * rest + 1
        if not is_prime(newnum):
            is_productive = False
            break

    if is_productive:
        prod_nums.append(int(''.join(num)))

print(f"============== There's {len(prod_nums)} Productive numbers up to {limit} ============== \n {prod_nums}")