# CuulFan
Simple python script to enable/disable fan to cool Raspberry Pi 4

Each 15 seconds it checks current temperature and enables or disables an external FAN on pin 12.

Systemd is used to run it. Containesd makefile is just used install script and control it by systemctl.

Parameters for make are:
* install
* link (can be used instead of install, but systemctl disable will remove symlink)
* remove
* enable
* disable
* start
* stop
* restart
* status


Note: To fit to service file, needs to be cloned in /home/pi/.
