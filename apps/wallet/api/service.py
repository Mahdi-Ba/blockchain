from apps.wallet.api.repository import WalletRepository


class WalletService(WalletRepository):

    def getAddressInfo(self, request):
        link = "https://api.blockchair.com/{}/dashboards/address/{}".format(request.data['blockchain_type'],
                                                                            request.data['address'])
        return self.addressInfo(link)

    def getTransactionInfo(self, request):
        link = "https://api.blockchair.com/{}/dashboards/transaction/{}".format(request.data['blockchain_type'],
                                                                            request.data['transaction_hash'])
        return self.transactionInfo(link)
