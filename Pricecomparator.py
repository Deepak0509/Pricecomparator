import requests
from bs4 import BeautifulSoup
from tkinter import *
import webbrowser
from PIL import ImageTk, Image

root = Tk()

root.title("Compare prices of any products")

Label1 = Label(root, text="Search for any product:")

SearchBar = Entry(root, width=60)

Label1.grid(column=1, row=1)
Label1.config(font=("san-serif", 20))
SearchBar.grid(column=1, row=2)

def Run():
    SearchItem = SearchBar.get()
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
    headers = {"user-agent" : USER_AGENT}

    #Amazon Search
    url_amazon = "https://www.amazon.in/s?k="+SearchItem
    respAmazon = requests.get(url_amazon, headers=headers)
    if respAmazon.status_code == 200:
        soupAmazon = BeautifulSoup(respAmazon.content, "html.parser")
    ProductAmazon = soupAmazon.find('a', class_='a-link-normal a-text-normal')
    if ProductAmazon :
        link_amazon = "https://www.amazon.in"+ProductAmazon.get('href')
    amazonName = ProductAmazon.find('span').get_text()
    amazonPrice = soupAmazon.find('span', class_='a-offscreen')

    # Flipcart Search
    searchItem = SearchBar.get()
    url_flipkart = "https://www.flipkart.com/search?q="+SearchItem
    respFlipkart = requests.get(url_flipkart, headers=headers)
    if respFlipkart.status_code == 200:
        soupFlipkart = BeautifulSoup(respFlipkart.content, "html.parser")
    link_flipkart = "https://www.flipkart.com"+soupFlipkart.find('a', target='_blank').get('href')
    response = requests.get(link_flipkart, headers=headers)
    if response.status_code == 200:
        linkSoup = BeautifulSoup(response.content, "html.parser")
    Name = linkSoup.find('h1').get_text()
    Price = linkSoup.find('div', class_='_1vC4OE _3qQ9m1').get_text()

    # Amazon Display
    AmazonLabel = Label(root, text="Product on Amazon", justify='center')
    AmazonNameLabel = Label(root, text=amazonName, wraplength=400, justify='center')
    AmazonPrizeLabel = Label(root, text="Price : "+amazonPrice.get_text(), justify='center')
    AmazonLabel.grid(column=1,row=4)
    AmazonNameLabel.grid(column=1, row=5)
    AmazonPrizeLabel.grid(column=1, row=6)
    def OpenAmazonLink():
        webbrowser.open(link_amazon)
    AmazonLinkButton = Button(root, text="View product", command=OpenAmazonLink, bg='blue', fg='white')
    AmazonLinkButton.grid(column=1, row=7)

    # Flipkart Display
    FlipkartLabel = Label(root, text="Product on Flipkart", justify='center')
    FlipkartNameLabel = Label(root, text=Name, wraplength=400, justify='center')
    FlipcartPriceLabel = Label(root, text="Price : "+Price, justify='center')
    FlipkartLabel.grid(column=1, row=8)
    FlipkartNameLabel.grid(column=1, row=9)
    FlipcartPriceLabel.grid(column=1, row=10)
    def OpenFlipkartLink():
        webbrowser.open(link_flipkart)
    FlipcartLinkButton = Button(root, text="View product", command=OpenFlipkartLink, bg='blue', fg='white')
    FlipcartLinkButton.grid(column=1, row=11)

    MyButton.grid_forget()
    exitButton = Button(root, text="Exit", command=root.quit, padx=20, bg='#333', fg='white')
    exitButton.grid(column=1, row=15)


# Search
MyButton = Button(root, text="Compare",  command=Run, bg='#333', fg='white')
MyButton.config(font=(15))
MyButton.grid(column=1, row=3)


root.mainloop()
