#  Hardware Acceleration Tutorial On NVIDIA GPU
If below error shown
- libnvcuvid1 but it is not installable
- libnvidia-encode1 but it is not installable

Then we need to install

    wget https://developer.download.nvidia.com/compute/cuda/repos/debian12/x86_64/cuda-keyring_1.1-1_all.deb

    sudo dpkg -i cuda-keyring_1.1-1_all.deb

    sudo add-apt-repository contrib

    apt update
    sudo apt install -y libnvcuvid1 libnvidia-encode1

**NOTE**
If error add-apt-repository command not found
    
    apt install software-properties-common