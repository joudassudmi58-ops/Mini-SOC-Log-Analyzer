
def analyze_log(file_path):
    failed_attempts = {}

    with open(file_path, "r") as file:
        for line in file:
            if "FAILED LOGIN" in line:
                parts = line.split()

                ip = parts[0]  # IP is first element
                timestamp = parts[3].strip("[")  # Extract timestamp

                if ip in failed_attempts:
                    failed_attempts[ip]["count"] += 1
                else:
                    failed_attempts[ip] = {
                        "count": 1,
                        "timestamps": [timestamp]
                    }

    print("\n🚨 Failed Login Attempts Report:\n")

    # Sort by highest attempts
    sorted_ips = sorted(
        failed_attempts.items(),
        key=lambda x: x[1]["count"],
        reverse=True
    )

    for ip, data in sorted_ips:
        print(f"IP: {ip}")
        print(f"Attempts: {data['count']}")
        print(f"Timestamps: {data['timestamps']}")
        print("-" * 40)

        if data["count"] >= 3:
            print("⚠ ALERT: Possible Brute Force Attack!\n")


if __name__ == "__main__":
    analyze_log("sample_log.txt")