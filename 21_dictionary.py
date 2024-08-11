emp = {
    "id": 1,
    "name": "John Doe",
    "designation": "Software Engineer",
    "salary": 60000
}

print("Original dictionary:", emp)

if "designation" in emp:
    del emp["designation"]

emp["name"] = "Jane Smith"

print("Updated dictionary:", emp)
