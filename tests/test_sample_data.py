import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.sample_data import POLICY_CATEGORIES, get_sample, get_sample_names


def test_at_least_four_samples():
    assert len(get_sample_names()) >= 4


def test_each_sample_has_required_fields():
    for name in get_sample_names():
        sample = get_sample(name)
        assert sample["category"] in POLICY_CATEGORIES
        assert sample["policy_text"].strip()
        assert sample["sample_question"].strip()


def test_unknown_sample_returns_none():
    assert get_sample("does-not-exist") is None
