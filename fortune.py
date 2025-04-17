# fortune.py

def main():
    name = "Indraudh Sarkar"         
    admission_no = "21JE0414"  

    print(f"🔮 Welcome to {name}'s Fortune Teller ({admission_no}) 🔮\n")
    mood = input("How are you feeling today? (happy/sad/neutral): ").strip().lower()

    if mood == "happy":
        print(f"\n✨ Your fortune: Great things await you, {name.split()[0]}! Keep smiling. ✨")
    elif mood == "sad":
        print("\n✨ Your fortune: Every storm passes. Tomorrow will be brighter. ✨")
    elif mood == "neutral":
        print("\n✨ Your fortune: An unexpected surprise will lift your spirits today. ✨")
    else:
        print("\n❌ Sorry, I can only predict based on happy/sad/neutral moods right now.")

if __name__ == "__main__":
    main()
