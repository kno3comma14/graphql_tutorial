from main import db


coins_wallets_association = db.Table(
    'coins_wallets',
    db.Column('coin_id', db.Integer, db.ForeignKey('coin.coin_id')),
    db.Column('wallet_id', db.Integer, db.ForeignKey('wallet.wallet_id')))


class Coin(db.Model):
    coin_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(150), nullable=False)
    name = db.Column(db.String(50), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    wallets = db.relationship(
        'Wallet',
        secondary=coins_wallets_association,
        backref=db.backref('coins', lazy='dynamic'))

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "name": self.name,
            "price": self.price
        }


class Wallet(db.Model):
    wallet_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "coins": self.coins
        }
