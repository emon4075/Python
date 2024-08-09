List = {}
while True:
    try:
        Item = input().strip().upper()
    except EOFError:
        break
    except KeyboardInterrupt:
        continue
    else:
        if Item in List:
            List[Item] += 1
        else:
            List[Item] = 1
sorted_keys = sorted(List.keys())
sorted_list = {key: List[key] for key in sorted_keys}

for item in sorted_list:
    print(sorted_list[item], item)
