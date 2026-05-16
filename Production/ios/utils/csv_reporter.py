import csv
import os
from datetime import datetime


class CSVReporter:
    def __init__(self, device_name):
        self.device_name = device_name
        self.results = []

    def add_result(self, nodeid, outcome, duration, phase="call", message=""):
        self.results.append({
            "test_case": nodeid.split("::")[-1],
            "nodeid": nodeid,
            "phase": phase,
            "status": outcome.upper(),
            "duration(s)": round(duration, 2),
            "device_name": self.device_name,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            # "message": message
        })

    def write_csv(self, file_path):
        print("🔥 write_csv FROM:", __file__)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        file_exists = os.path.exists(file_path)
        with open(file_path, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(
                f,
                fieldnames=[
                    "test_case",
                    "nodeid",
                    "phase",
                    "status",
                    "duration(s)",
                    "device_name",
                    "timestamp",
                    # "message"
                ]
            )

            if not file_exists:
                writer.writeheader()
            writer.writerows(self.results)

        # QUAN TRỌNG: clear sau khi ghi
        self.results.clear()
