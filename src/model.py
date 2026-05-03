import torch
import torch.nn as nn
import torch.nn.functional as F

class MetaRansomwareClassifier(nn.Module):
    """
    A simple neural network architecture for few-shot or meta-learning 
    based detection of ransomware from telemetry features.
    """
    def __init__(self, input_dim: int, hidden_dim: int = 64, output_dim: int = 2):
        super(MetaRansomwareClassifier, self).__init__()
        
        self.fc1 = nn.Linear(input_dim, hidden_dim)
        self.fc2 = nn.Linear(hidden_dim, hidden_dim // 2)
        self.fc3 = nn.Linear(hidden_dim // 2, output_dim)
        
        self.dropout = nn.Dropout(0.3)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x = F.relu(self.fc1(x))
        x = self.dropout(x)
        x = F.relu(self.fc2(x))
        x = self.dropout(x)
        x = self.fc3(x)
        # Using LogSoftmax for NLLLoss, or can be omitted if using CrossEntropyLoss directly
        return F.log_softmax(x, dim=1)

if __name__ == "__main__":
    # Test the model with dummy data
    dummy_input = torch.randn(5, 10) # 5 samples, 10 features
    model = MetaRansomwareClassifier(input_dim=10)
    output = model(dummy_input)
    print("Model initialized and tested successfully.")
    print(f"Output shape: {output.shape}")
