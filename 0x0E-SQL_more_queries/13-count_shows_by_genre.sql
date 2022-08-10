-- List all genres from 'hbtn_0d_tvshows' and display number of shows linked to each
-- Each record should display tv_genres.name, number of shows
-- Don't display a genre that doesn't have any shows linked
-- Results must be sorted descending order by number of shows linked
-- Can only use one SELECT statement
SELECT gr.name AS genre,
       COUNT(shgr.genre_id) AS number_of_shows FROM tv_genres AS gr
       JOIN tv_show_genres AS shgr
       ON gr.id=shgr.genre_id
       GROUP BY shgr.genre_id
       ORDER BY number_of_shows DESC;