
import os
from checks.common import HealthCheck, Result

class ExtFsMountedHealthCheck(HealthCheck):
    def __init__(self, endpoint_name, path):
        self.endpoint_name = endpoint_name
        self.path = path

    def name(self):
        return "ExtFsMounted." + self.endpoint_name

    def run(self) -> Result:
        if not os.path.exists(self.path):
            return Result(healthy=False, message="Folder does not exist")
        if not os.path.isdir(self.path):
            return Result(healthy=False, message="Path is not directory")
        if not os.listdir(self.path):
            return Result(healthy=False, message="No files in path. Probably disk not mounted")
        return Result(healthy=True, message="ok")
