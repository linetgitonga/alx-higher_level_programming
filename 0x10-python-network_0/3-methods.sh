#!/bin/bash

curl -sI "$1" | grep "Allow:" | sed -ne 's/^Allow: //p'
