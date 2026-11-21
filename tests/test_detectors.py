from pii_shield.detectors import make_label, mask_emails


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