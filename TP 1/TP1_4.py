movies_ranking = {
    "The Long Braids of the Bald": 9.5,
    "Dust in the High Seas": 9.25,
    "Oppenheimer": 3.2,
    "Barbie": 7.1,
    "The Return of Those Won't Go": 9.75,
    "Kill Bill": 2.4
}

highest_rated_movies = {
    movie: rating for movie, rating in movies_ranking.items() if rating > 7
}

print(highest_rated_movies)