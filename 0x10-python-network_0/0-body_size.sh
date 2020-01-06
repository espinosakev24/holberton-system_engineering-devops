#!/usr/bin/env bash
# Request to a URL and printing only de content size in bytes
curl -sI $1 | sed -n "/Content-Length/p" | cut -d " " -f 2
