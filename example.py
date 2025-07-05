from library_help_desk import LibraryHelpDesk

def main():
    desk = LibraryHelpDesk()
    questions = [
        "What are your opening hours?",
        "Tell me about membership.",
        "How much is the late fee?",
        "How can I borrow books?",
        "Do you host events?"
    ]

    for q in questions:
        print(f"❓ {q}")
        print(f"✅ {desk.get_response(q)}\n")

if __name__ == "__main__":
    main()
