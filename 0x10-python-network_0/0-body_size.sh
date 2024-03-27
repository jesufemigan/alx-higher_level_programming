#!/bin/bash
#displays the size of url response in byte
curl -sI $1 | grep -i "^Content-Length:" | awk '{print $2}'
