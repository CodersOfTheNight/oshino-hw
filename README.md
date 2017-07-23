oshino-hw
=====================
An agent to retrieve HW info

For more info, refer to parent project [Oshino](https://github.com/CodersOfTheNight/oshino)

Config
======
- `paths` - a list of pathes to measure disk usage. Eg. `/` would be used in unix to find free space on root. `C:\` can be useful when using Windows

Example config
--------------
```yaml
---
interval: 10
loglevel: DEBUG
riemann:
  host: localhost
  port: 5555
agents:
  - name: hw
    module: oshino_hw.agent.HWAgent
    tag: hw
    paths:
      - /
      - /mnt/external-data/
```
