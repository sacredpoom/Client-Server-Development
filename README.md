# Client-Server-Development
Coursework learning to develop a full stack web application with MongoDB and Dash framework.

![image](https://github.com/sacredpoom/Client-Server-Development/assets/20672168/6250f386-530c-4bd4-b68b-95bb32320d90)

## About the Project:
The aim of this project is to create a NoSQL database with a client-facing web application for use by the client Grazioso Salvare. The MVC design pattern is used for this project to create the web application. The database is created using MongoDB with a Python CRUD script for the Model component. Dashboard coded using Dash framework to implement interactive filters and visualizations such as geolocation and pie charts for the View and Controller components. 
The client logo is displayed at the top of the dashboard, drop down filters below allows users to choose from three custom filtering queries and reset to default option. Geolocation and pie-chart components are interactive with dashboard filters. Tooltip set to display animal name in geolocation chart. 

## Tools Used: 
* Python 3.0.12 [https://www.python.org/downloads/ ]
* MongoDB [https://www.mongodb.com/docs/manual/installation/]
* PyMongo _$ python3 -m pip install pymongo_ [https://pymongo.readthedocs.io/en/stable/installation.html]
* Jupyter Notebook [https://jupyter.org/install]
* Dash [https://dash.plotly.com/installation] 
* Pandas [https://pandas.pydata.org/] 

How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?
Writing modular code that is documented with comments helps improve code-reusability in future projects. The Python CRUD module consists of small, single responsability functions increasing readability and reuse. Writing modular code like this helps with testing and debugging stages by reducing the time it takes to identify the section of code with an issue. 

How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?
The first step to any problem as a computer scientist is to understand the requirements. Once I understand the requirements I can begin to break the problem down into smaller parts. This course began by creating the database backend, next working on the Python CRUD for our middle layer, and finally the client-facing dashboard web application. Breaking down the overall project into smaller parts helps with unit testing to ensure each "layer" works as expected, then integration testing to ensure the system compenents all interact well. This helps ensure a quality deliverable to clients with minimal bugs.

What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?
Computer scientists solve problems by using computers to automate tasks that are normally time-consuming or prone to human-error. This project involved creating a way for the client to interact with data in a quick and user-friendly method helping them focus on finding ideal candidates for their search and rescue training instead of digging through the data.  
