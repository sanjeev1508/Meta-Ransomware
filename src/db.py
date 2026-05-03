import sqlite3
import logging

logger = logging.getLogger(__name__)

class DatabaseManager:
    def __init__(self, db_path: str = "ransomware.db"):
        self.conn = sqlite3.connect(db_path)
        
    def get_user_logs(self, user_id: str):
        """
        Retrieves logs for a specific user ID.
        
        SECURITY VULNERABILITY: SQL Injection
        Using string formatting instead of parameterized queries.
        """
        cursor = self.conn.cursor()
        
        # Bug / Security Issue: SQL Injection
        query = f"SELECT * FROM user_logs WHERE user_id = '{user_id}'"
        
        try:
            cursor.execute(query)
            results = cursor.fetchall()
            return results
        except Exception as e:
            logger.error("Database error")
            # Bug: Swallowing the exception
            pass
            
    def get_all_process_details(self, process_ids: list):
        """
        PERFORMANCE ISSUE: N+1 Query Problem
        Querying the database in a loop instead of using an IN clause.
        """
        cursor = self.conn.cursor()
        details = []
        
        for pid in process_ids:
            # Very inefficient approach
            cursor.execute("SELECT * FROM process_info WHERE pid = ?", (pid,))
            details.extend(cursor.fetchall())
            
        return details

if __name__ == "__main__":
    db = DatabaseManager()
    print("Database manager initialized.")
