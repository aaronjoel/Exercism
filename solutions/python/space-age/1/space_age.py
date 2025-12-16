class SpaceAge:
    # Orbital period in Earth years
    ORBITAL_PERIODS = {
        'mercury': 0.2408467,
        'venus': 0.61519726,
        'earth': 31557600,
        'mars': 1.8808158,
        'jupiter': 11.862615,
        'saturn':  29.447498,
        'uranus': 84.016846,
        'neptune': 164.79132
    }
    def __init__(self, seconds):
        self.seconds = seconds
        self.earth_age = seconds / SpaceAge.ORBITAL_PERIODS['earth']

    def on_earth(self):
        return round(self.earth_age, 2)
        
    def on_mercury(self):
        return round(self.earth_age / SpaceAge.ORBITAL_PERIODS['mercury'], 2)
                     
    def on_venus(self):
        return round(self.earth_age / SpaceAge.ORBITAL_PERIODS['venus'], 2)

    def on_saturn(self):
        return round(self.earth_age / SpaceAge.ORBITAL_PERIODS['saturn'], 2)
        
    def on_mars(self):
        return round(self.earth_age / SpaceAge.ORBITAL_PERIODS['mars'], 2)
        
    def on_jupiter(self):
        return round(self.earth_age / SpaceAge.ORBITAL_PERIODS['jupiter'], 2)
        
    def on_uranus(self):
        return round(self.earth_age / SpaceAge.ORBITAL_PERIODS['uranus'], 2)
        
    def on_neptune(self):
        return round(self.earth_age / SpaceAge.ORBITAL_PERIODS['neptune'], 2)
        
