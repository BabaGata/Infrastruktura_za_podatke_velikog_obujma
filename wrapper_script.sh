#!/bin/bash

exec python3 ./server.py &
exec python3 ./client.py &
exec python3 ./producer.py &
exec python3 ./consumer.py