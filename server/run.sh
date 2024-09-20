#!/bin/bash

BACKEND_HOST=${BACKEND_HOST:=0.0.0.0}
BACKEND_PORT=${BACKEND_PORT:=42000}

fastapi run main.py --host=$BACKEND_HOST --port=$BACKEND_PORT
