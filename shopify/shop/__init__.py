import os

from shopify.shop import interface


shops = {
    i.shop_url: i
    for i in [
        interface.Shop(
            "KurioKits",
            "kuriookits",
            os.getenv("KURIO_KITS_TOKEN", ""),
        ),
    ]
}
