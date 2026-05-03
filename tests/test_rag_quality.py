from app.rag.answer_generator import generate_answer


def test_mars_11th_retrieval():
    response = generate_answer("mars in 11th house gains through friends")

    assert response["parsed_query"]["planet"] == "Mars"
    assert response["parsed_query"]["house"] == "11"
    assert len(response["sources"]) >= 1

    top_source = response["sources"][0]
    assert "Mars" in top_source["metadata"]["planets"]
    assert "11" in top_source["metadata"]["houses"]


def test_answer_is_grounded():
    response = generate_answer("mars in 11th house gains through friends")
    answer = response["answer"].lower()

    assert "gains" in answer
    assert "recognition" in answer
    assert "social influence" in answer
    assert "networks" in answer or "friends" in answer


def test_answer_avoids_absolute_claims():
    response = generate_answer("mars in 11th house gains through friends")
    answer = response["answer"].lower()

    forbidden = [
        "definitely",
        "guaranteed",
        "will certainly",
        "must happen",
        "100%"
    ]

    for phrase in forbidden:
        assert phrase not in answer