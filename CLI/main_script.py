import helper_module

// IPFS initialization
helper_module.helper_function()
ipfs_client = IPFSClient()
ipfs_client.start_ipfs_daemon()


# Your program logic here


// Do at program exit
ipfs_client = IPFSClient()
ipfs_client.stop_ipfs_daemon()
