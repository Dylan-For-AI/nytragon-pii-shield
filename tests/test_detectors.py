from pii_shield.detectors import make_label, mask_emails, mask_phones, mask_ssn


def test_masks_a_simple_email():
    result = mask_emails("Write to jean.bernard@saint-louis-clinic.fr today.")
    assert result == f"Write to {make_label('EMAIL')} today."


def test_text_without_email_is_unchanged():
    text = "No sensitive data here."
    assert mask_emails(text) == text

def test_masks_email_with_hyphen_in_domain():
    result = mask_emails(
        "Please contact Mr. Jean Bernard at jean.bernard@saint-louis-clinic.fr for follow-up."
    )
    assert result == (
        f"Please contact Mr. Jean Bernard at {make_label('EMAIL')} for follow-up."
    )

def test_masks_french_phone_formats():
    phones = [
        "06 12 34 56 78",
        "0612345678",
        "06.12.34.56.78",
        "+33 6 12 34 56 78",
    ]
    for phone in phones:
        result = mask_phones(f"Call {phone} tomorrow.")
        assert result == f"Call {make_label('PHONE')} tomorrow."


def test_text_without_phone_is_unchanged():
    text = "Room 12 opens at 8 am."
    assert mask_phones(text) == text

def test_masks_french_ssn_formats():
    numbers = [
        "1 85 05 78 006 084 36",
        "185057800608436",
        "2 91 12 2A 004 012 45",
    ]
    for number in numbers:
        result = mask_ssn(f"SSN: {number}.")
        assert result == f"SSN: {make_label('SSN')}."


def test_text_without_ssn_is_unchanged():
    text = "Invoice 12345 dated 2026."
    assert mask_ssn(text) == text

def test_phone_inside_longer_number_is_not_masked():
    text = "Order 1206123456789 shipped."
    assert mask_phones(text) == text

def test_phone_followed_by_extra_digit_is_not_masked():
    text = "Ref 06123456789 archived."
    assert mask_phones(text) == text