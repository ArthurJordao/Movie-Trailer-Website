from media import Movie
import fresh_tomatoes


def main():
    interstellar = Movie("Interstellar", "A science fiction film about space travalling",
                         "https://upload.wikimedia.org/wikipedia/en/thumb/b/bc/Interstellar_film_poster.jpg/220px-Interstellar_film_poster.jpg", "https://www.youtube.com/watch?v=zSWdZVtXT7E")
    divergent = Movie("Divergent", "A filme about a future society",
                      "https://upload.wikimedia.org/wikipedia/en/d/d4/Divergent.jpg", "https://www.youtube.com/watch?v=sutgWjz10sM")
    maze_runner = Movie("The Maze Runner", "A filme about a society that lives in a maze",
                        "https://upload.wikimedia.org/wikipedia/en/b/be/The_Maze_Runner_poster.jpg", "https://www.youtube.com/watch?v=AwwbhhjQ9Xk")

    movies = [interstellar, divergent, maze_runner]
    fresh_tomatoes.open_movies_page(movies)

if __name__ == "__main__":
    main()
