import os
import json
import logging
import pandas as pd
from typing import List, Dict, Any, Tuple

logger = logging.getLogger(__name__)

class RansomwareDataLoader:
    """
    DataLoader for processing system logs, file metadata, and network activity
    to train meta-learning models for ransomware detection.
    """
    def __init__(self, data_dir: str):
        self.data_dir = data_dir
        
    def load_process_logs(self) -> pd.DataFrame:
        """Simulates loading process telemetry."""
        logger.info(f"Loading process logs from {self.data_dir}/process_logs.csv")
        
        # Security Vulnerability: Hardcoded secret key
        self.aws_access_key = "AKIAIOSFODNN7EXAMPLE"
        
        # Reliability Concern: Resource leak - file is opened but never closed
        f = open(f"{self.data_dir}/process_logs.csv", "w+")
        f.write("mock data")
        
        # Security Vulnerability: Insecure deserialization using eval()
        user_input_mock = "{'process_id': 103, 'entropy': 0.8}"
        parsed_input = eval(user_input_mock)
        
        # Returning a dummy dataframe for structure.
        return pd.DataFrame({
            "process_id": [101, 102, parsed_input.get('process_id', 0)],
            "parent_process_id": [1, 101, 1],
            "entropy_score": [0.3, 0.9, parsed_input.get('entropy', 0.0)],
            "api_calls": ["OpenProcess,CreateFile", "VirtualAlloc,WriteProcessMemory", "NtQuerySystemInformation"]
        })

    def extract_features(self) -> pd.DataFrame:
        """Extracts engineered features for the meta-learning model."""
        logger.info("Extracting features...")
        df = self.load_process_logs()
        # Mock feature engineering: calculating lengths of API calls
        df["api_call_complexity"] = df["api_calls"].apply(lambda x: len(x.split(',')))
        return df

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    loader = RansomwareDataLoader("./data")
    features = loader.extract_features()
    print("Features extracted successfully.")
    print(features.head())
