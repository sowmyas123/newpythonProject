#api_response is also mutable in nature
#dictonary can be directly used with json
api_response = {
    "first_name": "sowmya",
    "last_name": "arjun",
    "age": 30,
    "email": "sowmyasiddu@gmail.com",
    "password": "test@123",
    "commission" : 30
}
print(api_response)
print(type(api_response))
print(api_response.get("password"))

for key, value in api_response.items():
    print(key, " ", value)