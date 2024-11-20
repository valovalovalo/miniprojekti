class UserInputError(Exception):
    pass

def validate_reference(content):
    
    """
    Tarkistaa, että syötteen pituus on hyväksyttävällä alueella (5-100 merkkiä).
    Heittää UserInputError-poikkeuksen, jos pituus on liian lyhyt tai pitkä.
    """
    
    if len(content) < 5:
        raise UserInputError("Todo content length must be greater than 4")

    if len(content) > 100:
          raise UserInputError("Todo content length must be smaller than 100")
