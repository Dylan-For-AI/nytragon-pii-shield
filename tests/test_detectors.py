from pii_shield.detectors import make_label, mask_emails, mask_phones


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