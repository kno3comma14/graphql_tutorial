from api.models import Wallet


def fetch_wallets(obj, info):
    try:
        wallets = [wallet.to_dict() for wallet in Wallet.query.all()]
        payload = {
            "success": True,
            "wallets": wallets
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload
