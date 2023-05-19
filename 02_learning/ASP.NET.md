Website = [[HTML]] CSS and JavaScript
API client communicate with server over HTTP, JSON or XML
SPA(react, Angular) perdorm most UI logic of website.

REST:
-   GET: Retrieve data from the web service.
-   POST: Create a new item of data on the web service.
-   PUT: Update an item of data on the web service.
-   PATCH: Update an item of data on the web service by describing a set of instructions about how the item should be modified. The sample application in this module doesn't use this verb.
-   DELETE: Delete an item of data on the web service.

Benefits
-  S**imple serialization**: ASP.NET was designed for modern web experiences. Endpoints automatically serialize your classes to properly formatted JSON out of the box. No special configuration is required. Of course, you can [customize serialization](https://learn.microsoft.com/en-us/aspnet/core/web-api/advanced/custom-formatters) for endpoints that have unique requirements.
-  **Authentication and authorization**: For security, API endpoints have built-in support for industry-standard JSON Web Tokens (JWTs). Policy-based authorization gives you the flexibility to define powerful access-control rules in code.
-  **Routing alongside your code**: ASP.NET lets you define routes and verbs inline with your code by using attributes. Data from the request path, query string, and request body are automatically bound to method parameters.
-  **HTTPS by default**: HTTPS is an important part of modern, professional web APIs. It relies on end-to-end encryption to provide privacy, and to help ensure that your API calls aren't intercepted and altered between client and server.

`dotnet dev-certs https --trust
Serve traditional page = use Razor Pages or MVC
FormBased to WebAppbased // ASP.NET use [[HTML]] + ASP markup
Java Spring PHP Laravel Python Flask, Node.js express
ASP.NET fullStack (from DB, business logic ot [[HTML]]) combine with Vue React  

![[Pasted image 20230118131341.png]]
```cmd
dotnet new webapi -f net6.0
dotnet run
```
localhost:{port}/WeatherForecast

![[Pasted image 20230118131351.png]]

ASP.NET REPL
```cmd
dotnet tool install -g Microsoft.dotnet-httprepl
httprepl https://localhost:{PORT}

ls / cd WeatherForecast / get/ post
```

  ![[Pasted image 20230118131411.png]]

