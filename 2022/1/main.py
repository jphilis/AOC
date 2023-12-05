with open("data.txt", "r") as file:
    data = file.read().split("\n\n") # Split by double new line
    print(len(data))
    data = [x.split("\n") for x in data] # Split by new line
    data = [[int(x) for x in inner_data if x != ""] for inner_data in data] # Remove empty strings
    # print([sum(x) for x in data])

def max_summed_group(data):
    return max(enumerate(data), key = lambda x: sum(x[1]))

data_copy = data.copy()
index_1, elf_1 = max_summed_group(data_copy)
data_copy.pop(index_1)
index_2, elf_2 = max_summed_group(data_copy)
data_copy.pop(index_2)
index_3, elf_3 = max_summed_group(data_copy)

print(elf_1, elf_2, elf_3)
print(sum(elf_1) + sum(elf_2) + sum(elf_3))