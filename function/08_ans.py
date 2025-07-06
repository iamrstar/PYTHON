def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Function calls
print_kwargs(name="shaktiman", power="lazer")
print_kwargs(name="shaktiman")
print_kwargs(name="shaktiman", power="lazer", enemy="Dr. Jackal")
