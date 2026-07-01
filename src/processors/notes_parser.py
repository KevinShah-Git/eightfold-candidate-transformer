import re

from models import Skill


def parse_notes(candidate, text):

    if not text:
        return candidate

    lower = text.lower()

    if "backend" in lower:

        candidate.skills.append(

            Skill(
                name="Backend Development",
                confidence=0.60,
                sources=["notes"],
            )

        )

    if "artificial intelligence" in lower:

        candidate.skills.append(

            Skill(
                name="Artificial Intelligence",
                confidence=0.60,
                sources=["notes"],
            )

        )

    if "communication" in lower:

        candidate.skills.append(

            Skill(
                name="Communication",
                confidence=0.60,
                sources=["notes"],
            )

        )

    match = re.search(
        r"preferred location:\s*(.*)",
        text,
        re.I,
    )

    if match:

        candidate.location.city = (match.group(1).strip().rstrip("."))

    return candidate