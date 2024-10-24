#!/bin/bash
for pid in $(ps aux | grep 'libgpiod_pulsein' | awk '{print $2}'); do kill -9 $pid; done