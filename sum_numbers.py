# test = ["asd", 7, 9.3, {}, 12, None, []]
# print(sum([i for i in test if isinstance(i, (int, float))]))

test = ["asd", 7, 9.3, {}, 12, None, []]
print(sum(map(lambda i: i if type(i) in [int,float] else 0, test)))
