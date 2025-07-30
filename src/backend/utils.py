import phonenumbers

def normalize_phone_number(phone_number: str, default_region: str = "IN") -> str | None:
    """Parses and normalizes a phone number to the E.164 format."""
    try:
        parsed_number = phonenumbers.parse(phone_number, default_region)
        if phonenumbers.is_valid_number(parsed_number):
            return phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
    except phonenumbers.phonenumberutil.NumberParseException:
        # Log the error in a real application
        pass
    return None