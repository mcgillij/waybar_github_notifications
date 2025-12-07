#Adding it to your waybar

**~/.config/waybar/config**
``` json
...
  "modules-center": [
    "hyprland/window",
    "cpu",
    "memory",
    "network",
    "custom/gh", // < add it here
...
"custom/gh": {
	"format": "{text}",
	"return-type": "json",
	"exec": "$HOME/.config/waybar/custom_modules/gh_notifications.sh",
	"interval": 300,
}
...
```

## Installing

clone the repo into `~/.config/waybar/custom_modules/` and then **poetry install**

## Put your github token in the shell script, or read it in from an env var etc

**gh_notifications.sh**
``` bash

#!/bin/bash

cd "$(dirname "$0")"
poetry run python waybar_gh_notifications.py <yourtokenhere>

```

## Adding some color

``` css

#custom-gh {
    color: rgba(0, 255, 0, 1);
}

```
