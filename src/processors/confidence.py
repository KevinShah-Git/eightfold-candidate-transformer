SOURCE_CONFIDENCE = {

    "recruiter":1.00,

    "ats":0.95,

    "linkedin":0.90,

    "github":0.85,

    "notes":0.60,

}


def calculate_confidence(candidate):

    if len(candidate.provenance)==0:

        candidate.overall_confidence=0

        return candidate

    total=0

    seen=[]

    for item in candidate.provenance:

        if item.field in seen:

            continue

        seen.append(item.field)

        total+=SOURCE_CONFIDENCE.get(
            item.source,
            0.50,
        )

    candidate.overall_confidence=round(
        total/len(seen),
        2,
    )

    return candidate