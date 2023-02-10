# CSCI_Assignment_Two

## Instructions

Create a polls Django project. How you design the UI is your choice, however the website should have the following functionalities:

- [x] Page to display list of all the questions.
- [x] A click of a 'vote' button which lists all of choices for a given question.
- [x] The user must be able to select one of the choices and submit the vote.
- [x] Another page to view the results of the voting for each question.
- [x] Final page to create and modify a question (Django admin interface can be used to do this task.)
- [x] Share the final working code base, with instructions to run the project and required instruction must be specified in the `README.md` file.

## Question 1.
- [x] Create two models in `models.py` called Question and Choice.  
These 2 models can have any fields that are required for the project. For example: Question model has 

```python
question_text = models.CharField(max_length=200)
```

- [x] What is the `models.CharField`? and why is it used? (Short 2 sentence answer.)
    - [x] `models.CharField` is a string field for small to large sized strings. In this case the max length is 200 characters and is used to store the question that will be asked.


## Question 2.
- [x] Run a Django shell using the following command and run atleast 3 queries using Django model objects. Example: `Question.objects.all()`

```
python manage.py shell
```
Share the screenshot of your shell.
- [x] Screenshot one.  
![This is an image](https://github.com/mikekenn/CSCI_Assignment_Two/blob/main/mysite/assets/images/img1.png?raw=true)
- [x] Screenshot two.  
![This is an image](https://github.com/mikekenn/CSCI_Assignment_Two/blob/main/mysite/assets/images/img2.png?raw=true)
- [x] Screenshot three.  
![This is an image](https://github.com/mikekenn/CSCI_Assignment_Two/blob/main/mysite/assets/images/img3.png?raw=true)
## Question 3.
- [x] Change `views.py` of your polls app and add a view which should use a template to render.  
- [x] When you run the server, you should be able to click on `http://127.0.0.1:8000/` to open in browser and it should list all the questions.
- [x] With a button to 'Vote'. On click of vote, it should open the choices for that question and the user must be able to vote on a hoice and submit.

### Example:
`/polls/` page with list of Questions:  
![This is an image](https://github.com/mikekenn/CSCI_Assignment_Two/blob/main/mysite/assets/images/img4.png?raw=true)

`/vote/1/`  
![This is an image](https://github.com/mikekenn/CSCI_Assignment_Two/blob/main/mysite/assets/images/img5.png?raw=true)

## Question 4.
- [ ] Design a page to display the poll results for a given question.
`/results/1/`  
![This is an image](https://github.com/mikekenn/CSCI_Assignment_Two/blob/main/mysite/assets/images/img6.png?raw=true)

## Question 5.
- [x] Add and edit a question with appropriate choices. You are allowed to use Django admin for this question.  
![This is an image](https://github.com/mikekenn/CSCI_Assignment_Two/blob/main/mysite/assets/images/img7.png?raw=true)

## Question 6.
- [x] Django is easy to setup and use. Do you agree? (Yes/No)? write a brief reason for your choice.
    - [x] Yes, i think Django is easy to use. The documentation on their site is clean and concise. There is a great public community that supports it and the examples on their site do a good job of explaining its functionalities.

Add Django python setup steps.

1. Check python version/if python is installed `python`.
2. Check to see if Django is installed/the version `python -m django --version`
3. If not installed, go ahead and install `pip3 install django==4.0.4`
4. Create Django project `django-admin startproject mysite`
5. spin up server `python3.11 manage.py runserver`
6. Create polls app `paython3.11 manage.py startapp polls`

## Steps to Run.

1. Check Django is installed.
    - Linux/macOS: `python -m django --version`
    - Windows: `py -m django --version`
2. Clone GitHub repo.
    - Linux/macOS/Windows: `git clone [repoURL]`
3. Move into root site folder.
    - Linux/macOS/Windows: `cd mysite`
4. Spin up server.
    - Linus/macOS: `python manage.py runserver`
    - Windows: `py manage.py runserver`
5. Open up browser to following URL.
    - To see the questions: `http://127.0.0.1:8000/polls/`
    - To see the Admin panel: `http://127.0.0.1:8000/admin/`


## TODOs

1. Could be Dockerized to remove OS dependability.