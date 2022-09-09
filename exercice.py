#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    result = math.sqrt(a)
    return result


def square(a: float) -> float:
    result = a*a
    return result


def average(a: float, b: float, c: float) -> float:
    result = (a+b+c)/3
    return result


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    totalDeg = angle_degs + (angle_mins/60) + (angle_secs/3600) #Calcule le nbr de degrés totaux
    result = math.radians(totalDeg) #Transforme les degrés en radians
    return result


def to_degrees(angle_rads: float) -> tuple:
    nbrDeSecTotal = angle_rads*((3600*180)/math.pi) #Calcule le nbr de sec total de l'angle
    nbrSec = nbrDeSecTotal%60 #Calcule le nbr de sec (nbr entier)
    nbrDeSecTotal = nbrDeSecTotal - nbrSec
    nbrMin = (nbrDeSecTotal/60)%60 #Calcule le nbr de min (nbr entier)
    nbrDeSecTotal = nbrDeSecTotal - (nbrMin*60)
    nbrDeg = nbrDeSecTotal/(60*60) #Calcul le nbr de degrés
    return nbrDeg, nbrMin, nbrSec


def to_celsius(temperature: float) -> float:
    result = (temperature-32)/1.8
    return result


def to_farenheit(temperature: float) -> float:
    result = (temperature*1.8)+32
    return result


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(100, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
