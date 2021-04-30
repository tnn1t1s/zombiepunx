# Background
This is an advanced NFT tutorial and implementation that uses machine learnning to create zombie versions of the original cryptopunks. The `CryptoZombies` contract will contain a Solidty implementation of the ML model that is used to mint new zombies entirely on chain. 

# On Chain v. Off Chain
THe original cryptopunx were very aware of the tradeoffs between offchain economics and artistic integrity. While they aspired to keep the information raito of each punk high, they were still limited by what could be stored on the blockchain. They did include a hash of the .png image of each crypto punk on the chain, which allows art collectors, historians and students to trust, to a fair extent, the relationship between the image and the blockchain collectible. 

This work aims to preserve the essence of each collectible on the blockchain by storing the model, the latent space essentially, and the model parameters of each zombie on the chain. WIth zombiepunx, the attributes assigned to each punk will be learned by a separate classification model, as opposed to assigned manually as in the original punks. These labels will be added to the collectible as meta data stored in IPFS as it is not computationally practical to classify on chain.



