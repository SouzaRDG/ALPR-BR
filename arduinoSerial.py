#!/usr/bin/env python

import serial
import time

try:
    ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0)
except:
    print("\nNão foi possível se conectar a porta '/dev/ttyACM0'")
    try:
        ser = serial.Serial('/dev/ttyACM1', 9600, timeout=0)
    except:
        print("\nNão foi possível se conectar a porta '/dev/ttyACM1'"
              "\n\nNÃO FOI POSSÍVEL SE CONECTAR AO ARDUINO! AS LEITURAS DE PLACAS AINDA VÃO OCORRER,"
              "\nPORÉM A CANCELA NÃO SERÁ LEVANTADA E NÃO HAVERA UM FEEDBACK PELOS LED'S\n")


def openGate():

    try:
        ser.write(b'1')
        time.sleep(0.01)
    except:
        print("\nNão possivel se conectar ao arduino para levantar a cancela\n"
              "Verifique se a porta serial está bloqueada\n")

def warningLED():

    try:
        ser.write(b'3')
        time.sleep(0.01)
    except:
        print("\n~~ATENÇÃO~~\nNÃO FOI POSSIVEL FECHAR E TRAVAR A CANCELA AUTOMATICAMENTE\n"
              "~~ATENÇÃO~~\n")

def attentionLED():

    try:
        ser.write(b'2')
        time.sleep(0.01)
    except:
        print("\nNÃO FOI POSSIVEL FECHAR E TRAVAR A CANCELA AUTOMATICAMENTE\n"
              "FIQUE ATENTO...\n")