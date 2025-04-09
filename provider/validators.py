def validate_priority(priority):
    # Validate priority value
    try:
        new_priority = int(priority)
    except (KeyError, ValueError):
        # Raise an error if priority is missing or not an integer
        raise ValueError("Invalid or missing 'priority' (must be integer).")

    # Check the new priority is greater or equal to 0
    if new_priority < 0:
        raise ValueError("Priority must be greater or equal than 0.")

    return new_priority