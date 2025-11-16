import os
from dotenv import load_dotenv
import openai

load_dotenv()

class AIChatbot:
    def __init__(self):
        self.client = openai.OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
        self.conversation = [
            {"role": "system", "content": "You are a helpful AI assistant."}
        ]
    
    def chat(self, message):
        self.conversation.append({"role": "user", "content": message})
        
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=self.conversation,
                max_tokens=150,
                temperature=0.7
            )
            
            ai_response = response.choices[0].message.content
            self.conversation.append({"role": "assistant", "content": ai_response})
            
            return ai_response
            
        except Exception as e:
            return f"Error: {str(e)}"
    
    def run(self):
        print("🤖 AI Chatbot (OpenAI GPT-3.5)")
        print("Type 'quit' to exit\n")
        
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit']:
                print("Bot: Goodbye!")
                break
            
            if not user_input:
                continue
                
            response = self.chat(user_input)
            print(f"Bot: {response}")

if __name__ == "__main__":
    if not os.getenv('OPENAI_API_KEY'):
        print("Please set OPENAI_API_KEY in .env file")
    else:
        chatbot = AIChatbot()
        chatbot.run()