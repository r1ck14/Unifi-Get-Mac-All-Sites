# Unifi-Get-Mac-All-Sites
A Python 3 script that allows you to get a list of all mac addresses from devices across all sites within Unifi

When using the Unifi controller, there is no way to see a list of all the devices from every site. It can be useful to be able to search for a specific MAC
address without having to go site by site. This script allows you to login to your Unifi portal and will automatically generate a .txt file with all the MAC
addresses listed by site.

Included is a .exe file which can just be run if you don't want to install Python and run the script yourself. 

Text file will be created in the same directory as the .exe or .py file.

Thanks to https://github.com/DataKnox who created the script that this is based on. The original script is here: https://github.com/DataKnox/CodeSamples/blob/master/Python/Networking/Ubiquiti/ubnt.py
