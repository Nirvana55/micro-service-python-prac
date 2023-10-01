#!/bin/bash

source env/bin/activate
cd "$1"
python -m grpc_tools.protoc -I ../protobufs --python_out=generated_${1} --grpc_python_out=generated_${1} ../protobufs/recommendation.proto;
