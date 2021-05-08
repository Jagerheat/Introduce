 def cher(s):
    return s[:2] + s[-2:] if len(s) >= 2 else ''
print(cher("step"))