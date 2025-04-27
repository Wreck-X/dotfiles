import hashlib
import json
import time
import requests

class Node:
    def __init__(self, node_id, peers):
        self.node_id = node_id
        self.peers = peers

        """ 
        Ledger for now but might have to switch to decentralised solutions not sure how yet.
        """ 
        self.news_db = []

    def validate_news(self,news):
        if isinstance(news, dict) and 'content' in news:
            return True
        return False