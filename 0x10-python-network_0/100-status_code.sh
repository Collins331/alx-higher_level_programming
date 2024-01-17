#!/bin/bash
#script that displays the status code
curl  -s -o /dev/null -w "${http_code}" "$1"
