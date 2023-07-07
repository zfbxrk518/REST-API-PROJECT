MERN: mongoDB, express, react, node
 
frontend -> react : build user interfaces
backend ->  mongoDB: a noSql database
        ->  express: a node.js framework
        ->  node: a server-side runtime: javascript on the server-side 

front-end web development = displaying things on a web page = rendering

DOM(Document Object Model): feature that allows JavaScript to change the web page
DOM is repetitive and hard to manage so we use javascript framework.
javascript framework -> plain javascript 
javascript doesn't have an official framework. The latest generation is: React, Vue, Angular

Javascript can't split the code to different files so it needs a bundler, the most famous one is called webpack. Webpack will split the js code into different files then combine all these files into one file and put it on the website. Typescript is js's transpiler. It adds extra features to js and transfers into normal js.

Bootstrap is css framework.
Js frontend uses XMLHttpRequest to send messages to url of backend. Nowadays we also use axios-http, fetchAPI to send messages.

Backend saves and manages data.

Programming language can turn a computer into a server and allow it to receive messages from the client. Popular programming language are js(also calls node.js), python, ruby and java. Any programming language needs a backend framework and package manager to help it to work together.

language        framework      package manager(install and manage packages)
javascript      express         npm
python          django          pip 
ruby            ruby on rails   bundler
java            java spring     maven

Backend has backend server and database server. The most famous databases are mysql, postgres and mongodb.

request: POST https://amazon.com/orders
         Type         domain name/url path


API(application programming interface): 
the list of all the different types of requests that the backend allows, such as :

app.post('/orders', (request, response) =>{
    const order = createOrder(request);
    database.save(order);
    response.send('Order confirmed.');
})
app.get('/orders', (request, response) =>{
    const order = database.getOrderHistory();
    response.json(orders);
})

'POST /orders' is a naming covention for our requests, a.k.a REST(Representational State Transfer)
post = create
API + REST = REST API
REST is the most common convention that we use for our APIs, there are other types like GraphQL and RPC.

Infrastructures: companies rent computers from cloud computing companies, including:
companies                         PaaS
aws : amazon web services      Elastic Beanstalk
gcp: google cloud platform     App Engine
microsoft azure                App Service

You rent a bunch of computers, a.k.a IaaS = Infrastructure as a Service.
Small computer in the software calls virtual machine or VMs.
Load Balancer
PaaS = Platform as a Service

Microservices: split the backend into several seperate backend, like orders backend, payments backend and email backend.
twilio: email service. It's a Saas. When a company provides a backend and an API that outside applications can use is called Saas = Software as a Service.

Cloud Computing: Iaas, PaaS, SaaS

Additional Techonologies: 
Primary database: MySql, Postgres, Mongodb
Image upload: Primary database + Blob Storage(AWS S3) + CDN(AWS Cloudfront)
Text Search: Primary database + Search Database(Elasticsearch)
Improve performance: Primary database + Cache(redis)
Data Science: Primary database + Analatical database(Snowflake)
Scheduled Tasks: Primary database + Queue(RabbitMQ)