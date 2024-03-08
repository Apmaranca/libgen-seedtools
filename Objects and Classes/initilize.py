import configparser

class Settings:
    def __init__(self, config_file="settings.ini"):
        self.config = configparser.ConfigParser()
        self.config_file = config_file
        self.read_config()

    def read_config(self):
        """Reads the configuration file and stores the settings."""
        # Ensure the file is read as UTF-8
        with open(self.config_file, 'r', encoding='utf-8') as f:
            self.config.read_file(f)

    def get(self, section, option, fallback=None):
        """Retrieves a value for the given section and option with an optional fallback."""
        return self.config.get(section, option, fallback=fallback)

# Example usage
settings = Settings("settings.ini")
daemon_host = settings.get('IPFS', 'DaemonHost', fallback='localhost')
print(f"IPFS Daemon Host: {daemon_host}")
