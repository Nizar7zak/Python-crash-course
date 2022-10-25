#  what if I want so save username, email, phone, password
# this values is related to each other
#  so we can save it in the same place
#  that called dictionaries!

first_name = 'Nizar'
last_name = 'Zakout'
phone_number = 972599111111
email = 'awsrestart.program@gazaskygeeks.com'
password = 123456789


#  using dictionary
customer = {
    "first_name": 'Nizar',
    "last_name": 'Zakout',
    "phone_number": 972599111111,
    "email": 'awsrestart.program@gazaskygeeks.com',
    "password": 123456789,
}

#  how we can arrive to phone number value?

print(customer['phone_number'])


# what about get method?

print(customer.get("last_name"))

#  get can take two argument, the first argument is a key
#  the second argument is default value.
print(customer.get("age", 27))

print(customer)


# conclusion
#  customer.get("age", 27) => here will search in customer dict
#  if find a key call age, will get the value, but if does not,
#  it will set a default value.
