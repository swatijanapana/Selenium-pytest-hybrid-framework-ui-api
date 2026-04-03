# API Create User TestData


def get_api_user_payload(email, password):
    return {"name": "Test User",
            "email": email,
            "password": password,
            "title": "Mr",
            "birth_date": "10",
            "birth_month": "May",
            "birth_year": "1990",
            "firstname": "Test",
            "lastname": "User",
            "company": "ABC",
            "address1": "Street 1",
            "address2": "Street2",
            "country": "US",
            "zipcode": "12345",
            "state": "GA",
            "city": "Denton",
            "mobile_number": "15635722"}


def del_api_user_payload(email, password):
    return {"email": email,
            "password": password}
