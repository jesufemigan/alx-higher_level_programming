#!/bin/bash
#comment
curl -so /dev/null -w "%{http_code}" "$1"
