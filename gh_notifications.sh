#!/bin/bash

cd "$(dirname "$0")"
poetry run python waybar_gh_notifications.py <yourtokenhere>
