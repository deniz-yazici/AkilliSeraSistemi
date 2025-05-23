import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

def get_fuzzy_result(temp, hum, plant_type, hour_val, soil_moist):
    # Girdi tanımları
    temperature = ctrl.Antecedent(np.arange(10, 46, 1), 'temperature')
    humidity = ctrl.Antecedent(np.arange(20, 101, 1), 'humidity')
    plant = ctrl.Antecedent(np.arange(1, 4, 1), 'plant_type')
    hour = ctrl.Antecedent(np.arange(0, 25, 1), 'hour')
    soil = ctrl.Antecedent(np.arange(0, 101, 1), 'soil_moisture')

    # Çıktı tanımları
    water_time = ctrl.Consequent(np.arange(0, 31, 1), 'water_time')
    fan_power = ctrl.Consequent(np.arange(0, 101, 1), 'fan_power')

    # Üyelik fonksiyonları
    temperature['low'] = fuzz.trimf(temperature.universe, [10, 10, 20])
    temperature['optimal'] = fuzz.trimf(temperature.universe, [18, 25, 32])
    temperature['high'] = fuzz.trimf(temperature.universe, [30, 45, 45])

    humidity['low'] = fuzz.trimf(humidity.universe, [20, 20, 40])
    humidity['medium'] = fuzz.trimf(humidity.universe, [35, 60, 85])
    humidity['high'] = fuzz.trimf(humidity.universe, [75, 100, 100])

    plant['cactus'] = fuzz.trimf(plant.universe, [1, 1, 1.5])
    plant['tomato'] = fuzz.trimf(plant.universe, [1.5, 2, 2.5])
    plant['lettuce'] = fuzz.trimf(plant.universe, [2.5, 3, 3])

    hour['night'] = fuzz.trimf(hour.universe, [0, 0, 6])
    hour['morning'] = fuzz.trimf(hour.universe, [6, 9, 12])
    hour['afternoon'] = fuzz.trimf(hour.universe, [12, 15, 18])
    hour['evening'] = fuzz.trimf(hour.universe, [18, 21, 24])

    soil['dry'] = fuzz.trimf(soil.universe, [0, 0, 40])
    soil['moist'] = fuzz.trimf(soil.universe, [30, 50, 70])
    soil['wet'] = fuzz.trimf(soil.universe, [60, 100, 100])

    water_time['short'] = fuzz.trimf(water_time.universe, [0, 0, 10])
    water_time['medium'] = fuzz.trimf(water_time.universe, [5, 15, 25])
    water_time['long'] = fuzz.trimf(water_time.universe, [20, 30, 30])

    fan_power['low'] = fuzz.trimf(fan_power.universe, [0, 0, 40])
    fan_power['medium'] = fuzz.trimf(fan_power.universe, [30, 50, 70])
    fan_power['high'] = fuzz.trimf(fan_power.universe, [60, 100, 100])

    # Kurallar
    rules = [
        ctrl.Rule(temperature['high'] & humidity['low'], (fan_power['high'], water_time['long'])),
        ctrl.Rule(temperature['high'] & soil['dry'], (water_time['long'], fan_power['medium'])),
        ctrl.Rule(plant['cactus'] & soil['wet'], water_time['short']),
        ctrl.Rule(plant['lettuce'] & soil['dry'], water_time['long']),
        ctrl.Rule(plant['tomato'] & humidity['medium'] & temperature['optimal'], water_time['medium']),
        ctrl.Rule(soil['moist'] & hour['morning'], water_time['short']),
        ctrl.Rule(humidity['high'] & temperature['low'], fan_power['low']),
        ctrl.Rule(soil['dry'] & hour['afternoon'], water_time['long']),
        ctrl.Rule(temperature['optimal'] & humidity['medium'], fan_power['medium']),
        ctrl.Rule(soil['wet'] & humidity['high'], fan_power['low'])
    ]

    # Kontrol sistemi
    system = ctrl.ControlSystem(rules)
    sim = ctrl.ControlSystemSimulation(system)

    # Girdi değerleri atanıyor
    sim.input['temperature'] = temp
    sim.input['humidity'] = hum
    sim.input['plant_type'] = plant_type
    sim.input['hour'] = hour_val
    sim.input['soil_moisture'] = soil_moist

    # Hesapla
    sim.compute()

    # Çıktı kontrolü ve dönüş
    fan = sim.output['fan_power'] if 'fan_power' in sim.output else 0
    water = sim.output['water_time'] if 'water_time' in sim.output else 0
    return water, fan

