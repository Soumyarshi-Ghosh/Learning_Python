import time
print(" This is an application to test your reflexes ")
start = time.time()
print(" Press return...")
input()
end = time.time()
difference = end - start
rounded = round(difference, 2)
print(f" you took {rounded} to press return. ")
