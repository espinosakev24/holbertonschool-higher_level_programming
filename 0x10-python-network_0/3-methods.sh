#!/bin/bash
# Script that sends a OPTION request and display allow methods
curl -is -X OPTIONS $1 | sed -n "/Allow:/p" | cut -d ":" -f 2
