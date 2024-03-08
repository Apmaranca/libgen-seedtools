import subprocess
import atexit
import time

class IPFSClient:
    def __init__(self, settings):
        self.settings = settings
        # Ensure the daemon is stopped properly on exit
        atexit.register(self.stop_ipfs_daemon)
        self.daemon_process = None
        self.initialize_daemon()

    def run_command(self, command):
        """
        Runs a command in the subprocess and returns the output.
        Throws an exception if the command execution fails.
        """
        result = subprocess.run(command, capture_output=True, text=True)
        if result.stderr:
            raise Exception(result.stderr)
        return result.stdout

    def initialize_ipfs(self):
        """
        Initializes the IPFS local repository if not already initialized.
        """
        try:
            print("Checking if IPFS is initialized...")
            self.run_command(["ipfs", "config", "show"])
            print("IPFS is already initialized.")
        except Exception as e:
            print("Initializing IPFS...")
            self.run_command(["ipfs", "init"])
            print("IPFS initialized.")

    def start_ipfs_daemon(self):
        """
        Starts the IPFS daemon.
        """
        try:
            print("Starting IPFS daemon...")
            self.daemon_process = subprocess.Popen(["ipfs", "daemon"])
            # Use the settings for initial delay
            time.sleep(self.settings.get('IPFS', 'InitialDelay', fallback=5))
            print("IPFS daemon is running.")
        except FileNotFoundError:
            print("Error: IPFS executable not found. Please ensure IPFS is installed and in your PATH.")
        except Exception as e:
            print(f"An unexpected error occurred while starting the IPFS daemon: {e}")

    def stop_ipfs_daemon(self):
        """
        Stops the IPFS daemon.
        """
        if self.daemon_process:
            try:
                print("Stopping IPFS daemon...")
                self.daemon_process.terminate()  # Sends a SIGTERM signal
                self.daemon_process.wait()  # Wait for the process to terminate
                print("IPFS daemon stopped.")
            except Exception as e:
                print(f"An error occurred while stopping the IPFS daemon: {e}")

    def initialize_daemon(self):
        """
        Initializes and starts the IPFS daemon.
        """
        self.initialize_ipfs()
        self.start_ipfs_daemon()

    def upload(self, file_path):
        # Implement file upload to IPFS
        pass

    def download(self, file_id):
        # Implement file download from IPFS
        pass

    def transfer_to(self, destination, file_id):
        # Implement transferring IPFS file to another file-sharing protocol
        pass

# Example usage, assuming 'settings' is an instance of the Settings class created earlier
settings = Settings("settings.ini")  # Make sure to import the Settings class
ipfs_client = IPFSClient(settings)
