#!/bin/bash

source env/bin/activate
cd "$1"
echo "$2"
python -m grpc_tools.protoc -I ../protobufs --python_out="$2" --grpc_python_out="$2" ../protobufs/recommendation.proto;

