from service.blog import create_post, view_all_posts, view_post_by_title, search_posts_by_tag
from colorama import Fore, Style, init

init(autoreset=True)  # Automatically reset colors after each print

def main():
    while True:
        print(Fore.CYAN + "\n" + "=" * 40)
        print(Fore.MAGENTA + "         📚 Welcome to Blog CLI App 📚")
        print(Fore.CYAN + "=" * 40)

        print(Fore.GREEN + "1. ✏️  Create a New Post")
        print(Fore.YELLOW + "2. 📄 View All Posts")
        print(Fore.BLUE + "3. 🔍 View Post by Title")
        print(Fore.MAGENTA + "4. 🏷️  Search Posts by Tag")
        print(Fore.RED + "5. 🚪 Exit")

        choice = input(Fore.CYAN + "\nEnter your choice (1-5): ").strip()
        print(f"{Fore.WHITE}DEBUG: You entered '{choice}'")

        if choice == "1":
            title = input(Fore.CYAN + "\nEnter Post Title: ")
            content = input(Fore.CYAN + "Enter Post Content: ")
            tags = input(Fore.CYAN + "Enter Tags (comma-separated): ")
            create_post(title, content, tags)

        elif choice == "2":
            view_all_posts()

        elif choice == "3":
            title = input(Fore.CYAN + "\nEnter the title of the post to view: ")
            view_post_by_title(title)

        elif choice == "4":
            tag = input(Fore.CYAN + "\nEnter Tag name to search: ")
            search_posts_by_tag(tag)

        elif choice == "5":
            print(Fore.GREEN + "\n👋 Thank you for using the Blog CLI App. Goodbye!")
            break

        else:
            print(Fore.RED + "\n❌ Invalid choice. Please try again!")

if __name__ == "__main__":
    main()
