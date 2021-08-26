# Welcome to CodeifBlog!

Welcome to CodeifBlog - An **E-Magazine** and **Blog** crafted using _Django_.

The Features that are currently incorporated or in the works include : 
- The basic Login and Sign up structure based on user category - _Writer_ or _Reader_ .
- The Writer Dashboard to facilitate author functionalities.
>The writer has an ability to create, read, update or delete a post
>Have an overview of their previous post and view all post and their corresponding views ordered by time of publishing
- A followers model aimed to connect readers and writers is in the works.
- Reader's Dashboard - Currently being worked on.


## Instructions to run on Local System : 

Run the following commands at the terminal

- git clone [this repository](https://github.com/sinchana-kumbale/codeif-blog) into the desired folder 
- Navigate to the folder codeif-blog
- Activate the virtual environment in codeif-blog using the following command 
> python -m pipenv shell
- Download the required dependencies using the command below
> python -m pipenv install -r requirements.txt 
- Navigate into codeif which is the directory containing the manage.py file
- Run the following command 
>python manage.py runserver

Open a web browser and type http://127.0.1:8000/ or http://localhost:8000/


