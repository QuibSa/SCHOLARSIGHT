from typing import Dict
from openai import OpenAI
import os
import textwrap

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def fallback_summary(text: str) -> str:
    """
    Simple extractive fallback summarizer.
    """
    sentences = text.split(".")
    return ". ".join(sentences[:4]).strip() + "."

def summarize_sections(sections: Dict[str, str]) -> Dict[str, str]:
    summaries = {}

    for section, content in sections.items():
        try:
            prompt = f"""
You are an academic assistant.
Summarize the following {section} section of a research paper
in 4–5 concise, technical sentences.

Section text:
{content}
"""

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
            )

            summaries[section] = response.choices[0].message.content.strip()

        except Exception as e:
            # 🔁 FALLBACK MODE
            summaries[section] = (
                "[Fallback summary due to API quota]\n"
                + fallback_summary(content)
            )

    return summaries
