#!/bin/bash


gunicorn_cmd="gunicorn"
config_file="config.wsgi"
bind_address="0.0.0.0:8080"
workers=3
gunicorn_command="$gunicorn_cmd --bind $bind_address -w $workers $config_file"
exec $gunicorn_command

