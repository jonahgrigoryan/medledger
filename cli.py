
from bridge.models import Patient, Prescriber, Pharmacy, Registrar
from bridge.simulate import Simulator
import argparse
import json
import os
import time

import solc



BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def compile():
    """Compiles all Solidity smart contracts.
    """
    if not os.path.exists('build'):
        os.mkdir(os.path.join('build'))

    standard_json = {
        'language': 'Solidity',
        'sources': {},
        'settings':
        {
            'outputSelection': {
                '*': {
                    '*': [
                        'metadata', 'evm.bytecode', 'evm.bytecode.sourceMap'
                    ]
                }
            }
        }
    }

    contracts = [f for f in os.listdir('contracts') if f.endswith('.sol')]
    for contract in contracts:
        with open(os.path.join('contracts', contract)) as file:
            source = file.read()
            standard_json['sources'][contract] = {'content': ''}
            standard_json['sources'][contract]['content'] = source

    compiled_sol = solc.compile_standard(standard_json)
    with open(os.path.join('build', 'contracts.json'), 'w') as file:
        json.dump(compiled_sol, file, indent=4)

    for contract in contracts:
        name = contract.replace('.sol', '')
        bytecode = compiled_sol['contracts'][contract][name]['evm']['bytecode']['object']
        abi = json.loads(compiled_sol['contracts'][contract][name]['metadata'])['output']['abi']

        with open(os.path.join('build', name + '.abi'), 'w') as file:
            json.dump(abi, file, indent=4)
        with open(os.path.join('build', name + '.bin'), 'w') as file:
            file.write(bytecode)





def clean():
    """Removes all Solidity smart contract compilation files.
    """
    if os.path.exists('build'):
        files = os.listdir(os.path.join('build'))
        for file in files:
            os.remove(os.path.join('build', file))

def run_ganache():
    """Runs the Ganache test blockchain locally. Solidity smart
    contracts must be compiled first.
    """
    path = os.path.join('..', 'node_modules', '.bin', 'ganache-cli')
    os.system(f'osascript -e \'tell app "Terminal" to do script "{path}"\'')


def run_server():
    """Runs the Django web app server locally. Ganache must be running
    and a Registrar smart contract deployed.
    """
    cwd = os.getcwd()
    path = os.path.join(cwd, 'app', 'manage.py')
    os.system(f'osascript -e \'tell app "Terminal" to do script "python {path} runserver"\'')



def bridge():
    """Deploys a new registrar contract. Ganache must be running."""
    venv_path = "/Users/jonahkesoyan/Downloads/MedLedger/venv/bin/activate"
    path = os.path.join(BASE_DIR, 'bridge', 'bridge_module.py')
    command = f'source {venv_path} && python3 {path}'
    
    # Create a simulator instance
    simulator = Simulator(50, 100, 0.8, 0.16, 0.04)
    # Run the simulation
    simulator.cycle()
    
    registrar = Registrar()

    os.system(f'osascript -e \'tell app "Terminal" to do script "{command}"\'')


def build():
    """Compiles all Solidity smart contracts, runs the Ganache test
    blockchain locally, deploys a new registrar contract, and runs the
    Django web app server locally.
    """
    clean()
    compile()
    run_ganache()
    time.sleep(3)
    bridge()
    run_server()


if __name__ == '__main__':
    ACTIONS = {
        'compile': compile,
        'clean': clean,
        'runserver': run_server,
        'runganache': run_ganache,
        'bridge': bridge,
        'build': build,
    }

    argparser = argparse.ArgumentParser()
    argparser.add_argument('--action', choices=ACTIONS.keys(), required=True)
    args = argparser.parse_args()
    function = ACTIONS[args.action]
    function()
