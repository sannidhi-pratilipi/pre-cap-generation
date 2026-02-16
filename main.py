# def main():
#     series_slug = "ouc3uvpuaug1"
#     ingestor = ChapterIngestor()
#     previous_chapter_text = None
#     chapter_index = 1
#     for current_chapter_text in ingestor.iter_series_chapters(
#         series_slug,
#         language="hi"
#     ):
#         if previous_chapter_text is None:
#             previous_chapter_text = current_chapter_text
#             continue
#         process_chapter(
#             chapter_id=f"chapter_{chapter_index}",
#             previous_chapter_text=previous_chapter_text,
#             current_chapter_text=current_chapter_text,
#         )
#         previous_chapter_text = current_chapter_text
#         chapter_index += 1

from concurrent.futures import ThreadPoolExecutor, as_completed
from ingestion.ingest_chapter import ChapterIngestor
from pipeline.runner import process_chapter
import pandas as pd

def hook_worker(series_slug, idx, prev_text, curr_text):
    chapter_number = idx + 1

    hook = process_chapter(
        chapter_id=f"{series_slug}_chapter_{chapter_number}",
        previous_chapter_text=prev_text,
        current_chapter_text=curr_text,
    )
    return chapter_number, hook

def main():
    series_slug = "wxljcrzqxhlj"
    # series_slug = "6cpqfrtqn8dk"
    ingestor = ChapterIngestor()

    chapters = list(
        ingestor.iter_series_chapters(series_slug, language="hi")
    )
    # chapters =fetch_chapters_from_html_file(
    #     "orqd3inphyvb.html"
    # )
    if len(chapters) < 2:
        print("Not enough chapters to generate hooks")
        return

    chapter_pairs = [
        (i, chapters[i - 1], chapters[i])
        for i in range(1, len(chapters))
    ]

    results = []

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = [
            executor.submit(
                hook_worker,
                series_slug,
                idx,
                prev_text,
                curr_text,
            )
            for idx, prev_text, curr_text in chapter_pairs
        ]

        for future in as_completed(futures):
            try:
                results.append(future.result())
            except Exception as e:
                print(f"Hook generation failed: {e}")

    results.sort(key=lambda x: x[0])

    df = pd.DataFrame(results, columns=["chapter_number", "hook"])
    output_file = f"{series_slug}_grok.xlsx"
    df.to_excel(output_file, index=False)

    print(f"Results stored in Excel sheet: {output_file}")

if __name__ == "__main__":
    main()
