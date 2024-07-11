#!/bin/bash

# Comando para convertir XML a CSV
python3 /opt/sumo/tools/xml/xml2csv.py -s , fcd2.xml
python3 /opt/sumo/tools/xml/xml2csv.py -s , tripinfo2.xml

# Mensaje para indicar que el script ha terminado
echo "Conversión de XML a CSV completada."

