def main():
        book_loc = "books/frankenstein.txt"
        with open(book_loc) as f:
            file_contents = f.read()
            words = file_contents.split()
            n_words = len(words)
            char_dict = {}
            for char in file_contents:
                if char.isalpha():
                    char_dict[char.lower()] = char_dict.get(char.lower(),0) + 1
            # print(char_dict)
            def sort_on(dict):
                return dict["num"]
            char_list = []
            for i in char_dict:
                char_list.append({"char": i, "num": char_dict[i]})
            # print(char_list)
            char_list.sort(reverse=True,key=sort_on)
            # print(char_list)
            print(f"--- Begin report of {book_loc} ---")
            print(f"{n_words} words found in the document\n")
            for char in char_list:
                print(f"the '{char['char']}' character was found {char['num']} times")
            print("--- End report ---")


main()
