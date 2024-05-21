import os
import subprocess
import platform

def check_ssh_key():
    ssh_key_path = os.path.expanduser("~/.ssh/id_ed25519.pub")
    return os.path.isfile(ssh_key_path)

def generate_ssh_key(email):
    cmd = f'ssh-keygen -t ed25519 -C "{email}" -f ~/.ssh/id_ed25519 -N ""'
    subprocess.run(cmd, shell=True, check=True)
    print("SSH key generated successfully.")

def start_ssh_agent():
    if platform.system() == "Windows":
        cmd = 'start-ssh-agent.cmd'
    else:
        cmd = 'eval "$(ssh-agent -s)"'
    subprocess.run(cmd, shell=True, check=True)
    print("SSH agent started.")

def add_ssh_key_to_agent():
    cmd = 'ssh-add ~/.ssh/id_ed25519'
    subprocess.run(cmd, shell=True, check=True)
    print("SSH key added to SSH agent.")

def get_ssh_key():
    with open(os.path.expanduser("~/.ssh/id_ed25519.pub"), 'r') as file:
        return file.read().strip()

def main():
    email = input("Enter your GitHub email address: ")
    
    if check_ssh_key():
        print("An existing SSH key was found.")
    else:
        print("No existing SSH key found. Generating a new one.")
        generate_ssh_key(email)
    
    start_ssh_agent()
    add_ssh_key_to_agent()
    
    ssh_key = get_ssh_key()
    print("\nCopy the following SSH key and add it to your GitHub account:")
    print(ssh_key)
    print("\nTo add the SSH key to your GitHub account:")
    print("1. Log in to GitHub.")
    print("2. Go to Settings > SSH and GPG keys.")
    print("3. Click 'New SSH key', give it a title, and paste the SSH key.")
    print("4. Click 'Add SSH key'.")

if __name__ == "__main__":
    main()
