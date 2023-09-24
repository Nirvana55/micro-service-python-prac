FROM python

RUN mkdir /service
RUN python -m venv /opt/venv
COPY marketPlace/requirements.txt .
COPY protobufs/ /service/protobufs/
COPY marketPlace/ /service/marketPlace/
COPY recommendations/generated /service/recommendations/generated
WORKDIR /service/marketPlace
ENV PATH="/opt/venv/bin:$PATH"
RUN python -m pip install --upgrade pip
RUN . /opt/venv/bin/activate && pip install -r requirements.txt

ENV FLASK_APP=marketplace.py
EXPOSE 5000
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]
