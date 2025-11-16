import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'python-chatbot'))

from chatbot import SimpleChatbot

def test_simple_chatbot():
    """Test the simple rule-based chatbot"""
    bot = SimpleChatbot()
    
    test_cases = [
        ("hello", "Hi there! How can I help you today?"),
        ("how are you", "I'm doing great! Thanks for asking."),
        ("help", "Available commands: hello, how are you, what can you do, bye, help"),
        ("random text", "I'm not sure how to respond to that. Type 'help' for available commands.")
    ]
    
    print("🧪 Testing Simple Chatbot...")
    for user_input, expected in test_cases:
        response = bot.get_response(user_input)
        status = "✅" if response == expected else "❌"
        print(f"{status} Input: '{user_input}' -> Response: '{response}'")

if __name__ == "__main__":
    test_simple_chatbot()