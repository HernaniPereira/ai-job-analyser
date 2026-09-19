from analyzer import find_technologies


def test_find_technologies():
    technologies = ["Python", "React", "Docker"]
    job = "We are looking for someone with Python and Docker."
    result = find_technologies(technologies, job)
    assert result == ["Python", "Docker"]


def test_find_technologies_case_insensitive():
    technologies = ["Python", "React", "Docker"]
    job = "We are looking for someone with python and docker."
    result = find_technologies(technologies, job)
    assert result == ["Python", "Docker"]


def test_find_technologies_no_match():
    technologies = ["Python", "React", "Docker"]
    job = "We are looking for someone with Java and Angular."
    result = find_technologies(technologies, job)
    assert result == []
