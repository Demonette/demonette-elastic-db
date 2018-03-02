#!/usr/bin/env bash
source .env
docker-compose up -d
sleep 30
curl -XPUT 'http://localhost:'${PORT}'/_xpack/license' -H "Content-Type: application/json" -d @license.json
sleep 10
python deploy.py
