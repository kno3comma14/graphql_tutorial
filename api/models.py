from api import db
import enum


coins_wallets_association = db.Table(
    'coins_wallets',
    db.Column('coin_id', db.Integer, db.ForeignKey('coin.coin_id')),
    db.Column('wallet_id', db.Integer, db.ForeignKey('wallet.wallet_id')))


class CurrencyUnit(enum.Enum):
    USD = 1
    PEN = 2
    EUR = 3


class Coin(db.Model):
    coin_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(150), nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)    
    price = db.Column(db.Float, nullable=False)
    wallets = db.relationship(
        'Wallet',
        secondary=coins_wallets_association,
        backref=db.backref('coins', lazy='dynamic'))

    def to_dict(self, currency):
        return {
            "id": self.coin_id,
            "description": self.description,
            "name": self.name,
            "price": self.__convert_coin(currency)
        }

    def __convert_coin(self, currency):
        if currency == CurrencyUnit.USD:
            return self.price
        elif currency == CurrencyUnit.PEN:
            return self.price * 3.0
        elif currency == CurrencyUnit.EUR:
            return self.price * 0.8


class Wallet(db.Model):
    wallet_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    currency = db.Column(db.Enum(CurrencyUnit), nullable=False)

    def to_dict(self):
        return {
            "id": self.wallet_id,
            "name": self.name,
            "currency": self.__assign_correct_currency(),
            "coins": [coin.to_dict(self.currency) for coin in self.coins]
        }

    def __assign_correct_currency(self):
        if self.currency == CurrencyUnit.USD:
            return "USD"
        elif self.currency == CurrencyUnit.PEN:
            return "PEN"
        elif self.currency == CurrencyUnit.EUR:
            return "EUR"
