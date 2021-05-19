from ariadne import convert_kwargs_to_snake_case

from api import db
from api.models import Wallet, CurrencyUnit, Coin


@convert_kwargs_to_snake_case
def create_wallet(obj, info, name, currency, coins):
    try:
        wallet = Wallet()
        wallet.name = name
        wallet.currency = currency
        for coin in coins:
            aux_coin = Coin.query.get(coin)
            wallet.coins.append(aux_coin)
        db.session.add(wallet)
        db.session.commit()
        payload = {
            'success': True,
            'wallet': wallet.to_dict()
        }
    except ValueError as value_error:
        payload = {
            'success': False,
            'errors': [str(value_error)]
        }

    return payload

@convert_kwargs_to_snake_case
def delete_wallet(obj, info, wallet_id):
    try:
        wallet = Wallet.query.get(wallet_id)
        db.session.delete(wallet)
        db.session.commit()
        payload = {
            'success': True
        }
    except Exception as error:
        payload = {
            'success': False,
            'errors': [str(error)] 
        }

    return payload

@convert_kwargs_to_snake_case
def add_coin_to_wallet(obj, info, wallet_id, coin_id):
    # search for a wallet with the given wallet_id
    #
    try:
        wallet = Wallet.query.get(wallet_id)
        coins = [coin.coin_id for coin in wallet.coins.all()]
        if not coin_id in coins:
            coin = Coin.query.get(coin_id)
            wallet.coins.append(coin)
            db.session.add(wallet)
            db.session.commit()
        payload = {
            'success': True,
            'wallet': wallet.to_dict()
        }
    except Exception as error:
        payload = {
            'success': False,
            'errors': [str(error)]
        }

    return payload


