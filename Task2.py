def get_cats_info(path):
    list = []
    try:
        with open(path, "r", encoding="utf-8") as o:
            list_keys = ("id", "name", "age")
            for cat in o.readlines():
                cats = cat.strip().split(",")
                dict1 = dict(zip(list_keys, cats))
                list.append(dict1)
            return list
    except FileNotFoundError:
        print("File not found")
        return list
    except Exception as e:
        print(f"Error: {e}")
        return list


cats_info = get_cats_info("cats_file.txt")
print(cats_info)
