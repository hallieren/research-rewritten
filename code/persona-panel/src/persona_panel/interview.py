"""Interview prompt rendering and option extraction."""
import re

TEMPLATE = """You are answering a survey as the following person. Stay fully in character; \
answer as this person genuinely would, not as an AI assistant.

{card}

Survey question:
{question}

Options:
{options}

Reply with the option number only."""

OPT_RE = re.compile(r"\d+")


def render(card, question, options):
    opts = "\n".join(f"{code}. {label}" for code, label in options)
    return TEMPLATE.format(card=card, question=question, options=opts)


def extract_option(text, valid_codes):
    m = OPT_RE.search(text)
    return m.group(0) if m and m.group(0) in valid_codes else None
