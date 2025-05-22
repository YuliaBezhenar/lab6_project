import requests

API_KEY = '95a864f1e03859996fdfd3b3e8c2ed73'

def get_movie_data(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        title = data.get('title', 'No Title')
        budget = data.get('budget', 0)
        revenue = data.get('revenue', 0)

        if budget > 0:
            ratio = revenue / budget
            print(f"{title} — Budget: ${budget}; \nRevenue: ${revenue}; \nRatio: {ratio:.2f}")
        else:
            print(f"{title} — No budget")
    else:
        print(f"Error: cannot get data from id {movie_id}. Code: {response.status_code}")

#950387, 299536, 822119
print("Enter ID:")
movie_id = input()

if movie_id.isdigit():
    get_movie_data(movie_id)
else: print("Please, enter a number")

