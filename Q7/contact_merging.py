import re
import time


def normalize_name(name):
    if not name:
        return ""
    lowered = name.lower()
    letters = re.sub(r"[^a-z0-9]+", " ", lowered).strip()
    return " ".join(letters.split())


def normalize_number(number):
    if not number:
        return ""
    digits = re.sub(r"\D", "", number)
    if len(digits) > 10:
        digits = digits[-10:]
    return digits


def merge_contacts(contacts):
    merged = {}
    for contact in contacts:
        primary_name = normalize_name(contact.get("name", ""))
        phone = normalize_number(contact.get("phone", ""))
        email = (contact.get("email") or "").strip().lower()
        key = phone or primary_name or "unknown"

        if key not in merged:
            merged[key] = {
                "name": primary_name or "Unknown",
                "phones": set(),
                "emails": set(),
            }

        if phone:
            merged[key]["phones"].add(phone)
        if email:
            merged[key]["emails"].add(email)
        if primary_name and merged[key]["name"] == "Unknown":
            merged[key]["name"] = primary_name

    return merged


def build_demo_contacts():
    return [
        {"name": "Dr. Ravi Kumar", "phone": "+91 98400 12345", "email": "ravi@gmail.com"},
        {"name": "ravi kumar", "phone": "9840012345", "email": "ravi.kumar@yahoo.com"},
        {"name": "Ananya Rao", "phone": "+91 99887 55666", "email": "ananya@outlook.com"},
        {"name": "ANANYA RAO", "phone": "9988755666", "email": "ananya.r@outlook.com"},
        {"name": "Ravi Kumar", "phone": "", "email": "ravi.kumar@proton.me"},
    ]


def benchmark_contacts(n_values=(1000, 100000)):
    for n in n_values:
        contacts = []
        for i in range(n):
            base = i % 7
            contacts.append({
                "name": ["Dr. Ravi Kumar", "ravi kumar", "Ananya Rao", "ANANYA RAO", "Sundar", "Meera", "Rohit"][base],
                "phone": ["+91 98400 12345", "9840012345", "+91 99887 55666", "9988755666", "+91 98760 00123", "9876000123", "+91 91234 56789"][base],
                "email": ["ravi@gmail.com", "ravi.kumar@yahoo.com", "ananya@outlook.com", "ananya.r@outlook.com", "sundar@test.com", "meera@test.com", "rohit@test.com"][base],
            })
            if i % 11 == 0:
                contacts[-1]["name"] = "Ravi Kumar"
                contacts[-1]["email"] = "ravi.kumar@proton.me"

        start = time.perf_counter()
        merge_contacts(contacts)
        elapsed = time.perf_counter() - start
        print(f"n={n:>6} | merge_time={elapsed:.6f}s")


if __name__ == "__main__":
    demo_contacts = build_demo_contacts()
    merged = merge_contacts(demo_contacts)
    print("Merged contacts:")
    for key, value in merged.items():
        print(key, value)

    print("\nBenchmark:")
    benchmark_contacts()
