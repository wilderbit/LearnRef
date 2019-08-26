# Spring Big Picture

#1.What is Spring

"Spring" could mean ...
- The Spring Framework
- Spring Boot
- Spring Data
- Spring Cloud
- Spring Batch
- And more!

Spring Family
-------------
Web, Data, AOP, Core

Spring Projects
---------------
Spring Data, Spring Batch, Spring LDAP, Spring Session, Spring Kafka, Spring Social,
Spring Web Services, Spring Integration, More...

Spring Boot
-----------
Built on Spring, Choice Making and Configuration

Spring Cloud
------------
Spring Cloud is built upon Spring boot, Micro-service Arch.

Why Spring
----------
Alternate to JEE
Spring make it easy to create Java Enterprise Applications.
Flexible, Modular and backwards compatible
Large and active community


#2. Getting to know Spring with Spring Boot
 Spring Boot is used to create web and non-web application both

# Notable Features
1. Auto config
2. Standalone (No need to deploy an application on web server). There is simple just run
    - Package the application (java -jar my-app.jar)
    - Run the application
3. Opinionated


Start Project from [Spring Initializer](https://start.spring.io)
- For more learning 
    1. Create your first Spring Boot application by Dan Bunker
    2. Spring Boot: Efficient Development, Configuration and Deployment by Dustin Schultz

#3. Understanding Spring's Foundation: The Spring Framework

Six key areas of Spring Framework
---------------------------------
1. Core
2. Web
3. AOP
4. Data Access
5. Integration
6. Testing

 
Spring Core
-----------
Provides a number of different features
- i18n Internationalization support
- Validation Support
- Data binding support
- Type conversion support
- and more...

At the center of Spring Core is Dependency Injection
Dependency Injection is all about dealing with the way objects fulfill their dependent objects.
Two choices to fulfill
- Fulfill our own (Tightly Coupled).
- Declare Dependencies(More Flexible, Loosely Coupled) -->> Dependency Injections

Spring Core is dependency Injection container
- Create and maintains objects and their dependencies
- Less for developer to manage

Spring Web
----------
Framework for handling web requests
1. Can be handled via Spring Web MVC
2. Can be handled via Spring web Flux

Spring Web MVC
--------------
  
 