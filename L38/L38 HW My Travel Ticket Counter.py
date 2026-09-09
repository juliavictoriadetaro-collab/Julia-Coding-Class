# =======================
#  MY TRAVEL TICKET COUNTER
# =======================


# PART 1 - TYPES OF DATA
destination   = "Dubai"       # str   - text
price         = 150.00        # float - decimal
quantity      = 2             # int   - whole number
is_available  = True          # bool  - True or False

print("Destination:", destination)
print("Price: $", price)
print("Tickets:", quantity)
print("Available?", is_available)
print()

print(type(destination))
print(type(price))
print(type(quantity))
print(type(is_available))
print()


# PART 2 - ARITHMETIC OPERATORS
total = price * quantity
print("Total ticket cost: $", total)
print("Sale price: $", price - 25.00)
print("Double tickets:", quantity * 2)
print()


# PART 3 - COMPARISON OPERTAORS
print("Is price under $200?", price < 200)
print("More than 1 ticket?", quantity > 1)
print(" Is price exactly $150.00?", price == 150.00)
print()


# PART 4 - STRING OPERATIONS
travel_name = "Dubai" + " " + "Ticket"
print("Travel name:", travel_name)
print("Letters in destination:", len(destination))
print("First letter:", destination[0])
print()


# PART 5 - SWAPPING VALUES
price_a = 150.00
price_b = 300.00
print("Before:", price_a, "and", price_b)

temp    = price_a
price_a = price_b
price_b = temp

print("After:", price_a, "and", price_b)