# CT vs VM
ct is lightweighter
```Bash
pveam update
pveam available
pveam available --section system
pveam download local debian-10.0-standard_10.0-1_amd64.tar.gz
```

In order to able to SSH to ubuntu:
```shell
nano /etc/ssh/sshd_config

LoginGraceTime 120
PermitRootLogin yes
StrictModes yes

#optional
PasswordAuthentication yes
```

To show default gateway
```shell
 ip route show
 ip a
```

Disable powerbutton action
```bash
nano /etc/systemd/logind.conf

#change
#HandlePowerKey=poweroff
to 
HandlePowerKey=ignore

sudo systemctl restart systemd-logind

# option 2
nano /etc/acpi/events/

event=<acpi_event_code>
action=<script_to_call>
```

