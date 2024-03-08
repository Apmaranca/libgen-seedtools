import requests
import json
import subprocess
import atexit

class TransmissionRPC:
    def __init__(self, host='localhost', port=9091, username=None, password=None):
        self.url = f'http://{host}:{port}/transmission/rpc'
        self.session_id = None
        self.auth = (username, password) if username and password else None
        self.headers = {"content-type": "application/json"}

        # Start the Transmission daemon
        self.start_daemon()

        # Ensure the daemon is stopped when the program exits
        atexit.register(self.stop_daemon)

    def _send_request(self, method, arguments=None):
        # Implementation remains the same as previously described...

    def add_torrent(self, torrent_url):
        # Implementation remains the same as previously described...

    def list_torrents(self):
        # Implementation remains the same as previously described...

    def remove_torrent(self, torrent_id, delete_data=False):
        # Implementation remains the same as previously described...

    def start_daemon(self):
        try:
            subprocess.run(["transmission-daemon"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to start Transmission daemon: {e}")

    def stop_daemon(self):
        try:
            subprocess.run(["transmission-remote", "--exit"], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Failed to stop Transmission daemon: {e}")

# Example usage
if __name__ == "__main__":
    rpc = TransmissionRPC(username="your_username", password="your_password")
    # Use the rpc object as needed...
