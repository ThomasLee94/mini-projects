def solve(strings):
    for chars in zip(*strings):
        print(chars)
    
    temp = set(["a", "b", "c"])

    print(str(list(temp)))

print(solve(["flight", "flin", "flow"]))