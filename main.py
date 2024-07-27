# Importing necessary libraries
import random

# Sample data
resources = {
    'articles': [
        "Understanding Anxiety",
        "Coping Strategies for Depression",
        "How to Build Resilience"
    ],
    'videos': [
        "Meditation for Beginners",
        "Managing Stress Effectively",
        "Cognitive Behavioral Therapy Overview"
    ],
    'podcasts': [
        "Mental Health Matters",
        "The Therapist's Corner",
        "Healing Through Conversation"
    ],
    'downloads': [
        "Self-Care Checklist",
        "Daily Mood Tracker",
        "Guided Meditation Scripts"
    ]
}

therapists = [
    {"name": "Dr. Jane Smith", "location": "New York", "specialty": "Anxiety", "insurance": "ABC Insurance"},
    {"name": "Dr. John Doe", "location": "San Francisco", "specialty": "Depression", "insurance": "XYZ Insurance"},
    {"name": "Dr. Emily Davis", "location": "Los Angeles", "specialty": "Counseling", "insurance": "123 Insurance"},
]

# Functions

def display_resources():
    print("Resource Hub:")
    for category, items in resources.items():
        print(f"\n{category.capitalize()}:")
        for item in items:
            print(f" - {item}")

def chat_support():
    responses = [
        "I'm here to listen. Can you tell me more about what's going on?",
        "It sounds like you're going through a tough time. Have you tried any coping strategies?",
        "Remember, you're not alone. Would you like information on local therapists?"
    ]
    print("\nChat Support:")
    print(random.choice(responses))

def search_therapists(location=None, specialty=None, insurance=None):
    print("\nProfessional Therapist Local Listing:")
    for therapist in therapists:
        if (location is None or therapist['location'] == location) and \
           (specialty is None or therapist['specialty'] == specialty) and \
           (insurance is None or therapist['insurance'] == insurance):
            print(f"Name: {therapist['name']}, Location: {therapist['location']}, Specialty: {therapist['specialty']}, Insurance: {therapist['insurance']}")

# Main function to simulate platform usage
def main():
    print("Welcome to the Mental Health Support Platform!")
    display_resources()
    chat_support()
    search_therapists(location="New York", specialty="Anxiety")

if __name__ == "__main__":
    main()
