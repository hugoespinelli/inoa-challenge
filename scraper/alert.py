from database import get_connection

STOCK_ALERT_QUERY = f"""
SELECT
	u.email as user_email,
	tbl_alert.code as stock,
	tbl_alert.price,
    tbl_alert.`type` as action
FROM
	(
	SELECT
		aus.id_user,
		srv.code,
		srv.price,
        aus.`type`,
		CASE WHEN type = 'vender'
		AND srv.price > aus.price_alert THEN true
		WHEN type = 'comprar'
		AND srv.price < aus.price_alert THEN true
		ELSE false END as should_alert
	FROM
		alert_user_stocks aus
	JOIN stock_realtime_vw as srv ON
		srv.id = aus.id ) as tbl_alert
JOIN user as u ON
	u.id = tbl_alert.id_user
WHERE
	tbl_alert.should_alert = true;
"""


def get_stock_alerts(cursor):
    cursor.execute(STOCK_ALERT_QUERY)
    return list(cursor)


def search_stock_alerts():

    # Connect to the database
	connection = get_connection()
	with connection:
		with connection.cursor() as cursor:
			try:
				return get_stock_alerts(cursor)
			except Exception as e:
				Exception(f"Failure on search alerts. {e}")
