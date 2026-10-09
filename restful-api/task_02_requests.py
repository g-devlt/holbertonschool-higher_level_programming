#!/usr/bin/env python3
"""
A module that provides functions
to fetch data from a RESTful API
"""
import requests
import csv


def fetch_and_print_posts():
    """
    Fetch posts from API and print their titles
    """

    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    print(f'Status Code: {response.status_code}')
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """
    Fetch posts from API and saves them 
    to a csv file named 'posts.csv'
    """

    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    #print(f'Status Code: {response.status_code}') 
    if response.status_code == 200:
        posts = response.json()
        with open('posts.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['id', 'title', 'body'])
            for post in posts:
                writer.writerow([post['id'], post['title'], post['body']])


if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
