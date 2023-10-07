This is only a practice run for developing microservices with GRPC.

Two microservices communicate with each other in the following project.

Recommendations and the MarketPlace

- Marketplace is a very simple web app that presents the user a list of books.
- Recommendations is a microservice that displays a list of books that the user might be interested in.

I produced an ExcailDraw file in which I described GRPC and its flow

DM me for the file, if you need it.

This repository is currently being worked on.

To generate client to access the database:

```
prisma init
prisma db push
prisma generate

```

Create a separate docker for your db and run it in background. Then you can run two microservices.

You can make rpc call from the client and it will access the data from the recommendations server.
