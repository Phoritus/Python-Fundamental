def create_reservation(data):
    try:
        rev = Reservation(**data)
        print(f'Reservation: {rev.customer_name}, Date: {rev.reservation_date}, Number of Guest:{rev.number_of_guests}')
        if rev.special_requests:
            print('Special Request:',rev.special_requests)
    except ValidationError as e:
        print(f'As error {e}')
        print('Failed to create reservation')
    return rev