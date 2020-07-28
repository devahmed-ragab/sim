

class Appliance:

    def __init__(self, name, wattage):
        self.name = name
        self._wattage = wattage

    @property
    def wattage(self):
        return self._wattage

    def name(self):
        return self.name

    @wattage.setter
    def wattage(self, watt):
        if self.watt < 0:
            raise ValueError(" wattage can't be negative . ")
        self._wattage = watt

    def get_name(self, name):
        self._name = name
