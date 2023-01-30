# CSCI_Assignment_Two

## Instructions

Create a polls Django project. How you design the UI is your choice, however the website should have the following functionalities:

- [ ] Page to display list of all the questions.
- [ ] A click of a 'vote' button which lists all of choices for a given question.
- [ ] The user must be able to select one of the choices and submit the vote.
- [ ] Another page to view the results of the voting for each question.
- [ ] Final page to create and modify a question (Django admin interface can be used to do this task.)
- [ ] Share the final working code base, with instructions to run the project and required instruction must be specified in the `README.md` file.

## Question 1.
- [x] Create two models in `models.py` called Question and Choice.  
These 2 models can have any fields that are required for the project. For example: Question model has 

```python
question_text = models.CharField(max_length=200)
```

- [x] What is the `models.CharField`? and why is it used? (Short 2 sentence answer.)
    - [x] `models.CharField` is a string field for small to large sized strings. In this case the max length is 200 characters and is used to store the question that will be asked.


## Question 2.
- [ ] Run a Django shell using the following command and run atleast 3 queries using Django model objects. Example: `Question.objects.all()`

```
python manage.py shell
```
Share the screenshot of your shell.
- [ ] Screenshot one.
- [ ] Screenshot two.
- [ ] Screenshot three.

## Question 3.
- [ ] Change `views.py` of your polls app and add a view which should use a template to render.  
- [ ] When you run the server, you should be able to click on `http://127.0.0.1:8000/` to open in browser and it should list all the questions.
- [ ] With a button to 'Vote'. On click of vote, it should open the choices for that question and the user must be able to vote on a hoice and submit.

### Example:
`/polls/` page with list of Questions:
<!-- ![This is an image](/assets/images/img.png) -->

`/vote/1/`
<!-- ![This is an image](/assets/images/img.png) -->

## Question 4.
- [ ] Design a page to display the poll results for a given question.
### Example:
`/results/1/`
<!-- ![This is an image](/assets/images/img.png) -->

## Question 5.
- [ ] Add and edit a question with appropriate choices. You are allowed to use Django admin for this question.
### Example:

## Question 6.
- [ ] Django is easy to setup and use. Do you agree? (Yes/No)? write a brief reason for your choice.

Add Django python setup steps.

1. Check python version/if python is installed `python`.
2. Check to see if Django is installed/the version `python -m django --version`
3. If not installed, go ahead and install `pip3 install django==4.0.4`
4. Create Django project `django-admin startproject mysite`
5. spin up server `python3.11 manage.py runserver`
6. Create polls app `paython3.11 manage.py startapp polls`