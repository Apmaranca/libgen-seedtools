import helper_module
import click
import configparser
import subprocess
import atexit

# Function to read configuration
def read_configuration(file_path='configuration.ini'):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config

# Updated daemon start functions to accept parameters
def start_transmission_daemon(transmission_config):
    try:
        subprocess.run(["transmission-daemon", *transmission_config], check=True)
        print("Transmission daemon started successfully.")
    except subprocess.CalledProcessError:
        print("Failed to start Transmission daemon. It may already be running.")

def start_ipfs_daemon(ipfs_config):
    try:
        subprocess.run(["ipfs", "daemon", *ipfs_config], check=True)
        print("IPFS daemon started successfully.")
    except subprocess.CalledProcessError:
        print("Failed to start IPFS daemon. It may already be running.")

@click.command()
@click.option('--nt', is_flag=True, help='Do not initialize the torrent daemon.')
@click.option('--ni', is_flag=True, help='Do not initialize the IPFS daemon.')
def main(nt, ni):
    config = read_configuration()

    transmission_config = config['Transmission'].get('parameters', '').split()
    ipfs_config = config['IPFS'].get('parameters', '').split()

    if not nt:
        start_transmission_daemon(transmission_config)
        atexit.register(lambda: subprocess.run(["transmission-remote", "--exit"], check=True))
    else:
        print("Skipping Transmission daemon initialization.")

    if not ni:
        start_ipfs_daemon(ipfs_config)
    else:
        print("Skipping IPFS daemon initialization.")

    print("CLI app is running. Press Ctrl+C to exit.")

if __name__ == "__main__":
    main()
