#!/bin/sh
set -ex

uwsgi --socket 0.0.0.0:$PORT --protocol=http -w main:app --enable-threads --thunder-lock
