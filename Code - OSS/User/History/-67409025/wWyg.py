import hashlib
import json
import time
import requests

class Node:
    def __init__(self, node_id, peers):
        self.node_id = node_id
        self.peers = peers
        self.news_db = []