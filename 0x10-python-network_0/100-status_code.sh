#!/bin/bash
# script that returns status code
curl -sI $1 | grep HTTP/2 | cut -d " " -f 2
