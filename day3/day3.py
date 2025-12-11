with open("input3", "r") as f:
    data = f.read().split("\n")

# def get_largest(string, how_many):
#     largest = "0"
#     index = 0
#     for i in range(0, len(string)):
#         char = string[i:i+1]
#         if char >= largest:
#             largest = char
#             index = i
#     new_string = string[index+1:]
#     return largest, new_string
# 
# def get_sub(num, digits):
#     return_string = ""
#     index = 0
#     for i in range(1, digits + 2):
#         num = num[-(digits-i):]
#         if digits-i > 0: new_num = num[index:-(digits-i)]
#         else: new_num = num[index:]
#         print(index, (digits-i))
#         get = get_largest(new_num)
#         return_string += get[0]
#         index += get[1]
#         print(new_num)
#     return int(return_string)
# 

def find_largest(string : str, how_many):
    return_string = ""
    for i in range(0, how_many):
        if how_many - 1 - i > 0: new_string = string[:-(how_many-1-i)]
        else: new_string = string
        print(f"new_string: {new_string}")
        print(f"string: {string}")
        print(f"i: {i}")
        largest = "0"
        index = 0
        for j in range(0, len(new_string)):
            char = new_string[j]
            if char > largest:
                largest = char
                index = j
        return_string += largest
        string = string[index+1:]
    print(return_string)
    return int(return_string)

sum = 0

for line in data:
    sum += find_largest(line, 12)

print(sum)