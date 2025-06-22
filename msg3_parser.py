def read_log_file(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        return lines

def count_msg3_results(lines):
    success_count = 0
    failure_count = 0

    for line in lines:
        if "type MSG3-RRC-C-REQ" in line and "status success" in line:
            success_count += 1
        elif "type   MSG3-UNKNOWN" in line and "status timeout" in line:
            failure_count += 1

    return success_count, failure_count

def calculate_hourly_msg3_stats(lines):
    successes_by_hour = {}
    failures_by_hour = {}

    for line in lines:
        parts = line.split()
        if len(parts) < 2:
            continue

        hour = parts[1][:2]

        if "type MSG3-RRC-C-REQ" in line and "status success" in line:
            successes_by_hour[hour] = successes_by_hour.get(hour, 0) + 1
        elif "type MSG3-UNKNOWN" in line and "status timeout" in line:
            failures_by_hour[hour] = failures_by_hour.get(hour, 0) + 1
    print("\nHourly MSG3 Success Rate Report:\n")
    all_hours = set(successes_by_hour.keys()) | set(failures_by_hour.keys())
    for hour in sorted(all_hours):
        success = successes_by_hour.get(hour, 0)
        failure = failures_by_hour.get(hour, 0)
        total = success + failure

        if total > 0:
            rate = (success / total) * 100
            print(f"Hour {hour}: Success = {success}, Failure = {failure}, Success Rate = {rate:.2f}%")
        else:
            print(f"Hour {hour}: No MSG3 entries")



if __name__ == "__main__":
    log_lines = read_log_file("bs_log.txt")
    print(f"Total lines read: {len(log_lines)}")

    success, failure = count_msg3_results(log_lines)
    print(f"MSG3 Success: {success}")
    print(f"MSG3 Failure: {failure}")

    total = success + failure
    if total > 0:
        success_rate = (success / total) * 100
        print(f"MSG3 Success Rate: {success_rate:.2f}%")
    else:
        print("No MSG3 entries found.")

    calculate_hourly_msg3_stats(log_lines)


