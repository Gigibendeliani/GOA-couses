def capitalize_names(names):
    capitalized_names = [name.capitalize() for name in names]
    return capitalized_names

# ფუნქციის შემოწმება
names = ["john", "jane", "alex", "emily"]
capitalized_names = capitalize_names(names)
print("განახლებული სია:", capitalized_names)