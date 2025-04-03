from stats import count_words, count_charackters, number_report
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    

def main():
    try:
        if sys.argv:
            file_path = sys.argv[1]
            text = get_book_text(file_path)
            num_words = count_words(text)
            counts_of_letters = count_charackters(text)
            report = number_report(counts_of_letters)
            

            print(f"""============ BOOKBOT ============"
            Analyzing book found at {file_path}...")
            ----------- Word Count ----------
            Found {num_words} total words
            --------- Character Count -------""")
            for i in report:
                if str(i["letter"]).isalpha():
                    output_1 = f"{i["letter"]}: {i["value"]}"
                    print(output_1)
            print("============= END ===============")
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)




        


main()