language_1 = input("Enter your first favourite programming language: ")
language_2 = input("Enter your second favourite programming language: ")
language_3 = input("Enter your third favourite programming language: ")
favourite_languages = [language_1, language_2, language_3]
extra = input("Enter new language: ")
favourite_languages.append(extra)
remove_language = input("Enter the language to be removed: ")
favourite_languages.remove(remove_language)
print(favourite_languages)

