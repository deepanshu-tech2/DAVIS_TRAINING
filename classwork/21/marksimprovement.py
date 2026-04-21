old = {"A": 50, "B": 60}
new = {"A": 70, "B": 55}

for k in old:
    if new[k] > old[k]:
        print(k, "Improved", ((new[k]-old[k])/old[k])*100)
