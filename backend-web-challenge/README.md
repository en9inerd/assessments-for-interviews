# #1: Only normal?

> Normalization is a key design technique in database design to minimize the amount of data you have to store in order to get the complete picture of your data model.

> Take this simple model for storing an address: ![alt](db_schema.png)

## Create a data model that allows you maximize normalization

![alt](diagram.png)

My solution disregards that you can have the same City name in different States.

```Python
from django.db import models

class States(models.Model):
    name = models.TextField()

class Cities(models.Model):
    name = models.TextField()
    state_id = models.ForeignKey('States')

class Zipcodes(models.Model):
    name = models.CharField(max_length=10)

class Addresses(models.Model):
    street1 = models.TextField()
    street2 = models.TextField()
    city_id = models.ForeignKey('Cities')
    zipcode_id = models.ForeignKey('Zipcodes')

class Company(models.Model):
    company_name = models.TextField()
    address_id = models.ForeignKey('Addresses')
```


## Describe how would you recommend setting up an API for the frontend development team to access your normalized model
Access to database fields for the front-end developer should be very simple. He should not have to deal with SQL queries to fetch data and other things that are related to backend. Therefore, I would have implemented methods for data model that are letting create, retrieve, update and delete objects in database. This meaning that methods that generate SQL queries are for database. Then I would have implemented a template engine that is needed to replace from special constructions (template language) in templates to data (obtained at the output of model methods).  
For example, as it is implemented in Django, where a template is rendered with a context. Rendering replaces variables with their values, which are looked up in the context, and executes tags.  

## Describe what are the advantages and disadvantages your normalized model
- advantages normalized model:
  - Storing data in more optimal way
  - Tables are smaller 
  - The updates are very fast (data is located at a single place)
- disadvantages normalized model: 
  - Reading the data from many tables will take a performance hit, because increased the numbers of JOINs

# #2: A race against the clock

> Some tasks take a lot more time than we want to allow in the HTTP request / response cycle. We love to put things up in our queue using Celery. Unfortunately, this can present an opportunity for race conditions to occur, which are amongst the nastiest issues to debug. This Django model below has a race condition.

> The code you are evaluating is [here](https://gist.github.com/jkatz/01accb709cdf1dfdf9e2149cdc9eb8fc)

## Identify where the race condition is in the code
In file `models.py`, Lines 36-37 and 46-47

## Explain why it is a race condition
This is a race condition because the save is wrapped in transaction and if transaction isn't committed yet then updated changes are not available for other connections like calling celery task. Race conditions occur at the time of the calling celery task whether the task will start before or after the transaction is completed. If the task will start before the transaction is committed then it reads the old state of the object and an error appears.

## Explain or provide a solution to how you would solve it
**For Django >= 1.9**, you can use the on_commit hook  
replace line 37 to:
```python
transaction.on_commit(lambda: send_change_of_name.delay(self.id))
```
and replace line 47 to:
```python
transaction.on_commit(lambda: send_change_of_zipcode.delay(self.id))
```

**For Django < 1.9**, use [django-transaction-hooks](https://django-transaction-hooks.readthedocs.io/en/latest/). The solution is very similar  
replace line 3 to:
```python
from django.db import models, transaction, connection
```
replace line 37 to:
```python
connection.on_commit(lambda: send_change_of_name.delay(self.id))
```
and replace line 47 to:
```python
connection.on_commit(lambda: send_change_of_zipcode.delay(self.id))
```

# #3: APIs to the rescue?

> Here is some example return data from both APIs:
> **API #1**  
https://api1.example.com/v1/payments/
```json
[
    {
        "id": "42d213d2-cdc2-4655-99ec-9335b91c9a8f",
        "amount": "20.99",
        "last_4": "1111",
        "memo": "For the bill"
    }
]
```

> **API #2**  
https://api2.example.com/v6/order/history/
```json
[
    {
        "orderID": "32342302010102",
        "total": "9.99",
        "last_4": "1111",
        "description": "Services rendered"
    }
]
```
> Create a mini-application that provides an API that pulls the data from the above two APIs and returns a unified serialized JSON array of objects with the following keys:
> - `remote_payment_id`​ - a reference to the payment ID
> - `total​` - the amount the payment was for
> - `last_4​` - the last 4 digits of the credit card number used on the payment
> - `details`​ - a description of what the payment was

> Hints:
> - More APIs could be added in the future: can you design a modular solution?
> - You do not need to worry about sort order

[[Solution_1](rescue1.py)]    [[Solution_2](rescue2.py)]

# Bonus: Lists of Lists of Lists of Lists of...

Lists - they are everywhere! People love putting things in lists, and nesting the lists. In fact, it seems like some people want to nest things in lists ad infinitum! We need to generate HTML that allows us to do this. Given a JSON data structure like [this](https://gist.github.com/jkatz/2432c6d0c88af56e7162).

Architect and/or develop a solution that will generate the following HTML structure (you do not need to match the spacing): [link](https://gist.github.com/jkatz/14dee50d68d2b05aa953)

You can implement this in either Python or Javascript.

[[Solution](bonus.py)]