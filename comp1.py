integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]

d={}

d={i:b for i,b in zip(integer,binary)}
print(d)