import pandas as pd
from string import Template

class MessageGenerator:
    """Generate personalized messages based on event attendance and profile info."""
    def __init__(self):
        self.templates = {

            'joined': Template(

                "Hi $first_name,\n\n"
                "Thank you for joining our recent event! We were glad to have someone with your expertise as a $job there. "
                "It was great to meet you in person. We’ll follow up soon with additional resources related to the topics covered.\n\n"
                "Best regards,\nThe Team"

            ),

            'not_joined': Template(

                "Hi $first_name,\n\n"
                "We missed you at our recent event. As a $job in the industry, we think you would have found it valuable. "
                "We’ll keep you posted on future events that might interest you. "
                "In the meantime, feel free to reach out if you have any questions or ideas.\n\n"
                "Warm regards,\nThe Team"

            )
        }
        
        self.linkedin_note = "\n\nP.S. We couldn't find your LinkedIn profile. If you have one, please share it so we can connect professionally."

    def generate(self, first_name, job, joined, has_linkedin):
        key = 'joined' if joined else 'not_joined'
        msg = self.templates[key].substitute(first_name=first_name, job=job or "professional")
        if not has_linkedin:
            msg += self.linkedin_note
        return msg
    
def main():
    df = pd.read_csv('cleaned_output.csv')
    gen = MessageGenerator()
    messages = []
    for _, row in df.iterrows():
        first_name = row['Name'].split()[0]
        has_linkedin = not row['linkedin_flag']
        msg_text = gen.generate(
            first_name=first_name,
            job=row['Job Title'],
            joined=row['has_joined'],
            has_linkedin=has_linkedin
        )
        messages.append({'email': row['Email'], 'message': msg_text})
        with open(f"{row['Email']}.txt", 'w') as f:
            f.write(msg_text)
    pd.DataFrame(messages).to_csv('messages_output.csv', index=False)

if __name__ == "__main__":
    main()
