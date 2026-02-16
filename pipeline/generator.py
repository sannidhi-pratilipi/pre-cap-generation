# from llm.client_gemini import complete_gemini
from llm.client_grok import complete_grok

def generate_hook(
    previous_chapter_text: str,
    current_chapter_text: str,
) -> str:

    prompt = f"""
    You write high-impact end-of-chapter hooks for stories across genres in the style of popular commercial fiction.

    Your objective is to create a hook that builds strong anticipation for the single most significant event in the next chapter.

    The hook must:
    • Clearly identify that dominant event
    • Reveal a concrete glimpse of it
    • Withhold its outcome or full implications

    The reader should feel both informed and compelled to continue.

    ────────────────────
    STEP 1: IDENTIFY THE CORE EVENT (SILENT)
    ────────────────────

    From the next chapter, determine:

    • What is the most consequential event?
    • Which moment changes power, direction, or stakes?
    • What confrontation, revelation, decision, arrival, exposure, or irreversible act dominates the chapter?
    • Once these are identified, reveal the event in the hook while expressing that the outcome or full implications is withheld so that reader becomes curious to read the next chapter
    If multiple things happen, choose the ONE event that drives the chapter forward most strongly.

    The hook must revolve around that event only.

    ────────────────────
    CORE PRINCIPLE
    ────────────────────

    This hook must be FORWARD-DRIVEN.

    Do not summarize the chapter just read
    Do not vaguely hint at “something big.”
    Do not mechanically forecast what “will” happen.

    Instead:

    • Enter the edge of the central event.
    • Reveal a specific, tangible element of it (who is involved, what action is taking place, what decision is being made, what secret is surfacing).
    • Withhold the outcome or consequence.

    The hook must feel grounded in an actual upcoming moment — not in abstract tension.

    ────────────────────
    GLIMPSE REQUIREMENT
    ────────────────────

    The hook must contain at least one concrete anchor from the next chapter, such as:

    • A specific confrontation
    • A key action being initiated
    • A decision already taken
    • A secret about to surface
    • An arrival, exposure, or irreversible move

    Do not create tension without referencing a real event.

    Mystery must come from partial revelation, not vagueness.

    ────────────────────
    FORMAT CONTROL
    ────────────────────

    The hook may be written as assertion or question or exclamation

    FORMAT RULES:

    1. Do NOT default to any one format.
    2. Do NOT repeatedly use any particular format across chapters.
    3. Variation between the formats must feel natural.

    The hook format must feel intentional, not habitual.

    ────────────────────
    ASSERTION OPTION
    ────────────────────

    If hook is written as an assertion:
    • It must reference the specific central event.
    • It must clearly imply stakes.
    • It must not be generic or philosophical.
    • It must not ask about feelings alone — it must ask about an action or consequence tied to the event.
    • No dialogues from the story
    • Include the mystery or shock or surprise that may come after assertion
    
    ────────────────────
    EXCLAMATION OPTION
    ────────────────────

    If hook is written as an exclamation:
    • It must reference the specific central event.
    • It must clearly imply stakes.
    • It must not be generic or philosophical.
    • It must not ask about feelings alone — it must ask about an action or consequence tied to the event.  
    • No dialogues from the story

    ────────────────────
    QUESTION OPTION
    ────────────────────

    If hook is written as a question:
    • It must reference the specific central event.
    • It must clearly imply stakes.
    • It must not be generic or philosophical.
    • It must not ask about feelings alone — it must ask about an action or consequence tied to the event.
    • No dialogues from the story

    ────────────────────
    STRUCTURAL RULES
    ────────────────────

    - Avoid repetitive forecasting patterns
    - Avoid including exact dialogue from the story
    - Vary rhythm and sentence construction naturally.
    - Do NOT similarize the hook to the previous hook
    - Do NOT use hypens or em-dashes
    - The hook may be:
    • A sharp declarative statement
    • A moment already unfolding
    • A focused reveal of an action or object
    • A power shift implication
    • A precise, high-stakes question

    ────────────────────
    YOU MUST
    ────────────────────

    • Write in the same language as the story
    • 1-2 sentences only
    • Maximum 30-35 words
    • Clearly anchor the hook to the single central event of the next chapter
    • Never include exact dialogue from the story
    • Reveal something concrete
    • Write in the same language and slang as the story
    • Not reveal the outcome
    • Avoid summarizing the previous chapter
    • Avoid poetic vagueness
    • Not resolve the tension

    The hook must stand alone and generate immediate forward pull.

    ────────────────────
    INPUTS
    ────────────────────
    Chapter just read:
    {previous_chapter_text}

    Next chapter (primary direction source):
    {current_chapter_text}

    ────────────────────
    INTERNAL QUALITY CHECK (SILENT)
    ────────────────────

    Before finalizing, ensure:

    ✓ The hook revolves around ONE dominant upcoming event
    ✓ A concrete element of that event is revealed
    ✓ The outcome remains unknown
    ✓ The wording is not formulaic
    ✓ The tension comes from partial exposure, not ambiguity
    ✓ If written as a question, it creates curiosity about the specific event
    ✓ The hook does not default to question format without strong narrative reason
    ✓ The format choice feels intentional and varied
    ✓ If written as an assertion, it references the specific event
    ✓ If written as an exclamation, it references surprise or shock

    Return only the hook text.
    No explanations.
    No labels.
    No markdown.
    """

    messages = [
        {
            "role": "system",
            "content": "You write restrained, spoiler-safe, forward-looking story hooks."
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
    # return complete_gemini(messages)
    return complete_grok(messages)
