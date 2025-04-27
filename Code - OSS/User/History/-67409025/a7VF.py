import hashlib
import json
import time
import requests

# Simple Node class
class Node:
    def __init__(self, node_id, peers):
        self.node_id = node_id
        self.peers = peers
        self.news_db = []  # Ledger to store validated news

    def validate_news(self, news):
        """Simulate news validation by checking its content."""
        if isinstance(news, dict) and 'content' in news:
            return True
        return False

    def broadcast_news(self, news):
        """Broadcast the news to peers and get their consensus."""
        responses = [self.node_id]
        for peer in self.peers:
            if peer.validate_news(news):
                responses.append(peer.node_id)
        return responses

    def handle_new_news(self, news):
        """Handle new news and check if it has reached consensus."""
        if self.validate_news(news):
            responses = self.broadcast_news(news)
            if len(responses) >= len(self.peers) / 2 + 1:
                print(f"News '{news['content']}' validated by {len(responses)} nodes!")
                self.news_db.append(news)
            else:
                print("News did not achieve consensus.")
        else:
            print("Invalid news.")

# Set up the nodes
node1 = Node(node_id=1, peers=[])
node2 = Node(node_id=2, peers=[node1])
node3 = Node(node_id=3, peers=[node1, node2])

# Add peers to each node
node1.peers = [node2, node3]

# Sample news
news = {
    'id': hashlib.sha256(str(time.time()).encode()).hexdigest(),
    'content': 'New scientific discovery announced!',
    'timestamp': time.time()
}

# Node 1 receives the news and tries to validate it
node1.handle_new_news(news)
