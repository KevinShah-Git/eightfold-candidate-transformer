import json

from loaders.csv_loader import load_csv
from loaders.json_loader import load_json
from loaders.text_loader import load_text

from processors.merger import merge_candidate
from processors.validator import validate_candidate
from processors.projection import project_candidate
from processors.notes_parser import parse_notes


class CandidateTransformer:

    def __init__(self):

        self.sources = {
            "recruiter": "data/recruiter.csv",
            "ats": "data/ats.json",
            "linkedin": "data/linkedin.json",
            "github": "data/github.json",
            "notes": "data/notes.txt"
        }

    def load_sources(self):

        data = {}

        data["recruiter"] = load_csv(self.sources["recruiter"])
        data["ats"] = load_json(self.sources["ats"])
        data["linkedin"] = load_json(self.sources["linkedin"])
        data["github"] = load_json(self.sources["github"])

        try:
            data["notes"] = load_text(self.sources["notes"])
        except Exception:
            data["notes"] = ""

        return data

    def run(self, config_path):

        sources = self.load_sources()

        # Merge all structured sources
        candidate = merge_candidate(sources)

        # Parse unstructured notes
        candidate = parse_notes(
            candidate,
            sources.get("notes", "")
        )

        # Validate final candidate
        validate_candidate(candidate)

        # Load output configuration
        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)

        # Generate output
        output = project_candidate(candidate, config)

        return output