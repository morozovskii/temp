import sys
from stats import parse_record, read_valid, average_by_city, warmest_city


def count_errors(lines: list[str]) -> int:
    
    errors = 0
    for line in lines:
       
        if not line.strip():
            continue
        try:
            parse_record(line)
        except ValueError:
            errors += 1
    return errors


def main():
    input_lines = sys.stdin.read().splitlines()

    valid_records = read_valid(input_lines)
    processed_count = len(valid_records)
    skipped_count = count_errors(input_lines)

    if not valid_records:
        print(processed_count)
        print(skipped_count)
        print("0.0")
        return

    warm_city = warmest_city(valid_records)
    avg_temp = average_by_city(valid_records)[warm_city]

    print(processed_count)
    print(skipped_count)
    print(f"{avg_temp:.1f}")


if __name__ == "__main__":
    main()
