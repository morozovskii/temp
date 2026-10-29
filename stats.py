def parse_record(line: str) -> dict:
    
    parts = line.split(";")

   
    if len(parts) != 3:
        raise ValueError(f"Неверное количество полей: ожидалось 3, найдено {len(parts)} в строке '{line}'")

    city, temp_str, date = parts
    city = city.strip()
    date = date.strip()
    temp_str = temp_str.strip()

    
    if not city:
        raise ValueError("Город не может быть пустым")
    if not date:
        raise ValueError("Дата не может быть пустой")

   
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"Температура не является числом: '{temp_str}'")

    return {"city": city, "temp": temp, "date": date}


def read_valid(lines: list[str]) -> list[dict]:
   
    valid_records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            # Плохую строку просто пропускаем
            continue
    return valid_records


def average_by_city(records: list[dict]) -> dict:
 
    
    totals = {}
    counts = {}

    for r in records:
        c = r["city"]
        t = r["temp"]
        totals[c] = totals.get(c, 0.0) + t
        counts[c] = counts.get(c, 0) + 1

    averages = {}
    for c in totals:
        averages[c] = round(totals[c] / counts[c], 1)

    return averages


def warmest_city(records: list[dict]) -> str:
    
    if not records:
        return ""

    avg = average_by_city(records)

    best_city = None
    best_temp = -float("inf")

    for city, temp in avg.items():
        if temp > best_temp:
            best_temp = temp
            best_city = city
        elif temp == best_temp:
            if best_city is None or city < best_city:
                best_city = city

    return best_city



