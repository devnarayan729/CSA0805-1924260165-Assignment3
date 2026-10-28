def count_words(complaints, stop_words):
    """Count words in a list of complaint strings using dict.get()."""
    counts = {}
    for complaint in complaints:
        for word in complaint.lower().replace("-", " ").split():
            cleaned = word.strip(".,;:!?\"'")
            if not cleaned or cleaned in stop_words:
                continue
            counts[cleaned] = counts.get(cleaned, 0) + 1
    return counts


def group_by_district(complaints):
    """Group complaint text by district, using setdefault()."""
    by_district = {}
    for item in complaints:
        district = item["district"]
        by_district.setdefault(district, []).append(item["text"])
    return by_district


def top_k_words(word_counts, k):
    """Return top k words sorted by count desc, then alphabetically."""
    return sorted(word_counts.items(), key=lambda item: (-item[1], item[0]))[:k]


if __name__ == "__main__":
    stop_words = {
        "the", "and", "for", "with", "from", "in", "on", "at", "to", "is", "of", "a",
        "an", "was", "were", "their", "this", "that", "are", "it", "as", "by", "be"
    }

    complaints = [
        {"district": "Chennai", "text": "Low rainfall in tomato field and pest attack in Chennai"},
        {"district": "Coimbatore", "text": "Cotton crop affected by disease in Coimbatore"},
        {"district": "Chennai", "text": "Water logging in paddy field and poor drainage in Chennai"},
        {"district": "Madurai", "text": "Need guidance for maize crop management in Madurai"},
        {"district": "Coimbatore", "text": "Pest attack on cotton crop and fertilizer shortage"},
    ]

    word_counts = count_words([item["text"] for item in complaints], stop_words)
    print("Word frequencies:", word_counts)
    print("Top 5 words:", top_k_words(word_counts, 5))

    districts = group_by_district(complaints)
    print("Complaints by district:")
    for district, texts in districts.items():
        print(f"  {district}: {texts}")
