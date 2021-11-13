# pi-433
simple python program that sends codes to brennstuhl 433mhz power plugs. The programm is controlled via an Restful API.

## Installation
```
sudo ./install.sh
```

## Restful API
### `IP:5000/{A,B,C,D}` - GET
returns the current state.
```
{ "state":"1" } # ON
{ "state":"0" } # OFF
```

### `IP:5000/{A,B,C,D}` - POST
sets the new state with the following body:
```
{ "state":"1" } # ON
{ "state":"0" } # OFF
```

## 433Mhz codes
| # | on | off |
|---|---|---|
| A | 1361 | 1364 |
| B | 4433 | 4436 |
| C | 5201 | 5204 |
| D | 5393 | 5396 |