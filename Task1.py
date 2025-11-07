def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as o:
            total = 0
            count_developer = 0
            for elem in o.readlines():
                elements = elem.strip().split(",")
                if len(elements) != 2:
                    print(f"Not correct count of elements: {elem}")
                    continue
                try:
                    total += int(elements[1])
                    count_developer += 1
                except ValueError:
                    print(f"Not correct format salary: {elements[1]}")
                    continue
                if count_developer == 0:
                    return None, None
            average = total // count_developer
            return total, average
    except FileNotFoundError:
        print("File not found")
        return None, None
    except Exception as e:
        print("Error: {e}")
        return None, None


total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
