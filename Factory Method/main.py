from controllers import MySqlFactory

useCase = MySqlFactory.create()

response = useCase.do_something(True)

print(response)