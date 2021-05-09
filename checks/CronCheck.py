
import os
from checks.common import HealthCheck, Result
from subprocess import check_output

class CronHealthCheck(HealthCheck):
    def __init__(self, number_of_items_in_cron : int):
        self.number_of_items_in_cron =  number_of_items_in_cron

    def name(self):
        return f"CronHealthCheck.{self.number_of_items_in_cron}"

    def run(self):
        out = check_output(["crontab -l -u tomek | grep/home | wc -l"], shell=True)
        result = int(out)
        if result != self.number_of_items_in_cron:
            return Result(healthy=False, message=f"Number of elements in cron is different than expected. Current={result} expected={self.number_of_items_in_cron}")
        return Result(healthy=True, message=f"Number of cron elements matches. Expected {self.number_of_items_in_cron}")

