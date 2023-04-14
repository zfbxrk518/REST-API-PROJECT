# REST APIs Recording Project

Nothing here yet!

妈蛋终于搞明白了vs code里的代码和github repository的先后顺序，也创建了repository。终于开始要同步了！要有绿色了！

###4.12

 **docker:**

        ```
        docker build -t flask-smorest-api .
        ```
        ```
        docker run -dp 5000:5000 -w /app -v "/c/Documents/yourproject:/app" flask-smorest-api
        ``` 

         After running these two codes, you can close the terminal and the project will update automatically.

 **insomnia：**
 
          **url** -> {{url}} 

** Blueprint**: 

          divide an API into multiple segements.

**MethodView:**

          create a class whose methods route to specific endpoints.

**Swagger page:**

          localhost:5005/swagger-ui

**marshMallow:**

          use to do data validation.