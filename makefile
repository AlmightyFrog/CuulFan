########################################
# Makefile for handing systemd service #
########################################

service = CuulFan.service
path = /etc/systemd/system/

install:
	sudo cp $(service) $(path)$(service)

link:
	sudo ln -s $(shell pwd)/$(service) $(path)$(service)

remove:
	sudo rm $(path)$(service)

enable:
	sudo systemctl enable $(service)

disable:
	sudo systemctl disable $(service)

start:
	sudo systemctl start $(service)

stop:
	sudo systemctl stop $(service)

restart:
	sudo systemctl restart $(service)

status:
	systemctl status $(service)
