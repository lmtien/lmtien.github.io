---
title: "What is gRPC? Should we use it?"
categories:
  - Backend
tags:
  - microservices
  - protocol
---

Sometime ago back, when I was searching for a good protocol to help backend services communicate with one another easily. I read again RPC and also gRPC concept, and I should note them down for future references.

Like many RPC systems, gRPC is based around the idea of defining a service,
specifying the methods that can be called remotely with their parameters and
return types. By default, gRPC uses [protocol
buffers](https://developers.google.com/protocol-buffers) as the Interface
Definition Language (IDL) for describing both the service interface and the
structure of the payload messages. It is possible to use other alternatives if
desired.

```proto
service HelloService {
  rpc SayHello (HelloRequest) returns (HelloResponse);
}

message HelloRequest {
  string greeting = 1;
}

message HelloResponse {
  string reply = 1;
}
```

## So why do we need it?

RPC can be considered as a normal protocol request-response, however it can be used for the communication between services (server-server), moreover client-server. This is really important for those who is designing distributed system, or application is being processed in multiple server rather than one. The example that most everyone knows is Microservices.

That means: 1 request from a client can be processed in different servers or services in order to compute and gather the information, then return the response back to the client. The communication among the servers will be the problem where previously everything can be processed easily in only 1 server. It shows that, if 1 server wants to "talk" to other servers, it needs to encode data (JSON, XML, etc.) and send it over. After that, the receiver will need to decode the data in order to understand what the request is, then it will encode a response, and send back to the sender. This process will be repeated multiple times and consumer lots of resources where we should be simply do the sending part and receiving part.

## Optimize and standardize the communication are the reason for gRPC to be born

To solve the problem that I mentioned above, gRPC uses binary to send and receive, instead of encoding and decoding them to middle-man languages such as JSON or XML. This clearly shows that the performance and speed for communication increase significantly, reduce overhead for CPUs. Google was also making protobuf which is the default language for gRPC to serialize format. This help gRPC to be used or compatible with many popular programming languages: C++, C#, Java, Kotlin, Go, Python, etc.

![image-center](/assets/images/post/2019-02-14-grpc-img-1.png){: .align-center}

gRPC get supported by HTTP/2 which is the improved version of protocol HTTP/1.1. HTTP/2 is also considered as replacement for SPDY (the protocol was developed by Google, open source from 2012, and was stopped support since 2015).

Those are some thoughts from me, if you want to design distributed systems or dig deeper into this topic, you can check out [official website of gRPC](https://grpc.io/) to know more about the key concepts of RPC in general or gPRC specific. In my opinion, gRPC is one of the good choices when I want to implement microservices system.
