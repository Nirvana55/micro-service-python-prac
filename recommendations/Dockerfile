FROM python


RUN mkdir /service

RUN python -m venv /opt/venv
COPY recommendations/requirements.txt .
COPY protobufs/ /service/protobufs/
COPY recommendations/ /service/recommendations/
COPY recommendations/generated_recommendations /service/recommendations/generated_recommendations
COPY recommendations/services /service/recommendations/services
COPY recommendations/prisma /service/recommendations/prisma
COPY recommendations/prisma /service/recommendations/helpers
COPY recommendations/prisma /service/recommendations/controllers
WORKDIR /service/recommendations
ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHON_PATH_RECOMMENDATIONS="/service/recommendations"
RUN python -m pip install --upgrade pip
RUN . /opt/venv/bin/activate && pip install -r requirements.txt
EXPOSE 50051
ENTRYPOINT [ "python", "services/recommendation.py" ]