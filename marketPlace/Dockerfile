FROM python

RUN mkdir /service
RUN python -m venv /opt/venv
COPY marketPlace/requirements.txt .
COPY protobufs/ /service/protobufs/
COPY marketPlace/ /service/marketPlace/
WORKDIR /service/marketPlace
ENV PATH="/opt/venv/bin:$PATH"
RUN python -m pip install --upgrade pip
RUN . /opt/venv/bin/activate && pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I ../protobufs --python_out=. \
           --grpc_python_out=.  ../protobufs/recommendation.proto

EXPOSE 5000
ENV FLASK_APP=marketplace.py
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]
