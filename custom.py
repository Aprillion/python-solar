"""Read from files that have custom format"""

# open a file for reading and iterate each line
with open('./custom.txt') as f:
    config = {}
    for line in f:
        # assign to multiple variables (tuple unpacking)
        id, name = line.strip().split(' = ')
        config[id] = name

for id in ["123", "213"]:
    print(config[id])
