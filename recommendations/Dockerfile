FROM python


RUN mkdir /service

RUN python -m venv /opt/venv
COPY recommendations/requirements.txt .
COPY protobufs/ /service/protobufs/
COPY recommendations/ /service/recommendations/
COPY recommendations/generated /service/recommendations/generated
WORKDIR /service/recommendations
ENV PATH="/opt/venv/bin:$PATH"
RUN python -m pip install --upgrade pip
RUN . /opt/venv/bin/activate && pip install -r requirements.txt

EXPOSE 50051
ENTRYPOINT [ "python", "recommendations.py" ]