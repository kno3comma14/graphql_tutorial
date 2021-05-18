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
