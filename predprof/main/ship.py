class Ship:

    def __init__(self, oxi, fuel, sh):
        self.oxi = oxi
        self.fuel = fuel
        self.sh = sh

    def get_fuel(self):
        return self.fuel

    def set_fuel(self, fuel):
        self.fuel = fuel

    def get_oxi(self):
        return self.oxi

    def set_oxi(self, oxi):
        self.oxi = oxi

    def get_sh(self):
        return self.sh

    def set_sh(self, sh):
        self.sh = sh
