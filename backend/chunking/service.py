def create_chunks(segments, max_words=100):
    chunks = []

    current_text = []
    chunk_start = None
    chunk_end = None
    word_count = 0

    for segment in segments:
        text = segment["text"].strip()
        words = text.split()

        if chunk_start is None:
            chunk_start = segment["start"]

        current_text.extend(words)
        word_count += len(words)
        chunk_end = segment["end"]

        if word_count >= max_words:
            chunks.append({
                "text": " ".join(current_text),
                "start": chunk_start,
                "end": chunk_end
            })

            current_text = []
            word_count = 0
            chunk_start = None

    # Add remaining words
    if current_text:
        chunks.append({
            "text": " ".join(current_text),
            "start": chunk_start,
            "end": chunk_end
        })

    return chunks