def check_lines(lines):
    total = {}
    count = {}
    for line in lines:
        city, temp, date = line.split(";")
        total[city] = total.get(city, 0) + float(temp)
        count[city] = count.get(city, 0) + 1
    return total, count


def find_best(total, count):
    best = ""
    for city in total:
        if best == "" or total[city] / count[city] > total[best] / count[best]:
            best = city
    return best


