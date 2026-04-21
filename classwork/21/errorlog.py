errors = {}

with open("log.txt") as f:
    for line in f:
        key = line.split()[0]
        errors[key] = errors.get(key, 0) + 1

print(errors)
