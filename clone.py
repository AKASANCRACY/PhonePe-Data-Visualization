import subprocess
import os

def Clone():
    print("From")
    # Specify the URL of the repository you want to clone
    repository_url = 'https://github.com/PhonePe/pulse.git'

    # Specify the target directory where you want to clone the repository
    target_directory = str(os.path.abspath(os.getcwd()))
    print(target_directory)

    # Run the git clone command using subprocess
    subprocess.run(['git', 'clone', repository_url, target_directory+"/temp"])
