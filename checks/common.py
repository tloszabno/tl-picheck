import abc

from dataclasses import dataclass

@dataclass
class Result(object):
    healthy: bool
    message: str

    def as_json(self):
        return {
            "healthy": self.healthy,
            "message": self.message
        }


class HealthCheck(object):
    @abc.abstractmethod
    def name(self) -> str:
        pass

    @abc.abstractmethod
    def run(self) -> Result:
        pass

