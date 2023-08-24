#!/Users/jonahkesoyan/Downloads/MedLedger/venv/bin/python

import json
import os

from web3 import Web3

BASE_DIR_BRIDGE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



class NotCompiledException(Exception):
    """Raised when Solidity contracts are not compiled. A build must be
    compiled to prevent this exception.
    """
    pass


class GanacheConnectionException(Exception):
    """Raised when Web3 cannot connect to Ganache, usually due to
    Ganache not being run previous to attempted connection.
    """
    pass


try:
    with open(os.path.join(BASE_DIR_BRIDGE, 'build', 'Registrar.abi'), 'r') as file:
        REGISTRAR_ABI = json.load(file)
    with open(os.path.join(BASE_DIR_BRIDGE, 'build', 'Registrar.bin'), 'r') as file:
        REGISTRAR_BIN = file.read()
    with open(os.path.join(BASE_DIR_BRIDGE, 'build', 'Patient.abi'), 'r') as file:
        PATIENT_ABI = json.load(file)
    with open(os.path.join(BASE_DIR_BRIDGE, 'build', 'Patient.bin'), 'r') as file:
        PATIENT_BIN = file.read()
    with open(os.path.join(BASE_DIR_BRIDGE, 'build', 'Prescriber.abi'), 'r') as file:
        PRESCRIBER_ABI = json.load(file)
    with open(os.path.join(BASE_DIR_BRIDGE, 'build', 'Prescriber.bin'), 'r') as file:
        PRESCRIBER_BIN = file.read()    
    with open(os.path.join(BASE_DIR_BRIDGE, 'build', 'Pharmacy.abi'), 'r') as file:
        PHARMACY_ABI = json.load(file)
    with open(os.path.join(BASE_DIR_BRIDGE, 'build', 'Pharmacy.bin'), 'r') as file:
        PHARMACY_BIN = file.read()
    with open(os.path.join(BASE_DIR_BRIDGE, 'build', 'Prescription.abi'), 'r') as file:
        PRESCRIPTION_ABI = json.load(file)
    with open(os.path.join(BASE_DIR_BRIDGE, 'build', 'Prescription.bin'), 'r') as file:
        PRESCRIPTION_BIN = file.read()

except Exception as e:
    raise NotCompiledException()



try:
    w3 = Web3(Web3.HTTPProvider('http://localhost:8545'))
except:
    raise GanacheConnectionException()