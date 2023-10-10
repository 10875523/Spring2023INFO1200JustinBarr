#! bin/usr/env python3
#Name: Justin Barr
#Class: INFO 1200
#Section: X01
#Professor: Crandall
#Date: 2/21/2023
#Project #: MO5_P2_converter
#I declare that the source code contained in this assignment was written solely by me.
#I understand that copying any source code, in whole or in part, 
#constitutes cheating, and that I will receive a zero on this project
#if I am found in violation of this policy.

def to_meters(feet):
    '''
    Define function which takes in parameter feet and will convert it to meters returning that value
    '''
    meters = feet * 0.3048
    return meters

def to_feet(meters):
    ''' 
    Define function which takes in parameter meters and will convert it to feet returning that value
    '''
    feet = meters / 0.3048
    return feet