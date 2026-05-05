import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

num = int(input("Enter a number: "))

result = proxy.factorial(num)

print("Factorial is:", result)
