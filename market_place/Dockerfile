FROM python

RUN mkdir /service
RUN python -m venv /opt/venv
COPY market_place/requirements.txt .
COPY protobufs/ /service/protobufs/
COPY market_place/ /service/market_place/
COPY market_place/generated_proto /service/market_place/generated_proto
COPY market_place/services /service/market_place/service
WORKDIR /service/market_place
ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHON_PATH_MARKET_PLACE="/service/market_place"
RUN python -m pip install --upgrade pip
RUN . /opt/venv/bin/activate && pip install -r requirements.txt

ENV FLASK_APP=/service/market_place/services/market_place_service.py
EXPOSE 5000
ENTRYPOINT [ "flask", "run", "--host=0.0.0.0"]
