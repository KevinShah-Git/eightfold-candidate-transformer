from models import Candidate, Skill, Experience, Education

from processors.normalizer import (
    normalize_name,
    normalize_email,
    normalize_phone,
    normalize_skill,
)

from processors.provenance import add_provenance
from processors.confidence import calculate_confidence


def merge_candidate(records):

    candidate = Candidate()

    # ---------------- Recruiter ----------------

    recruiter = records.get("recruiter", {})

    if recruiter:

        candidate.full_name = normalize_name(
            recruiter.get("name")
        )

        if recruiter.get("email"):

            email = normalize_email(
                recruiter["email"]
            )

            if email:
                candidate.emails.append(email)

        if recruiter.get("phone"):

            phone = normalize_phone(
                recruiter["phone"]
            )

            if phone:
                candidate.phones.append(phone)

        candidate.headline = recruiter.get("title")

        location = recruiter.get("location")

        if location:

            if "India" in location:

                candidate.location.city = (
                    location.replace(
                        "India",
                        ""
                    ).strip()
                )

                candidate.location.country = "IN"

        add_provenance(
            candidate,
            "full_name",
            "recruiter",
            "extract"
        )

    # ---------------- ATS ----------------

    ats = records.get("ats", {})

    if ats:

        if not candidate.full_name:

            candidate.full_name = normalize_name(
                ats.get("candidateName")
            )

        email = normalize_email(
            ats.get("emailAddress")
        )

        if email and email not in candidate.emails:

            candidate.emails.append(email)

        phone = normalize_phone(
            ats.get("mobile")
        )

        if phone and phone not in candidate.phones:

            candidate.phones.append(phone)

        candidate.years_experience = ats.get(
            "experience"
        )

        for skill in ats.get("skills", []):

            skill = normalize_skill(skill)

            exists = any(
                s.name.lower() == skill.lower()
                for s in candidate.skills
            )

            if not exists:

                candidate.skills.append(

                    Skill(
                        name=skill,
                        confidence=0.95,
                        sources=["ats"],
                    )

                )

        add_provenance(
            candidate,
            "skills",
            "ats",
            "extract"
        )

    # ---------------- GitHub ----------------

    github = records.get("github", {})

    if github:

        candidate.links.github = github.get(
            "github"
        )

        if not candidate.headline:

            candidate.headline = github.get("bio")

        for language in github.get(
            "languages",
            [],
        ):

            language = normalize_skill(language)

            exists = any(
                s.name.lower() == language.lower()
                for s in candidate.skills
            )

            if not exists:

                candidate.skills.append(

                    Skill(
                        name=language,
                        confidence=0.85,
                        sources=["github"],
                    )

                )

        add_provenance(
            candidate,
            "github",
            "github",
            "extract"
        )

    # ---------------- LinkedIn ----------------

    linkedin = records.get(
        "linkedin",
        {},
    )

    if linkedin:

        candidate.headline = linkedin.get(
            "headline",
            candidate.headline,
        )

        for exp in linkedin.get(
            "experience",
            [],
        ):

            candidate.experience.append(

                Experience(
                    company=exp.get("company"),
                    title=exp.get("title"),
                    start=exp.get("start"),
                    end=exp.get("end"),
                )

            )

        for edu in linkedin.get(
            "education",
            [],
        ):

            candidate.education.append(

                Education(
                    institution=edu.get(
                        "institution"
                    ),
                    degree=edu.get("degree"),
                )

            )

        location = linkedin.get(
            "location"
        )

        if location:

            if "," in location:

                city, country = [
                    x.strip()
                    for x in location.split(",", 1)
                ]

                country_map = {
                    "india": "IN",
                    "usa": "US",
                    "united states": "US",
                    "uk": "GB",
                }

                candidate.location.city = city

                candidate.location.country = (
                    country_map.get(
                        country.lower(),
                        country,
                    )
                )

        add_provenance(
            candidate,
            "experience",
            "linkedin",
            "extract",
        )

    calculate_confidence(candidate)

    return candidate