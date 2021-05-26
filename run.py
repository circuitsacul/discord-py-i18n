import os

from dotenv import load_dotenv

load_dotenv()


def get_all_langs():
    dirs = []
    for _, dirs, _ in os.walk("./locale"):
        break
    return dirs


def launch_bot():
    gen_mo()

    from app.bot import Bot
    bot = Bot()
    try:
        bot.run(os.getenv("TOKEN"))
    finally:
        pass


def create_language():
    language_name = input("What language do you want to add?\n>")
    if language_name in get_all_langs() + ["en_US"]:
        print("That is already a language!")
    os.system(f"python3 generate_po.py {language_name}")
    gen_mo()


def update_languages():
    for lang in get_all_langs():
        os.system(f"python3 generate_po.py {lang}")
    gen_mo()


def gen_mo():
    os.system("python3 generate_mo.py")


def menu():
    print(
        "Welcome to Circuit#5585's discord i18n example!\n"
        "Please choose an option:\n"
        "0. Quit the menu.\n"
        "1. Launch the bot.\n"
        "2. Create a new language.\n"
        "3. Update languages."
    )
    choice = input(">")
    if choice == "0":
        return False
    elif choice == "1":
        launch_bot()
    elif choice == "2":
        create_language()
    elif choice == "3":
        update_languages()
    else:
        print("Invalid choice.")
    return True


if __name__ == "__main__":
    running = True
    while running:
        running = menu()
