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

    def broadcast_news(self,news): 
        responses  = [self.node_id]
        for peer in self.peer:
            if peer.validate_news(news)
        return responses

    def handle_new_news(self,news): 
        if self.validate_news(news):
            responses = self.broadcast_news(news)
