#Empezamos
# Definimos la variable 'i'. Aunque en Python no es estrictamente necesario,
# por claridad con respecto a tu ejemplo original:
i = 1

# El bucle for en Python itera sobre un rango de números.
# range(1, 31) genera números desde 1 hasta 30 (sin incluir el 31).
for i in range(1, 31):
    print(f"HOLA {i}")
    a = 5

cryptoex/
├─ core/                 # Infraestructura (no negocio)
│  ├─ config.py          # Carga de credenciales, entornos
│  ├─ auth.py            # HmacSigner (firma)
│  ├─ rest.py            # RestClient (POST firmados)
│  ├─ ws.py              # UserWsClient (auth + subscripciones)
│  └─ errors.py          # Excepciones de la API
├─ domain/               # Modelo de dominio (puro)
│  ├─ account.py         # Account, BalanceSummary, AccountSettings, Subaccount
│  ├─ money.py           # Value objects: Amount, Currency
│  ├─ operations.py      # Op base + Withdraw, Transfer, Order, etc.
│  ├─ market.py          # Instrument, Ticker, Candle (si lo usas)
│  └─ enums.py           # Enumeraciones: Side, OrderType, Network, etc.
├─ services/             # Casos de uso (hablan con core.*)
│  ├─ account_service.py # leer saldos, settings, subcuentas
│  ├─ wallet_service.py  # depósitos/retiros cripto y fiat
│  ├─ trade_service.py   # órdenes, historial, posiciones
│  └─ stream_service.py  # canales WS de usuario (user.balance, user.order.*)
└─ app/
   ├─ cli.py             # CLI (ej: cryptoex account balance)
   └─ main.py            # ejemplo de uso programático
