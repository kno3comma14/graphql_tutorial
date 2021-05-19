from api.models import Wallet

from ariadne import convert_kwargs_to_snake_case


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


@convert_kwargs_to_snake_case
def fetch_one_wallet(obj, info, wallet_id):
    try:
        wallet = Wallet.query.get(wallet_id)
        payload = {
            "success": True,
            "wallet": wallet.to_dict()
        }
    except AttributeError:
        payload = {
            "success": False,
            "errors": [f"Wallet item matching id {wallet_id} not found"]
        }

    return payload
        
