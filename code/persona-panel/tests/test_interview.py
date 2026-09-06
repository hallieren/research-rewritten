from persona_panel.interview import extract_option, render


def test_render_lists_options_and_card():
    p = render("- Age: 30", "Happy?", [["1", "Yes"], ["2", "No"]])
    assert "1. Yes" in p and "- Age: 30" in p and "Happy?" in p


def test_extract_option():
    assert extract_option("I'd say 2.", {"1", "2"}) == "2"
    assert extract_option("Option 10", {"1", "10"}) == "10"
    assert extract_option("none of these", {"1"}) is None
    assert extract_option("7", {"1", "2"}) is None
