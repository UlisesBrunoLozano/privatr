remera.get("color")
'rosa'

>>> remera.get("stock")
>>> remera.get("stock", "sin stock")
'sin stock'


existe = remera.has_key("precio")
>>> existe
False

>>> existe = remera.has_key("color")
>>> existe
True
