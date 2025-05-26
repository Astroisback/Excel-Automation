import pandas as pd
import requests
import time

# conifgs
bot_token = "token"   
receiver_chat_id = "987654321"                       
message_file = "messages_output.csv"                 
delay_seconds = 2                                    
message_data = pd.read_csv(message_file)

def send_message_to_telegram(content):
    api_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        "chat_id": receiver_chat_id,
        "text": content
    }
    response = requests.post(api_url, data=payload)
    return response.status_code, response.text

for i, row in message_data.iterrows():
    user_email = row.get('email', 'unknown')
    custom_message = row.get('message', '')

    status, response = send_message_to_telegram(custom_message)

    if status == 200:
        print(f" Message [{i+1}] sent to {user_email}")
    else:
        print(f" Failed to send message [{i+1}] to {user_email}. Error: {response}")

    time.sleep(delay_seconds)

print("All messages have been processed and sent!")
