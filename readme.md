# Fucking auto reboot telecom router!

# config example

```json
{
  "url": "http://192.168.1.1/",
  "username": "telecomadmin",
  "passwd": "telecomadmin60603885",
  "driver_executable_path": "bin/geckodriver",
  "loop_seconds": "86400"
}
```

# deploy

```bash

# natas @ natas-pc in ~/usr/telecom_reboot on git:master x [14:36:08]
$ sudo cp fuck_telecom_router_reboot.service /etc/systemd/system/

# natas @ natas-pc in ~/usr/telecom_reboot on git:master x [14:38:36]
$ sudo systemctl start fuck_telecom_router_reboot.service

# natas @ natas-pc in ~/usr/telecom_reboot on git:master x [14:38:42]
$ sudo systemctl enable fuck_telecom_router_reboot.service

# natas @ natas-pc in ~/usr/telecom_reboot on git:master x [14:38:45]
$ sudo systemctl status fuck_telecom_router_reboot.service

# natas @ natas-pc in ~/usr/telecom_reboot on git:master x [14:38:53]
$
```
