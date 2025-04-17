# fortune.py
import random

def main():
    name = "Indraudh Sarkar"        
    admission_no = "21JE0414"  

    print(f"🔮 Welcome to {name}'s Fortune Teller ({admission_no}) 🔮\n")
    mood = input("How are you feeling today? (happy/sad/neutral/stressed): ").strip().lower()

    fortunes = {
        "happy": [
            f"Great things await you, {name.split()[0]}! Keep smiling.",
            "Your joy is contagious. Keep spreading the positivity!",
            "Today will be as bright as your mood!"
        ],
        "sad": [
            "Every storm passes. Tomorrow will be brighter.",
            "Sadness is temporary, but strength is forever.",
            f"You’ve got this, {name.split()[0]}. Better days are ahead."
        ],
        "neutral": [
            "An unexpected surprise will lift your spirits today.",
            "Balance is beautiful. Embrace the calm.",
            "Stay steady, and something good will come your way."
        ],
        "stressed": [
            "Take a deep breath. Peace is just a moment away.",
            f"{name.split()[0]}, you are stronger than your stress.",
            "You’ve handled tough times before — and you'll do it again!"
        ]
    }

    if mood in fortunes:
        print(f"\n✨ Your fortune: {random.choice(fortunes[mood])} ✨")
    else:
        print("\n❌ Sorry, I can only predict for happy/sad/neutral/stressed moods.")

if __name__ == "__main__":
    main()
