from checks.common import HealthCheck, Result
from subprocess import check_output


def __get_cpu_temp__():
    def __get_temp__internal():
        out = check_output(["/opt/vc/bin/vcgencmd", "measure_temp"])
        return float(out.split('=')[1].split('\'')[0])
    try:
        return __get_temp__internal()
    except:
        return None


class  TemperatureHealthCheck(HealthCheck):
    def name(self):
        return "Temperature"

    def run(self) -> Result:
        temp = __get_cpu_temp__()
        if not temp:
            return Result(healthy=False, message="Cannot get temperature")
        if temp > 80:
            return Result(healthy=False, message=f"Temperature is to big. Currently is {str(temp)}C")

        return Result(healthy=True, message=f"Temperature is ok ({str(temp)}C")
