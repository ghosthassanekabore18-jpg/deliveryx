#Code by NiMATOU

#utils.py — Utility functions (validation, formatting, search)

# Burkina Institute of Technology 



from models import Courier



# VALIDATION FUNCTIONS 


def validate_phone(phone: str) -> bool:
    """
    Validates that a phone number contains exactly 8 digits.

    Args:
        phone (str): The phone number string to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    # Strip whitespace, check all characters are digits and length is exactly 8
    phone = phone.strip()
    return phone.isdigit() and len(phone) == 8


def validate_email(email: str) -> bool:
    """
    Validates that an email address contains the @ symbol and a dot.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    # An email must contain both '@' and '.' characters
    return "@" in email and "." in email


def validate_weight(weight_str: str) -> bool:
    """
    Validates that a weight input can be converted to a positive float.

    Args:
        weight_str (str): The weight string entered by the user.

    Returns:
        bool: True if valid, False otherwise.
    """
    try:
        # Try converting the string to a float
        weight = float(weight_str)
        # Weight must be strictly positive
        return weight > 0
    except ValueError:
        # Conversion failed — not a valid number
        return False
        




# DISPLAY HELPERS

  


def display_separator():
    print("-" * 60)


def display_title(title: str):
    
    print("\n" + "=" * 60)
    print(f" {title.upper()}")
    print("=" * 60)




# SEARCH FUNCTIONS — Nina



def find_available_courier(couriers: list) -> Courier:
    """
    Searches the couriers list and returns the first available courier.

    Args:
        couriers (list): The list of all Courier objects.

    Returns:
        Courier: The first available courier, or None if none are available.
    """
    # for loop to go through each courier and check availability
    for courier in couriers:
        if courier.is_available():
            return courier
    # No available courier found
    return None


def find_delivery_by_id(deliveries: list, delivery_id: str):
    """
    Searches the deliveries list and returns the delivery matching the given ID.

    Args:
        deliveries (list): The list of all Delivery objects.
        delivery_id (str): The unique ID to search for.

    Returns:
        Delivery: The matching Delivery object, or None if not found.
    """
    # for loop to search through all deliveries by ID
    for delivery in deliveries:
        if delivery.get_delivery_id() == delivery_id.upper():
            return delivery
    # No delivery found with that ID
    return None


def find_client_by_id(clients: list, client_id: str):
    """
    Searches the clients list and returns the client matching the given ID.

    Args:
        clients (list): The list of all Client objects.
        client_id (str): The unique ID to search for.

    Returns:
        Client: The matching Client object, or None if not found.
    """
    # for loop to search through all clients by ID
    for client in clients:
        if client.get_client_id() == client_id.upper():
            return client
    # No client found with that ID
    return None

