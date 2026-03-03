from datetime import datetime
import csv

THRESHOLD = 3
TIME_WINDOW_SECONDS = 60


def parse_timestamp(raw_time):
    # Remove closing bracket if exists
    raw_time = raw_time.replace("]", "")

    # Remove timezone if exists
    raw_time = raw_time.split()[0]

    return datetime.strptime(raw_time, "%d/%b/%Y:%H:%M:%S")


def analyze_log(file_path):
    failed_attempts = {}

    with open(file_path, "r") as file:
        for line in file:
            if "FAILED LOGIN" in line:
                parts = line.split()

                ip = parts[0]

                # Extract timestamp safely
                raw_timestamp = parts[3].strip("[")

                try:
                    timestamp = parse_timestamp(raw_timestamp)
                except ValueError:
                    continue  # Skip malformed lines safely

                if ip not in failed_attempts:
                    failed_attempts[ip] = []

                failed_attempts[ip].append(timestamp)

    suspicious_ips = []

    print("\n🚨 Advanced Failed Login Report\n")

    for ip, timestamps in failed_attempts.items():
        timestamps.sort()

        for i in range(len(timestamps) - (THRESHOLD - 1)):
            time_diff = (
                timestamps[i + THRESHOLD - 1] - timestamps[i]
            ).seconds

            if time_diff <= TIME_WINDOW_SECONDS:
                print("⚠ ALERT: Brute Force Detected!")
                print(f"IP: {ip}")
                print(f"Total Attempts: {len(timestamps)}")
                print("-" * 40)

                suspicious_ips.append(ip)
                break

    # Export CSV Report
    with open("report.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["IP Address", "Total Failed Attempts"])

        for ip, timestamps in failed_attempts.items():
            writer.writerow([ip, len(timestamps)])

    # Generate Blocklist
    with open("blocklist.txt", "w") as blockfile:
        for ip in suspicious_ips:
            blockfile.write(ip + "\n")

    print("\n✅ Report exported to report.csv")
    print("✅ Blocklist generated in blocklist.txt")


if __name__ == "__main__":
    analyze_log("sample_log.txt")