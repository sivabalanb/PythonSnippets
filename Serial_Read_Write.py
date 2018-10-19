import time
import sys
import binascii
import logging
import os
import serial
import crcmod
import pickle
import time

def initialize_serial_port(portnum):
	try:		
		ser = serial.Serial(
			port=portnum,
			baudrate=9600,
			parity=serial.PARITY_ODD,
			stopbits=serial.STOPBITS_TWO,
			bytesize=serial.SEVENBITS
			)
	except Exception as e:
		logging.error("\nError in initialize_serial_port:\t"+str(e))
		
def send_input(to_send):
	try:
		logging.info("\nCommand received in send_input:\t%s" , str(to_send))
		ser.write(to_send)
	except Exception as e:
		logging.error("\nError in send_input:\t"+str(e))
		
def receive_response():
	try:
		receivedBuffer= ser.readline()
	except Exception as e:
		logging.error("\nError in receive_response:\t"+str(e))

def read_response():
	try:
		response = receive_response()
		logging.info("Received response:\t"+str(response))
	except Exception as e:
		logging.error("Error while reciving the response:\t"+str(e))

def main():

	portnum = input("Enter initialize_serial_port")
	initialize_serial_port(portnum)
	send_input()
	read_response()

if __name__ == "__main__":
	try:
		main()
	except Exception as e:
		logging.error("\nError in main funnction:\t"+str(e))