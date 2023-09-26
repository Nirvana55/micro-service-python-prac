#!/bin/bash

source env/bin/activate
cd "$1"
python -m grpc_tools.protoc -I ../protobufs --python_out=generated --grpc_python_out=generated ../protobufs/recommendation.proto;