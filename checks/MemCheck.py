
import os
from checks.common import HealthCheck, Result
from subprocess import check_output
import psutil



class MemoryHealthCheck(HealthCheck):
    def name(self):
        return "MemoryHealthCheck"

    def run(self):
        available = psutil.virtual_memory().available / (1024 * 1024)
        total = psutil.virtual_memory().total / (1024 * 1024)
        available_percent = available * 100 / total


        if available_percent < 10:
            return Result(healthy=False, message=f"Free ram is less then 10%. Currently available {available:.2f} MB. Total {total:.2f} MB.")
        return Result(healthy=True, message=f"Ram usage ok. Currently available {available:.2f} MB. Total {total:.2f} MB.")

