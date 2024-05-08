#!/usr/bin/env bash
/usr/local/bin/docker-entrypoint.sh mysqld > /dev/null 2>&1 & disown
python3 app.py
