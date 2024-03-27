#!/usr/bin/bash
#displays the size of url response in byte
curl -sI $1 | tail -n 2 | awk '{print $2}' | head -n 1
