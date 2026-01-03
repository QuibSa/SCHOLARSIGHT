import re
from typing import Dict

SECTION_HEADERS = [
    "abstract",
    "introduction",
    "method",
    "methodology",
    "materials and methods",
    "results",
    "discussion",
    "conclusion",
    "limitations",
]

def extract_sections(text: str) -> Dict[str, str]:
    """
    Extract major research paper sections using robust heuristics.
    """
    sections = {}
    text_lower = text.lower()

    matches = []

    for header in SECTION_HEADERS:
        pattern = rf"\n\s*(\d+\.?\s*)?{header}\s*[:\-]?\s*\n"
        for match in re.finditer(pattern, text_lower):
            matches.append((match.start(), header))

    matches.sort()

    for i, (start_idx, header) in enumerate(matches):
        end_idx = len(text)
        if i + 1 < len(matches):
            end_idx = matches[i + 1][0]

        section_text = text[start_idx:end_idx].strip()
        sections[header] = section_text

    return sections
