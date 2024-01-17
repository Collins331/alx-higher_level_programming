#!/bin/bash
#script that lists the method that server accepts
curl -sI "$1" | grep Allow | cut -c 8-
