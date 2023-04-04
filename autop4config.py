from P4 import P4, P4Exception

import getpass
import os
import pprint
import socket
import toml

# If the P4CONFIG environment variable isn't set, report an error and skip this workspace
p4configfilename = os.environ.get("P4CONFIG")
if not p4configfilename:
    print("Error: P4CONFIG environment variable is not set. Please set it before running this!")
    print("(You may then have to restart the shell.)")
    exit(1)

# Load configuration from TOML file
if not os.path.exists("autop4config.conf"):
    print("Error: autop4config.conf is missing. Please create it! You can copy it from autop4config.conf.example")
    exit(1)
with open("autop4config.conf", "r") as f:
    config = toml.load(f)

# Create a P4 instance and set the configuration options
p4 = P4()
p4.port = config["p4"]["port"]
p4.user = config["p4"]["user"]

# Prompt for password
p4.password = getpass.getpass(prompt="Password for {}: ".format(p4.user))

try:
    # Connect to the Perforce server
    p4.connect()

    print("Connected successfully")

    # Get the list of workspaces for the current user
    workspaces = p4.run("clients", "-u", p4.user)
    for workspace in workspaces:
        #pprint.pprint(workspace)

        # Check if the workspace is on the current computer (case-insensitive)
        if socket.gethostname().lower() != workspace["Host"].lower():
            print(f"{workspace['client']}: Locked to a different computer.")
            continue
        
        # Verify the directory exists before creating the p4config file
        if not os.path.exists(workspace["Root"]):
            print(f"{workspace['client']}: Directory {workspace['Root']} missing, not writing a config file.")
            continue

        # Get the p4config filename for the workspace
        config_path = os.path.join(workspace["Root"], os.environ.get("P4CONFIG", ".p4config"))

        # Create a p4config file for each workspace
        with open(config_path, "w") as f:
            f.write("P4PORT={}\n".format(p4.port))
            f.write("P4USER={}\n".format(p4.user))
            f.write("P4CLIENT={}\n".format(workspace["client"]))
        
        print(f"{workspace['client']}: {config_path} written.")

    print("Finished")

finally:
    # Disconnect from the Perforce server
    p4.disconnect()