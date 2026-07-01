from transformer import CandidateTransformer


def test_transformer():

    transformer = CandidateTransformer()

    result = transformer.run("config/default.json")

    assert result["full_name"] == "Kevin Shah"

    assert len(result["emails"]) > 0

    assert len(result["phones"]) > 0

    assert len(result["skills"]) > 0

    assert result["overall_confidence"] > 0