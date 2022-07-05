from collections import namedtuple

data = [
    ("홍길동", 23, "01099990001"),
    ("김철수", 31, "01099991002"),
    ("이영희", 29, "01099992003"),
]

Employee = namedtuple("Employee", "name, age, cellphone")

# data = [Employee(emp[0], emp[1], emp[2]) for emp in data]

data = [Employee._make(emp) for emp in data]

emp = data[0]
print(emp)
print(emp.name)
print(emp.age)
print(emp.cellphone)
print(emp._asdict)

print(emp[0])
print(emp[1])
print(emp[2])

# emp.name = "박길동"

new_emp = emp._replace(name="박길동")
print(new_emp)
