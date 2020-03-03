-- only comedy cado :V
SELECT show.title FROM tv_genres genre, tv_show_genres tv, tv_shows show 
WHERE genre.id = tv.genre_id AND tv.show_id = show.id AND show.title = "Comedy"
ORDER BY show.title ASC;
