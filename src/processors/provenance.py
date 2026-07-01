from models import Provenance


def add_provenance(candidate, field, source, method):

    candidate.provenance.append(

        Provenance(
            field=field,
            source=source,
            method=method,
        )

    )