import os
import sys
import traci

def run():
    # IDs de los semáforos y detectores
    traffic_light_id1 = '4183242491'
    traffic_light_id2 = '419724292'
    traffic_light_id3 = '3073574611'
    traffic_light_id4 = '3451102567'
    traffic_light_id5 = '4174768674'
    traffic_light_id6 = '3445696063'
    traffic_light_id7 = '4962835014'
    traffic_light_id8 = '4962835015'
    traffic_light_id9 = '5214556597'
    traffic_light_id10 = '4991468333'
    traffic_light_id11 = '8920874075'
    traffic_light_id12 = '8920874077'
    traffic_light_id13 = '8920874083'
    traffic_light_id14 = '8920874082'
    

    detector_id1 = 'tram_detector'
    detector_id2 = 'tram_detector2'
    detector_id3 = 'tram_detector3'

    # Definición de fases del ciclo semafórico para cada semáforo
    phases1 = [
        {"duration": 68, "state": "GGGGrrrr"},
        {"duration": 3, "state": "yyyyrrrr"},
        {"duration": 69, "state": "rrrrGGGG"},
        {"duration": 3, "state": "rrrryyyy"}
    ]

    phases2 = [
        {"duration": 76, "state": "GGGrrrrGG"},
        {"duration": 3, "state": "yyyrrrryy"},
        {"duration": 33, "state": "rrrGGGGrr"},
        {"duration": 3, "state": "rrrryyyyrr"}
    ]

    phases3 = [
        {"duration": 3600, "state": "GGGGG"}
    ]

    phases4 = [
        {"duration": 3600, "state": "GGG"}
    ]

    phases5 = [
        {"duration": 3600, "state": "GGGG"}
    ]

    phases6 = [
        {"duration": 3600, "state": "GGGG"}
    ]

    phases7 = [
        {"duration": 3600, "state": "GGGG"}
    ]

    phases8 = [
        {"duration": 3600, "state": "GGGG"}
    ]

    phases9 = [
        {"duration": 3600, "state": "GGG"}
    ]
    
    phases10 = [
        {"duration": 3600, "state": "GGG"}
    ]
    phases11 = [
        {"duration": 3600, "state": "GGG"}
    ]
    
    phases12 = [
        {"duration": 3600, "state": "GGG"}
    ]
    
    phases13 = [
        {"duration": 3600, "state": "GG"}
    ]
    
    phases14 = [
        {"duration": 3600, "state": "GGG"}
    ]

    # Variables para mantener el estado del semáforo cuando se detecta un tranvía
    remaining_steps1 = 0
    remaining_steps2 = 0
    remaining_steps3 = 0

    # Variables para el ciclo normal del semáforo
    current_phase_index1 = 0
    current_phase_duration1 = phases1[current_phase_index1]["duration"]

    current_phase_index2 = 0
    current_phase_duration2 = phases2[current_phase_index2]["duration"]
    
    current_phase_index3 = 0
    current_phase_duration3 = phases4[current_phase_index3]["duration"]
    

    # Ciclo de simulación
    while traci.simulation.getMinExpectedNumber() > 0:
        traci.simulationStep()

        # Obtener el número de vehículos en los detectores
        vehicle_count1 = traci.inductionloop.getLastStepVehicleNumber(detector_id1)
        vehicle_count2 = traci.inductionloop.getLastStepVehicleNumber(detector_id2)
        vehicle_count3 = traci.inductionloop.getLastStepVehicleNumber(detector_id3)

        # Control del primer semáforo
        if vehicle_count1 > 0:
            traci.trafficlight.setRedYellowGreenState(traffic_light_id1, 'rrrrrrrr')
            remaining_steps1 = 15  # 15 segundos (150 pasos de simulación)
        else:
            if remaining_steps1 == 0:
                # Ciclo normal del semáforo 1
                current_phase_duration1 -= 1
                if current_phase_duration1 == 0:
                    current_phase_index1 = (current_phase_index1 + 1) % len(phases1)
                    current_phase_duration1 = phases1[current_phase_index1]["duration"]
                    traci.trafficlight.setRedYellowGreenState(traffic_light_id1, phases1[current_phase_index1]["state"])

        # Mantener el estado del primer semáforo durante 15 segundos
        if remaining_steps1 > 0:
            remaining_steps1 -= 1
            if remaining_steps1 == 0:
                traci.trafficlight.setRedYellowGreenState(traffic_light_id1, phases1[current_phase_index1]["state"])

        # Control del segundo semáforo
        if vehicle_count2 > 0:
            traci.trafficlight.setRedYellowGreenState(traffic_light_id2, 'rrrrrrrrr')
            remaining_steps2 = 15  # 15 segundos (150 pasos de simulación)
        else:
            if remaining_steps2 == 0:
                # Ciclo normal del semáforo 2
                current_phase_duration2 -= 1
                if current_phase_duration2 == 0:
                    current_phase_index2 = (current_phase_index2 + 1) % len(phases2)
                    current_phase_duration2 = phases2[current_phase_index2]["duration"]
                    traci.trafficlight.setRedYellowGreenState(traffic_light_id2, phases2[current_phase_index2]["state"])

        # Mantener el estado del segundo semáforo durante 15 segundos
        if remaining_steps2 > 0:
            remaining_steps2 -= 1
            if remaining_steps2 == 0:
                traci.trafficlight.setRedYellowGreenState(traffic_light_id2, phases2[current_phase_index2]["state"])
                
        # Control para resto de semaforos
        if vehicle_count3 > 0:
            traci.trafficlight.setRedYellowGreenState(traffic_light_id3, 'rrrrr')
            traci.trafficlight.setRedYellowGreenState(traffic_light_id4, 'rrr')
            traci.trafficlight.setRedYellowGreenState(traffic_light_id5, 'rrrr')
            traci.trafficlight.setRedYellowGreenState(traffic_light_id6, 'rrrr')
            traci.trafficlight.setRedYellowGreenState(traffic_light_id7, 'rrrr')
            traci.trafficlight.setRedYellowGreenState(traffic_light_id8, 'rrrr')
            traci.trafficlight.setRedYellowGreenState(traffic_light_id9, 'rrr')
            traci.trafficlight.setRedYellowGreenState(traffic_light_id10, 'rrG')
            traci.trafficlight.setRedYellowGreenState(traffic_light_id11, 'Grr')
            traci.trafficlight.setRedYellowGreenState(traffic_light_id12, 'rrG')
            traci.trafficlight.setRedYellowGreenState(traffic_light_id13, 'Gr')
            traci.trafficlight.setRedYellowGreenState(traffic_light_id14, 'Grr')
            
            remaining_steps3 = 20  # 20 segundos (150 pasos de simulación)
        else:
            if remaining_steps3 == 0:
                # Ciclo normal del semáforo 2
                current_phase_duration3 -= 1
                if current_phase_duration3 == 0:
                    current_phase_index3 = (current_phase_index3 + 1) % len(phases3)
                    current_phase_duration3 = phases3[current_phase_index3]["duration"]
                    traci.trafficlight.setRedYellowGreenState(traffic_light_id3, phases3[current_phase_index3]["state"])
                    traci.trafficlight.setRedYellowGreenState(traffic_light_id4, phases4[current_phase_index3]["state"])
                    traci.trafficlight.setRedYellowGreenState(traffic_light_id5, phases5[current_phase_index3]["state"])
                    traci.trafficlight.setRedYellowGreenState(traffic_light_id6, phases6[current_phase_index3]["state"])
                    traci.trafficlight.setRedYellowGreenState(traffic_light_id7, phases7[current_phase_index3]["state"])
                    traci.trafficlight.setRedYellowGreenState(traffic_light_id8, phases8[current_phase_index3]["state"])
                    traci.trafficlight.setRedYellowGreenState(traffic_light_id9, phases9[current_phase_index3]["state"])
                    traci.trafficlight.setRedYellowGreenState(traffic_light_id10, phases10[current_phase_index3]["state"])
                    traci.trafficlight.setRedYellowGreenState(traffic_light_id11, phases11[current_phase_index3]["state"])
                    traci.trafficlight.setRedYellowGreenState(traffic_light_id12, phases12[current_phase_index3]["state"])
                    traci.trafficlight.setRedYellowGreenState(traffic_light_id13, phases13[current_phase_index3]["state"])
                    traci.trafficlight.setRedYellowGreenState(traffic_light_id14, phases14[current_phase_index3]["state"])
                    

        # Mantener el estado del segundo semáforo durante 15 segundos
        if remaining_steps3 > 0:
            remaining_steps3 -= 1
            if remaining_steps3 == 0:
                traci.trafficlight.setRedYellowGreenState(traffic_light_id3, phases3[current_phase_index3]["state"])
                traci.trafficlight.setRedYellowGreenState(traffic_light_id4, phases4[current_phase_index3]["state"])
                traci.trafficlight.setRedYellowGreenState(traffic_light_id5, phases5[current_phase_index3]["state"])
                traci.trafficlight.setRedYellowGreenState(traffic_light_id6, phases6[current_phase_index3]["state"])
                traci.trafficlight.setRedYellowGreenState(traffic_light_id7, phases7[current_phase_index3]["state"])
                traci.trafficlight.setRedYellowGreenState(traffic_light_id8, phases8[current_phase_index3]["state"])
                traci.trafficlight.setRedYellowGreenState(traffic_light_id9, phases9[current_phase_index3]["state"])
                traci.trafficlight.setRedYellowGreenState(traffic_light_id10, phases10[current_phase_index3]["state"])
                traci.trafficlight.setRedYellowGreenState(traffic_light_id11, phases11[current_phase_index3]["state"])
                traci.trafficlight.setRedYellowGreenState(traffic_light_id12, phases12[current_phase_index3]["state"])
                traci.trafficlight.setRedYellowGreenState(traffic_light_id13, phases13[current_phase_index3]["state"])
                traci.trafficlight.setRedYellowGreenState(traffic_light_id14, phases14[current_phase_index3]["state"])

    traci.close()

# Ruta al ejecutable de SUMO
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Please declare environment variable 'SUMO_HOME'")

# Iniciar la simulación
traci.start(["sumo-gui", "-c", "avhuaynacapac.sumo.cfg"])

# Ejecutar la lógica de control
run()

