-- My genres :D
SELECT g.name FROM tv_genres gen, tv_show_genres tv, tv_shows sws WHERE gen.id = tv.genre_id
       	      	   	     	  		     	      	  	AND tv.show_id = sws.id
									AND sws.title = "Dexter"
ORDER BY gen.name ASC;
