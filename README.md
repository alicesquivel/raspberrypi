All Raspberry Pi setup.

# Enable wifi
In the boot partition, simple create an empty file with the name ssh.

Edit the file wpa_supplicant.conf. Change \ to your ISO country code found here (for the United States, this is US). Change \ to the SSID of your WiFi network and \ to the WiFi network's password.
Find the ```raspberrypi/wpa_supplicant.conf``` in this repo. 

# To set up a virtual environment for Python projects on your Raspberry Pi, follow these steps:
Starting with the October 10, 2023 Bookworm release of the Raspberry Pi OS, the use of Python Virtual Environments (venv) when pip installing packages is required. **No more sudo pip**. This will break things and require learning new things. 

Python Virtual Environment Usage on Raspberry Pi https://learn.adafruit.com/python-virtual-environment-usage-on-raspberry-pi/overview 
 
## Install virtualenv if not already installed:
```
sudo apt update
sudo apt install python3-venv
```
Navigate to your project directory:
```
cd /path/to/your/project
```

## Create a virtual environment:
```
python3 -m venv env
```
This will create a directory named env (you can replace env with any name you prefer).

Activate the virtual environment:
```
source env/bin/activate
```
Your terminal prompt should change to indicate that you are now working inside the virtual environment.

## Install dependencies:
Once inside the virtual environment (env), you can install Python packages as usual using pip. For example:
```
pip install package-name
```
## Deactivate the virtual environment:
To exit the virtual environment when you're done working on your project, use the deactivate command:
```
deactivate
```
Your terminal prompt will return to normal, indicating that you've exited the virtual environment.





