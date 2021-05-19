# Queries
This represent a list of sample queries to test the project(Review schema.graphql file)

### Fetch all wallets
```
query fetchAllWallets {
  wallets {
    success
    errors
    wallets {      
      id
      name
      currency
      coins {
        name
        description
        price
      }
    }
  }
}
```

### Fetch one wallet
```
query fetchOneWallet {
  wallet(walletId:<walllet_id>) {
    success
    errors
    wallet {      
      id
      name
      currency
      coins {
        name
        description
        price
      }
    }
  }
}
```

### Create a wallet
```
mutation createOneWallet {
  createWallet(name: <wallet_name>, currency:<wallet_currency>, coins:[<coin ids>]) {
    success
    errors
    wallet {      
      id
      name
      currency
      coins {
        name
        description
        price
      }
    }
  }
}
```

### Delete a wallet
```
mutation deleteOneWallet {
  deleteWallet(walletId: <wallet_id>) {
    success
    errors    
  }
}
```
### Add a new coin to a wallet
```
mutation addNewCoin {
  addNewCoinToWallet(walletId: 1, coinId: 3) {
    success
    errors    
    wallet {
      name
      currency
      coins {
        name
        description
        price
      }
    } 
  }
}
```
