import requests


class WalletRepository:
    def addressInfo(self, link):
        return requests.get(link).json()
