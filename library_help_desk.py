"""
library_help_desk.py

A simple Python library that acts as a help desk for library users.
Automatically answers common questions about the library.
"""

class LibraryHelpDesk:
    def __init__(self):
        # Dictionary of FAQs and answers
        self.responses = {
            "opening hours": "🕒 Our library is open from 9 AM to 8 PM, Monday to Saturday.",
            "membership": "📋 You can apply for membership online or at the help desk. Bring a valid ID proof!",
            "late fee": "💰 The late fee is $0.50 per day per book after the due date.",
            "borrow books": "📚 You can borrow up to 5 books at a time for 2 weeks.",
            "return books": "🔄 Books can be returned at the front desk or through our 24/7 drop box.",
            "contact": "☎️ You can contact us at +1-234-567-8901 or help@library.com.",
            "events": "🎉 We host events every month! Check our website or notice board for updates."
        }

    def get_response(self, user_question: str) -> str:
        """
        Find and return an answer based on the user question.
        """
        user_question = user_question.lower()
        for keyword, answer in self.responses.items():
            if keyword in user_question:
                return answer
        return "❓ Sorry, I don't have an answer for that. Please contact the librarian directly!"

if __name__ == "__main__":
    # Simple interactive help desk when run directly
    desk = LibraryHelpDesk()
    print("Welcome to the 📚 Library Help Desk!")
    print("Type your question (or 'exit' to quit):")

    while True:
        question = input("You: ")
        if question.lower() in ['exit', 'quit']:
            print("Goodbye! 👋")
            break
        answer = desk.get_response(question)
        print(f"Help Desk: {answer}")
