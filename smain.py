# try catch

# try ----> somthing that might cause an exception

# except  --> do this if there was exception

# else --> do this if there was no exception

# finally --> carry out no matter what happens

try:
    file = open("a_file.txt")
    a_dict = {"key": "value"}
    print(a_dict["gyug"])

except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Somthing")

except KeyError as error_message:
    print(f"The key {error_message} doesn't exist")

else:
    content = file.read()
    print(content)

finally:
    # file.close()
    raise KeyError("Error is error")  # Its raises error on our own


