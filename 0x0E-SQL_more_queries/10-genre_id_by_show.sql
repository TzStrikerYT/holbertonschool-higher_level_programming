-- ID by show
SELECT tv_shows_genres.title, tv_show_genres.gere.id FROM tv_shows
JOIN tv_shows_genres ON tv_show_genres.show_id = tv_shows.id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
