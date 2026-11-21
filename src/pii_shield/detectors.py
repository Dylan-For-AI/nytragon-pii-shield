import re

LABEL_FORMAT = "[{label}]"
EMAIL_PATTERN = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")


def make_label(label):
    return LABEL_FORMAT.format(label=label)


def mask_emails(text):
    return EMAIL_PATTERN.sub(make_label("EMAIL"), text)


if __name__ == "__main__":
    exemple = (
        "Please contact Mr. Jean Bernard at his email address "
        "jean.bernard@saint-louis-clinic.fr for follow-up."
    )
    print(mask_emails(exemple))