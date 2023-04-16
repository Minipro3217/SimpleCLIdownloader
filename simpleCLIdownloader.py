import wget

print("Enter 1 to quit the program")

site_url = input("Enter url here: ")

while site_url != "1":
    file_name = wget.download(site_url)
    print(file_name)
    site_url = input("Enter url here: ")

print("Program terminated by user")
