import re

LABEL_FORMAT = "[{label}]"
EMAIL_PATTERN = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
PHONE_PATTERN = re.compile(r"(?<!\d)(?:\+33\s?|0)[1-9](?:[\s.-]?\d{2}){4}(?!\d)")
SSN_PATTERN = re.compile(
    r"(?<!\d)[12]\s?\d{2}\s?(?:0[1-9]|1[0-2])\s?(?:\d{2}|2[AB])\s?\d{3}\s?\d{3}\s?\d{2}(?!\d)"
)


def make_label(label):
    return LABEL_FORMAT.format(label=label)


def mask_emails(text):
    return EMAIL_PATTERN.sub(make_label("EMAIL"), text)


def mask_phones(text):
    return PHONE_PATTERN.sub(make_label("PHONE"), text)


def mask_ssn(text):
    return SSN_PATTERN.sub(make_label("SSN"), text)


def mask_all(text):
    text = mask_ssn(text)
    text = mask_phones(text)
    text = mask_emails(text)
    return text


def find_emails(text):
    return [
        {"type": "EMAIL", "start": m.start(), "end": m.end()}
        for m in EMAIL_PATTERN.finditer(text)
    ]

def find_phones(text):
    return [
        {"type": "PHONE", "start": m.start(), "end": m.end()}
        for m in PHONE_PATTERN.finditer(text)
    ]


def find_ssn(text):
    return [
        {"type": "SSN", "start": m.start(), "end": m.end()}
        for m in SSN_PATTERN.finditer(text)
    ]


if __name__ == "__main__":
    exemple = (
        "Please contact Mr. Jean Bernard at his email address "
        "jean.bernard@saint-louis-clinic.fr, phone 06 12 34 56 78."
    )
    print(mask_all(exemple))
