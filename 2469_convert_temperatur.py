from typing import List


class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        f = celsius * 1.8 + 32
        k = celsius + 273.15
        return [k,f]


# Kelvin = Celsius + 273.15
# Fahrenheit = Celsius * 1.80 + 32.00