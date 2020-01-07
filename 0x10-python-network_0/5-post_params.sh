#!/bin/bash
# Script that sends a Post request to a URL
curl -sH -X POST "email:hr@holbertonschool.com%subject:I will always be here for PLD" "$1"
