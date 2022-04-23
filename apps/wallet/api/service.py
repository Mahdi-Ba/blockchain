from apps.wallet.api.repository import WalletRepository


class WalletService(WalletRepository):

    def getAddressInfo(self, request):
        link = "https://api.blockchair.com/{}/dashboards/address/{}".format(request.data['blockchain_type'],
                                                                            request.data['address'])
        return self.addressInfo(link)