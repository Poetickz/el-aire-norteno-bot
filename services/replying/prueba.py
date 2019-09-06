#!/usr/bin/env python
# Este archivo usa el encoding: utf-8
print ("ñññ")


def switchvalue(datos):
    switcher = {
        0: "Lo siento, no te entendi, vuelve a preguntar por favor compa",
        1..50: "La calidad del aire en la área metropolitana de Monterrey es de "+datos+ " AQI El aire está hermoso pariente, disfruta tu día compa.",
        51..100: "La calidad del aire en la área metropolitana de Monterrey es de "+datos+ " AQI El aire está regular pero no es dañino, una carnita más y nos lleva la @$%&%.",
        101..150: "La calidad del aire en la área metropolitana de Monterrey es de "+datos+ " AQI El aire está malo, evita realizar cualquier esfuerzo fuerte compa.",
        151..200: "La calidad del aire en la área metropolitana de Monterrey es de "+datos+ " AQI El aire está malisimo, igual que el reggeton.",
        201..300: "La calidad del aire en la área metropolitana de Monterrey es de "+datos+ " AQI El aire está horrible, tener la vida de Demmi Lovato es mejor.",
        301..1000:"Lo siento, no te entendi, vuelve a preguntar por favor compa",
    }
    return val
dato = 44
print(switchvalue(datos))