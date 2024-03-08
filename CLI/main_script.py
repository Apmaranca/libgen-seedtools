import helper_module

// IPFS initialization
helper_module.helper_function()
settings = Settings("settings.ini")  # Make sure to import the Settings class
ipfs_client = IPFSClient(settings)

# Your program logic here


// Do at program exit
ipfs_client = IPFSClient()
ipfs_client.stop_ipfs_daemon()

