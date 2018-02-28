#!/usr/bin/env bash
docker compose up -d
curl -XPUT -u elastic 'http://localhost:9999/_xpack/license' -H "Content-Type: application/json" -d @license.json
python deploy.py
