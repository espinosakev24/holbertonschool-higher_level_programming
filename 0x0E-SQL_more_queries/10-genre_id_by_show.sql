-- Script that lists all shows contained in hbtn_0d_tvshows 
-- Only those that have at least one genre linked.
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows, tv_show_genres where tv_shows.id = tv_show_genres.show_id;
