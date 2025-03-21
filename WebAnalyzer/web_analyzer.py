import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

url = "https://en.wikipedia.org/wiki/University_of_Calgary"
try:

    response = requests.get(url)
    response.raise_for_status() # Ensures the request was successful
    soup = BeautifulSoup(response.text, 'html.parser')

    print(f"Successfully fetched content from {url}\n")

    # 3. Data Analysis
    h1 = 0
    h2 = 0
    h3 = 0
    h4 = 0
    h5 = 0
    h6 = 0
    links = 0
    paragraphs = 0

    # For each tag, check if it is a header tag, link, or paragraph
    for tag in soup.find_all(True):
        if(tag.name == 'h1'):
            h1 += 1
        elif(tag.name == 'h2'):
            h2 += 1
        elif(tag.name == 'h3'):
            h3 += 1
        elif(tag.name == 'h4'):
            h4 += 1
        elif(tag.name == 'h5'):
            h5 += 1
        elif(tag.name == 'h6'):
            h6 += 1
        elif(tag.name == 'a'):
            links += 1
        elif(tag.name == 'p'):
            paragraphs += 1

    print("Question 3: Data Analysis")
    print(20 * '-')
    print(f"Number of h1 tags: {h1}")
    print(f"Number of h2 tags: {h2}")
    print(f"Number of h3 tags: {h3}")
    print(f"Number of h4 tags: {h4}")
    print(f"Number of h5 tags: {h5}")
    print(f"Number of h6 tags: {h6}")
    print(f"Number of links: {links}")
    print(f"Number of paragraphs: {paragraphs}\n")

    # 4. Keywords Analysis
    print("Question 4: Keywords Analysis")
    print(20 * '-')
    user_input = input("Enter a keyword to search for: ").lower()
    
    # Get the individual words on the page.
    webpage_text = soup.get_text().lower()
    individual_words = webpage_text.split()

    # See how many times that word appears in the page content.
    keyword_count = individual_words.count(user_input)
    print(f"'{user_input}' appears {keyword_count} times in the page content\n")

    # 5. Word Frequency Analysis
    print("Question 5: Links Analysis")
    print(20 * '-')

    # Create a frequency table for the words
    frequency_table = {}

    # Count the frequency of each word
    for word in individual_words:
        if(frequency_table.get(word) == None):
            frequency_table[word] = 1
        else:
            frequency_table[word] += 1
    
    # Display the top 5 most frequent words
    print("Top 5 most frequent words:")
    for i in range(5):
        most_frequent_word = max(frequency_table, key=frequency_table.get)
        print(f"{most_frequent_word}: {frequency_table[most_frequent_word]}")
        del frequency_table[most_frequent_word]

    # 6. Finding the Longest Paragraph
    print("\nQuestion 6: Finding the Longest Paragraph")
    print(20 * '-')

    # Get all paragraphs (tag <p>)
    all_paragraphs = soup.find_all('p')
    
    # Get the longest paragraph
    longest_paragraph = max(all_paragraphs, key=lambda x: len(x.text))
    
    print(f"Longest paragraph:\n {longest_paragraph.text}\n")
    print(f"Word Count: {len(longest_paragraph.text.split())}")

    # 7. Visualizing Results
    print("\nQuestion 7: Visualizing Results")
    print(20 * '-')

    labels = ['Headings', 'Links', 'Paragraphs']
    values = [(h1+h2+h3+h4+h5+h6), links, paragraphs]
    plt.bar(labels, values)
    plt.title('Group 15 Web Analyzer Results for UofC Wikipedia Page')
    plt.ylabel('Count')
    plt.show()

except Exception as e:
    print(f"Error fetching content: {e}")