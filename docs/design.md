# Candidate Profile Transformer – Technical Design

**Author:** Kevin Shah  
**Email:** kevinshah204@gmail.com  
**University:** Pandit Deendayal Energy University

---

## Objective

The Candidate Profile Transformer consolidates candidate information from multiple structured and unstructured sources into a single canonical candidate profile. The system resolves conflicts, normalizes data, tracks provenance, and calculates confidence scores while supporting configurable output.

---

## Architecture

```
CSV / JSON / TXT
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
 Provenance Tracking
        │
        ▼
 Confidence Scoring
        │
        ▼
 Validation
        │
        ▼
 Projection Engine
        │
        ▼
   JSON Output
```

---

## Components

### Loaders

Responsible for reading candidate information from:

- Recruiter CSV
- ATS JSON
- GitHub JSON
- LinkedIn JSON
- Notes TXT

---

### Normalizer

Normalizes:

- Name
- Email
- Phone
- Skills
- Country

into a common format.

---

### Merge Engine

Merges records using source priority.

Priority:

1. Recruiter
2. ATS
3. LinkedIn
4. GitHub
5. Notes

Rules:

- Higher priority wins.
- Empty values ignored.
- Skills merged as union.
- Duplicate values removed.

---

### Provenance

Each merged field stores:

- Source
- Merge Method

This provides traceability.

---

### Confidence

Each source contributes a confidence score.

| Source | Confidence |
|---------|------------|
| Recruiter | 1.00 |
| ATS | 0.95 |
| LinkedIn | 0.90 |
| GitHub | 0.85 |
| Notes | 0.60 |

Overall confidence is calculated as the average of contributing fields.

---

### Validation

Checks:

- Candidate Name
- Email
- Phone
- Confidence Score

Missing fields generate warnings instead of terminating execution.

---

## Assumptions

- One candidate is processed at a time.
- Recruiter data is most trusted.
- Notes provide supplemental information.
- Country codes follow ISO-3166 Alpha-2.
- Phone numbers follow E164 format.

---

## Future Improvements

- REST API
- Database persistence
- Better NLP for notes
- Multiple candidate support
- UI Dashboard