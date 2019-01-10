try:
    while True:
        code = input()
        result=reversed(code)
        if code=="END":break
        print("".join(result))
except:
    pass
