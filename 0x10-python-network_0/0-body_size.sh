#!/usr/bin/env bash
#script that outputs the bytes response contains
curl -s "$1" | wc -c
