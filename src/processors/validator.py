def validate_candidate(candidate):

    warnings = []

    if not candidate.full_name:
        warnings.append(
            "Missing candidate name"
        )

    if len(candidate.emails) == 0:
        warnings.append(
            "Missing email"
        )

    if len(candidate.phones) == 0:
        warnings.append(
            "Missing phone"
        )

    if candidate.overall_confidence < 0.60:

        warnings.append(
            "Low confidence profile"
        )

    for warning in warnings:

        print("WARNING:", warning)

    return True