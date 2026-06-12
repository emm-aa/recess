locations = ["Kampala", "Gulu", "Jinja", "Mbarara"]

search = input("Enter location to search for: ")

if search.title() in locations:
    print("Location found: " + search.title())
else:
    print("Location not found.")
