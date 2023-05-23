# Job description
You have been hired to consult Auby & Brinch Finance in their plans to improve and expand their development team. The job description from the business is fairly general, so it's up to your team to present what you think is important and relevant.

Auby & Brinch Finance is a company consisting of ~70 general employees and 3 software developers. The plan is to expand the current software development team to ~5 people within 3 months and another team of ~5 within 12 months. The software team as it stands now consists of general developers with little DevOps experience. One developer has the role of leader, the other two are general developers.

The software being developed is used in house by the rest of the employees. The software is a web site to manage employees, customers and jobs. The software is crucial to the operation of the business and will play an important role as the company grows.

**Link to the software source code (use this for setup and modifications): https://github.com/XD-DENG/flask-exampleLinks to an external site.**

(obviously this is not the software described in the imagined setting above, but let's pretend...)

## Current working practices for the development team is as follows:

1. The team meets on Mondays to discuss the plan for the week
2. Each team member writes down the tasks they will do this week
3. Each developer works on their own machine and submits changes in a zip file to the team leader
4. The team leader assembles the changes from the team and transfers the new release to the internal server
The team is not using any tools other than the development IDE and email. Bugs and issues are handled as they are reported.

Your task is to analyze the team's working practices and compare them to current best practices in the field. The company will use your analysis and recommendations as a base for improving their working practices and for staffing up the teams. The team wishes for a working DevOps setup with their application as a reference. They would like to move from SQLite to a database more suited for production and would like your assistance in doing so.

# flask-example

A minimal web app developed with [Flask](http://flask.pocoo.org/) framework. 

The main purpose is to introduce how to implement the essential elements in web application with Flask, including

- URL Building

- Authentication with Sessions

- Template & Template Inheritance

- Error Handling

- Integrating with *Bootstrap*

- Interaction with Database (SQLite)

- Invoking static resources

For more basic knowledge of Flask, you can refer to [a tutorial on Tutorialspoint](https://www.tutorialspoint.com/flask/).


## How to Run

- Step 1: Make sure you have Python

- Step 2: Install the requirements: `pip install -r requirements.txt`

- Step 3: Go to this app's directory and run `python app.py`



## Details about This Toy App

There are three tabs in this toy app

- **Public**: this is a page which can be accessed by anyone, no matter if the user has logged in or not.

- **Private**: Only logged-in user can access this page. Otherwise the user will get a 401 error page.

- **Admin Page**: This part is only open to the user who logged in as "Admin". In this tab, the administrator can manage accounts (list, delete, or add).


A few accounts were set for testing, like ***admin*** (password: admin), ***test*** (password: 123456), etc. You can also delete or add accounts after you log in as ***admin***.



## References

- http://flask.pocoo.org/

- https://www.tutorialspoint.com/flask/



## Credict
Image private.jpg: https://commons.wikimedia.org/wiki/File:(315-365)_Locked_(6149414678).jpg

Image public.jpg: https://commons.wikimedia.org/wiki/File:Drown%3F!_(131380682).jpg
