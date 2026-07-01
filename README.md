# Candidate Profile Transformer

## Author

**Kevin Shah**

Email: kevinshah204@gmail.com

University: Pandit Deendayal Energy University

---

# Overview

The Candidate Profile Transformer is a Python application that consolidates candidate information from multiple structured and unstructured data sources into a single canonical candidate profile.

The application performs:

- Multi-source data ingestion
- Data normalization
- Conflict resolution
- Candidate profile merging
- Confidence score calculation
- Provenance tracking
- Configurable output generation
- Validation

---

# Supported Sources

### Structured Sources

- Recruiter CSV
- ATS JSON
- LinkedIn JSON
- GitHub JSON

### Unstructured Source

- Notes TXT

---

# Project Structure

```
eightfold-candidate-transformer
│
├── config
│   ├── default.json
│   └── custom.json
│
├── data
│   ├── recruiter.csv
│   ├── ats.json
│   ├── github.json
│   ├── linkedin.json
│   └── notes.txt
│
├── docs
│
├── output
│
├── src
│   ├── main.py
│   ├── transformer.py
│   ├── models.py
│   │
│   ├── loaders
│   │   ├── csv_loader.py
│   │   ├── json_loader.py
│   │   └── text_loader.py
│   │
│   └── processors
│       ├── merger.py
│       ├── normalizer.py
│       ├── validator.py
│       ├── confidence.py
│       ├── provenance.py
│       ├── projection.py
│       └── notes_parser.py
│
├── tests
│
├── requirements.txt
│
└── README.md
```

---

# Installation

Clone the repository and install dependencies.

```bash
pip install -r requirements.txt
```

---

# Dependencies

- pandas
- pydantic
- phonenumbers
- python-dateutil

---

# Running the Project

### Default Configuration

```bash
python src/main.py
```

The output is generated inside:

```
output/result.json
```

---

### Custom Configuration

```bash
python src/main.py --config config/custom.json --output output/custom.json
```

The output is generated inside:

```
output/custom.json
```

---

# Processing Pipeline

```
Input Sources
      │
      ▼
Loaders
      │
      ▼
Normalization
      │
      ▼
Merge Engine
      │
      ▼
Validation
      │
      ▼
Confidence Scoring
      │
      ▼
Projection
      │
      ▼
Output JSON
```

---

# Merge Strategy

The merge engine follows a source priority approach.

Priority order:

1. Recruiter
2. ATS
3. LinkedIn
4. GitHub
5. Notes

Rules:

- First valid value wins.
- Empty values are ignored.
- Skills are merged as a union.
- Duplicate values are removed.
- Higher priority sources override lower priority sources.

---

# Normalization

The following normalization is applied:

| Field | Normalization |
|--------|---------------|
| Name | Title Case |
| Email | Lowercase |
| Phone | E164 Format |
| Skills | Canonical Skill Names |
| Country | ISO-3166 Alpha-2 |

---

# Confidence Scoring

Confidence values assigned to each source:

| Source | Confidence |
|----------|-----------|
| Recruiter | 1.00 |
| ATS | 0.95 |
| LinkedIn | 0.90 |
| GitHub | 0.85 |
| Notes | 0.60 |

Overall confidence is calculated using the average confidence of all contributing fields.

---

# Provenance Tracking

Each merged field stores:

- Source
- Merge Method

This enables traceability and auditing of merged information.

---

# Validation

The validator checks:

- Candidate name
- Email
- Phone number
- Confidence score

Missing information generates warnings instead of stopping execution.

---

# Sample Commands

Run using default configuration:

```bash
python src/main.py
```

Run using custom configuration:

```bash
python src/main.py --config config/custom.json --output output/custom.json
```

---

# Sample Output

Example fields generated:

- Full Name
- Emails
- Phones
- Skills
- Experience
- Education
- Links
- Location
- Confidence Score

---

# Assumptions

- One candidate is processed at a time.
- Recruiter data has the highest priority.
- Notes provide supplemental information.
- Skills are merged without duplication.
- Missing values are handled gracefully.

---

# Future Improvements

- Support multiple candidates.
- REST API using FastAPI.
- Database integration.
- Improved NLP for notes parsing.
- Advanced confidence calculation.
- Web interface.