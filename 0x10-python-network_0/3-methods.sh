#!/bin/bash
#comment
 curl -sI "$1" | grep -oP 'Allow: \K.*' | awk '{print}'
