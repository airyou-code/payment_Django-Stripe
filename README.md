<h1 align="center">payment Django+Stripe</h1>

<a href="https://github.com/airyou-code/Notification_service" target="_blank">github</a> 
<a href="https://testappairyou.herokuapp.com/api" target="_blank">Test app</a> 

## Description
- The project was created as a test task.
- The task is to implement a payment system for goods using Stripe

# Stack technology
- Django
- RestAPI
- Postgres
- Docker

# Test app
The application is running on Heroku
- `https://testappairyou.herokuapp.com`

# Installation
Need to install docker-compose!!!
- `git clone https://github.com/airyou-code/payment_Django-Stripe.git `
- `docker-compose up --build`

Commands for creating an admin:
- `docker-compose exec webapp python3 ./src/manage.py createsuperuser`

Go to the admin panel:
- `http://127.0.0.1:8000/admin/`

## Usage API
- `GET http://127.0.0.1:8000/api/`

### Item
creating, editing, or viewing a list of items

- `GET http://127.0.0.1:8000/api/item/`
- `GET http://127.0.0.1:8000/api/item/1`
- `GET http://127.0.0.1:8000/api/item/?name=Pen2&price=2000`
- `POST http://127.0.0.1:8000/api/item/` + json
- `PUT http://127.0.0.1:8000/api/item/1` + json
Search is implemented by name
- `GET http://127.0.0.1:8000/api/item/?search=P`


json example:
```json
{
    "name": "Pen",
    "description": "cool",
    "price": 1200
}
```

### Order
creating, editing, or viewing a list of items

- `GET http://127.0.0.1:8000/api/order/`
- `GET http://127.0.0.1:8000/api/order/{id}`
- `POST http://127.0.0.1:8000/api/order/` + json
- `PUT http://127.0.0.1:8000/api/order/{id}` + json


json example:
```json
{
    "items": [
        1,
        2,
        3
    ]
}
```

### Buy and BuyOrder
functions with which you can get a Stripe Session Id
to pay for the selected Item or Order

- `GET http://127.0.0.1:8000/api/buy/{id}`
- `GET http://127.0.0.1:8000/api/buyorder/{id}`

## HTML response
Request with the help of which you can get a simple HTML page with information about the selected Item and a Buy button.
By clicking on the Buy button, a request for api/buy/{id} should occur, session_id should be obtained, and then a redirect to the Checkout form stripe should occur using the Stripe JS library.redirectToCheckout(SessionID=session_id)
- `GET http://127.0.0.1:8000/item/{id}`

Request with the help of which you can get a simple HTML page with information about the selected Order and a Buy button.
By clicking on the Buy button, a request for api/buyorder/{id} should occur, session_id should be obtained, and then a redirect to the Checkout form stripe should occur using the Stripe JS library.redirectToCheckout(SessionID=session_id)

- `GET http://127.0.0.1:8000/order/{id}`






