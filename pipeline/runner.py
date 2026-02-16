from pipeline.generator import generate_hook
from pipeline.validator import validate_hook

def process_chapter(
    chapter_id: str,
    previous_chapter_text: str,
    current_chapter_text: str
):
    print(f"Generating hook for chapter {chapter_id}...")

    hook = generate_hook(
        previous_chapter_text=previous_chapter_text,
        current_chapter_text=current_chapter_text
    )

    if not validate_hook(hook):
        hook = generate_hook(
            previous_chapter_text=previous_chapter_text,
            current_chapter_text=current_chapter_text
        )

    # out = Path(f"hook_output/new_hooks_english/{chapter_id}.txt")
    # out.parent.mkdir(parents=True, exist_ok=True)
    # out.write_text(hook, encoding="utf-8")

    return hook
