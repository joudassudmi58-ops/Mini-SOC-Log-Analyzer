# Mini SOC Log Analyzer
# Created by Joud

def analyze_log(file_path):
    failed_attempts = {}

    with open(file_path, "r") as file:
        for line in file:
            if "FAILED LOGIN" in line:
                parts = line.split()
                ip = parts[-1]

                if ip in failed_attempts:
                    failed_attempts[ip] += 1
                else:
                    failed_attempts[ip] = 1

    print("\n🚨 Failed Login Attempts Report:\n")

    for ip, count in failed_attempts.items():
        print(f"IP Address: {ip} | Attempts: {count}")

        if count >= 3:
            print("⚠️ ALERT: Possible Brute Force Attack!\n")


if __name__ == "__main__":
    analyze_log("sample_log.txt")