class ShippingContainer:

    # This is an example to class attribute
    next_serial = 1337

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = next_serial
        ShippingContainer.next_serial += 1