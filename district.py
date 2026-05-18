#OOP 
# пункт с ООП
class District: # рабатаю с классом
# каждый район как объект со своими методами и свойствами
    def __init__(self, name, air_quality, traffic, infrastructure, population_density):
        self.name = name
        self.air_quality = air_quality
        self.traffic = traffic
        self.infrastructure = infrastructure
        self.population_density = population_density

    def show(self):
        print("District:", self.name)
        print("Air quality:", self.air_quality)
        print("Traffic level:", self.traffic)
        print("Infrastructure:", self.infrastructure)
        print("Population density:", self.population_density)
        print("-" * 40)