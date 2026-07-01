import re
import phonenumbers
from dateutil import parser


SKILL_MAP = {
    "py": "Python",
    "python": "Python",
    "python3": "Python",

    "js": "JavaScript",
    "javascript": "JavaScript",

    "react": "React",
    "reactjs": "React",

    "node": "Node.js",
    "nodejs": "Node.js",

    "cpp": "C++",
    "c++": "C++",

    "fastapi":"FastAPI",
    "ai":"Artificial Intelligence",
    "ml":"Machine Learning",
    "backend":"Backend Development",

    "ml": "Machine Learning",

    "ai": "Artificial Intelligence",
}


def normalize_name(name):
    if not name:
        return None
    return " ".join(name.strip().title().split())


def normalize_email(email):
    if not email:
        return None
    return email.strip().lower()


def normalize_phone(phone):
    if not phone:
        return None
    try:
        num = phonenumbers.parse(phone, "IN")
        if phonenumbers.is_valid_number(num):
            return phonenumbers.format_number(
                num,
                phonenumbers.PhoneNumberFormat.E164,
            )
    except Exception:
        return None
    return None


def normalize_date(value):
    if not value:
        return None

    try:
        return parser.parse(value).strftime("%Y-%m")
    except Exception:
        return None


def normalize_skill(skill):
    if not skill:
        return None

    s = skill.strip().lower()

    return SKILL_MAP.get(s, skill.strip().title())


def clean_text(text):
    if not text:
        return None

    text = re.sub(r"\s+", " ", text)
    return text.strip()