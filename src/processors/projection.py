from pydantic import BaseModel


def get_value(data, path):
    value = data

    for part in path.split("."):

        if isinstance(value, BaseModel):
            value = getattr(value, part, None)

        elif isinstance(value, dict):
            value = value.get(part)

        else:
            return None

    return value


def project_candidate(candidate, config):

    output = {}

    candidate = candidate.model_dump()

    include_confidence = config.get(
        "include_confidence",
        True,
    )

    on_missing = config.get(
        "on_missing",
        "null",
    )

    for field in config["fields"]:

        source = field.get(
            "from",
            field["path"],
        )

        value = get_value(candidate, source)

        if value is None:

            if on_missing == "omit":
                continue

            if on_missing == "null":
                output[field["path"]] = None
                continue

            raise ValueError(
                f"Missing {field['path']}"
            )

        output[field["path"]] = value

    if include_confidence:

        output["overall_confidence"] = candidate[
            "overall_confidence"
        ]

    return output