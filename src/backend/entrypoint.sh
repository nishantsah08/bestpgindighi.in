#!/bin/sh
set -e

uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}
