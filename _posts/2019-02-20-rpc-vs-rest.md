---
title: "RPC vs REST"
categories:
  - Backend
tags:
  - microservices
  - protocol
---

In my previous post, I have answered the question [if we should use gRPC]({% link _posts/2019-02-14-grpc-should-we-use-it.md %}). But why don't we use REST as another popular protocol in developing web services?

The answer is depending on your needs, and what suitable to your system. Maybe we can take closer look on the differences between RPC and REST.

## Background
### RPC
RPC is short for "remote procedure call". The idea is simple - execute some method by name on another computer. It functions like a normal method call, accepting a set of parameters that are [serialized](https://en.wikipedia.org/wiki/Serialization) over the network and a response that is serialized over the network. There are lots of frameworks for RPC. Some of the more popular (at least for the JVM) are Thrift, Spring RPC, and Finagle.

### REST
REST, short for "representational state transfer" originated from Roy Fielding's PhD dissertation. RESTful systems view HTTP endpoints, that can be distributed across difference services, as resources that have an associated set of standardized verbs (GET, PUT, POST, DELETE) that can be invoked to interact with the resource. RESTful APIs can be self-documenting and easily discoverable.

## Implementation
### RPC
RPC implements client and server stubs that essentially make it possible to make calls to procedures over a network address as if the procedure was local. Simply put, RPC exposes methods (say, ***getUsers()***) in the server to the client.

For the RPC endpoint assume the client only cares about the name of the user based on id. We expect a JSON from the service call that has a name property.

For example:
```js
var app = http.createServer(function onRequest(req, res) {
  if (req.url === '/getUserNameById?id=' + USER_ID) {

    var user = MODERATOR_USERS.find(function onModeratorUser(u) {
      return u.id === USER_ID;
    });

    res.setHeader('Content-Type', 'application/json; charset=utf-8');

    res.end('{' + '"name":"' + user.name + '"}');
  }
});
```

Note the URL matches an endpoint `/getUserNameById` with a query string `id` parameter. RPC style endpoints are notorious for specifying the function in the URL. This is convenient because by looking up the URL you can decipher what it does and what you get in return. The service does not concern itself with all the properties available so it is simple.

Testing the RPC style endpoint yields these results:
```
> curl http://localhost:1989/getUserNameById?id=1
{"name":"Tien Le"}
```

### REST
REST as an architectural style implements HTTP protocol between a client and a server through a set of constraints, typically a method (***GET***) and a resource or endpoint (***/users/1***).

For the REST endpoint, we must treat it as a resource. Imagine we have a domain of all users found in the system. Within this moderator domain of users, you will find a user.

For example:
```js
var app = http.createServer(function onRequest(req, res) {
  if (req.method === 'GET' &&
    req.url === '/moderator/user/' + USER_ID) {

    var user = MODERATOR_USERS.find(function onModeratorUser(u) {
      return u.id === USER_ID;
    });

    res.setHeader('Content-Type', 'application/json; charset=utf-8');

    res.end('{"id":' + user.id + ',"name":"' + user.name +
      '","activeStatus":"' + user.activeStatus + '"}');
  }
});
```

Note the URL matches an endpoint `/moderator/user` with an id of `1` appended at the end. For this REST endpoint, the HTTP verb or method matters. A GET request tells the service we want everything under the user domain with all property fields. If you inspect the JSON returned this is why you get back the entire domain. This is nice because you are building a domain boundary that defines all the data it has. With this, any client that wants user data can use it because the service allows many ways of using the data.

Testing the REST style endpoint yields these results:
```
> curl http://localhost:1989/moderator/user/1
{"id":1,"name":"Tien Le","activeStatus":"Active"}
```

Other cool thing about REST is that it provides a code called **“status code”** within the response to let you know wether the operation succeded or not. The set of error codes it might return is standardized and you can check it in the following cheat sheet:

| Status code | Meaning                    |
|-------------|----------------------------|
| 2XX         | Success                    |
| 3XX         | A resource has been moved  |
| 4XX         | Error from the client-side |
| 5XX         | Error from the server-side |

## Summarizing

|                      | RPC                                                                                                                                                                                                                               | REST                                                                                                                                                                                                                                                                                                  |
|----------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Definition           | Exposes action-based API methods                                                                                                                                                                                                  | Exposes data as resources;<br>To represent CRUD operations                                                                                                                                                                                                                                            |
| Use case             | For APIs exposing several actions                                                                                                                                                                                                 | For APIs doing CRUD-like operations                                                                                                                                                                                                                                                                   |
| HTTP verbs           | GET – read-only response<br>POST – others                                                                                                                                                                                         | POST – Create<br>GET – Read<br>PUT – Update<br>PATCH – Updated<br>DELETE – Delete                                                                                                                                                                                                                     |
| Pros                 | * Easy to understand<br>* Lightweight payloads<br>* High performance<br>* Not exclusive to HTTP protocol<br>* It is easier to design an API endpoint that only requires you to create a function                                  | * Standard method name, arguments, format and status codes<br>* Uses HTTP features<br>* Highly debuggable, human-readable format makes it easier to prototype<br>* Easy to maintain<br>* Can easily expose internal APIs as external APIs<br>* Wide language support - easy to integrate acquisitions |
| Cons                 | * Discovery is difficult<br>* Limited standardization<br>* Application developers can, and will, do whatever they want<br>* Can lead to function explosion<br>* Client or server libraries may not be available for all languages | * Big payloads<br>* Multiple HTTP round trips. Being atomic i.e. one API can only perform one operation can lead to multiple API hits before properly rendering a particular feature<br>* No defined specification or framework leads to a lot of interpretations                                     |
| Usage interpretation | Triggers an action to perform the request                                                                                                                                                                                         | It’s more like a post-action<br>* First your create a resource in an existing collection<br>* Then the action is performed in background through a trigger                                                                                                                                            |


There are many other comparisons about RPC and REST, you can also check them for more details and opinions:
- [REST vs. gRPC: Battle of the APIs](https://code.tutsplus.com/tutorials/rest-vs-grpc-battle-of-the-apis--cms-30711)
- [Debunking the Myths of RPC & REST](https://etherealbits.com/2012/12/debunking-the-myths-of-rpc-rest/)
- [REST vs. RPC: what problems are you trying to solve with your APIs?](https://cloud.google.com/blog/products/application-development/rest-vs-rpc-what-problems-are-you-trying-to-solve-with-your-apis)
- [API Paradigms – which and when to use them: REST vs RPC](https://filipaivars.pt/2019/03/18/api-paradigms-and-when-to-use-them/)
