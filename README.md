# graphql_tutorial
This project is made as an example of the graph tutorial created at (All Stars Coders)[https://allstarscoders.com].

### Requirements
To run this project you will need to have the following requirements:
- Python 3.8.6 or superior
- pip
- MySQL(With little modifications in the configuration layer you can use another RDBMS)

### Pre-run configurations
In this project we are using environment variables to avoid the exposure of some
configuration parameters, so you will need to import these values in your OS:
- FLASK_APP=main.py (Please use the same main.py value if don't want to have problems locating your entrypoint file)
- GRAPHQL_TUTORIAL_DB_SERVER (Location of the database e.g localhost)
- GRAPHQL_TUTORIAL_DB_NAME (Name of the database - schema in MySQL)
- GRAPHQL_TUTORIAL_DB_PASSWORD (Password used to connect to the database)
- GRAPHQL_TUTORIAL_DB_USER (Database user)

### Running the project
To run the project use the following command in the root folder of the project:
```
flask run 
```

### Testing the project
To test the project go to [http://localhost:5000/graphql], this URL will provide you an
user interface named PLAYGROUND where you can test different queries.
