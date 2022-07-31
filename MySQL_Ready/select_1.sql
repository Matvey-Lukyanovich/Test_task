SELECT bid.client_number, sum(event_value.outcome='win') AS "Побед",SUM(event_value.outcome='lose') AS "Порожение"
	FROM bid
		INNER JOIN event_value ON
			bid.play_id = event_value.play_id
		GROUP BY client_number