import users_pb2

users = [
    {
        "id": 33,
        "name": "Dino",
        "surname": "Dvornik",
        "phone": "+385994923462",
        "created": "2018-01-09T03:50:19",
        "active": True,
        "lat": 43.5081,
        "lng": 16.4402,
        "country": {
            "name": "Croatia",
            "currency": "HRK",
            "code": "HR",
        },
        "payments": [
            {"created": "2018-04-01T03:50:19", "amount": 99856},
            {"created": "2018-04-02T06:24:32", "amount": 85567},
        ]
    },
    {
        "id": 34,
        "name": "Boris",
        "surname": "Dvornik",
        "phone": "+3859854345345",
        "created": "2018-01-10T03:50:19",
        "active": True,
        "lat": 43.5081,
        "lng": 16.4402,
        "country": {
            "name": "Croatia",
            "currency": "HRK",
            "code": "HR",
        },
        "payments": [
            {"created": "2018-04-01T03:50:19", "amount": 989864},
            {"created": "2018-04-02T06:24:32", "amount": 55336},
        ]
    },

]

users_grpc = []
for user in users:
    payments = []
    for payment in user['payments']:
        payments.append(users_pb2.Payment(
            created=payment['created'],
            amount=payment['amount'],
        ))

    users_grpc.append(users_pb2.User(
        id=user['id'],
        name=user['name'],
        surname=user['surname'],
        phone=user['phone'],
        created=user['created'],
        active=user['active'],
        lat=user['lat'],
        lng=user['lng'],
        country=users_pb2.Country(
            name=user['country']['name'],
            currency=user['country']['currency'],
            code=user['country']['code'],
        ),
        payments=payments,
    ))

users_reply = users_pb2.UsersReply(total=len(users_grpc), users=users_grpc)