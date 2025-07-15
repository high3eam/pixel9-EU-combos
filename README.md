## [Check Releases for Magisk modules](https://github.com/high3eam/pixel9-EU-combos/releases)
### Module includes a built-in updater
## Edit combos yourself (or even better, use the binarypb editor here: [https://nxij.github.io/pixel-pb/](https://nxij.github.io/pixel-pb/), thanks to [@NXij](https://github.com/NXij))
- Download [`protoc`](https://github.com/protocolbuffers/protobuf/releases) as well as the ShannonUeCap `.proto template` files from this repo.
- Then use protoc to decode the protobuf binary file.
For NR combos, use:
```sh
protoc --decode=ShannonNrUECap ShannonNrUeCap.proto < PLATFORM_11376227466629817631.binarypb > decoded.txt
```
For LTE combos, use:
```sh
protoc --decode=ShannonLteUECap ShannonLteUeCap.proto < lte_2160127815.binarypb > decoded.txt
```
Then, edit, add or delete combos as you like.

After that, recompile to protobuf binary.

For NR combos, use:
```sh
protoc --encode=ShannonNrUECap ShannonNrUeCap.proto < decoded.txt > PLATFORM_11376227466629817631.binarypb
```
For LTE combos, use:
```sh
protoc --encode=ShannonLteUECap ShannonLteUeCap.proto < decoded.txt > lte_2160127815.binarypb
```
