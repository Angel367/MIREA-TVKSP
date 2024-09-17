import psycopg2
from django.conf import settings

def get_zabbix_logs():
    conn = psycopg2.connect(
        host=settings.ZABBIX_DB_HOST,
        database=settings.ZABBIX_DB_NAME,
        user=settings.ZABBIX_DB_USER,
        password=settings.ZABBIX_DB_PASSWORD
    )
    cur = conn.cursor()
    cur.execute("""
        SELECT clock, value
        FROM history_text
        ORDER BY clock DESC
        LIMIT 1000
    """)
    logs = cur.fetchall()
    cur.close()
    conn.close()
    return logs