import os
import json
from datetime import datetime

class SimpleChatbot:
    def __init__(self):
        self.conversation_history = []
        
    def get_response(self, user_input):
        # Simple rule-based responses
        responses = {
            "hello": "Hi there! How can I help you today?",
            "how are you": "I'm doing great! Thanks for asking.",
            "what can you do": "I can chat with you, answer questions, and help with various tasks!",
            "bye": "Goodbye! Have a great day!",
            "help": "Available commands: hello, how are you, what can you do, bye, help"
        }
        
        user_input_lower = user_input.lower().strip()
        
        # Check for exact matches first
        if user_input_lower in responses:
            response = responses[user_input_lower]
        else:
            # Check for partial matches
            for key in responses:
                if key in user_input_lower:
                    response = responses[key]
                    break
            else:
                response = "I'm not sure how to respond to that. Type 'help' for available commands."
        
        # Store conversation
        self.conversation_history.append({
            "timestamp": datetime.now().isoformat(),
            "user": user_input,
            "bot": response
        })
        
        return response
    
    def save_conversation(self, filename="conversation_log.json"):
        with open(filename, 'w') as f:
            json.dump(self.conversation_history, f, indent=2)
    
    def run(self):
        print("🤖 Simple Chatbot Started!")
        print("Type 'quit' to exit or 'help' for commands\n")
        
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit']:
                print("Bot: Goodbye!")
                self.save_conversation()
                break
            
            if not user_input:
                continue
                
            response = self.get_response(user_input)
            print(f"Bot: {response}")

if __name__ == "__main__":
    chatbot = SimpleChatbot()
    chatbot.run()