_nomi = None 

def zip_to_latlng(zip_code):
    global _nomi
    try:
        if _nomi is None:
            import pgeocode

            _nomi = pgeocode.Nominatim("us")
        result = _nomi.query_postal_code(str(zip_code).strip())
    except Exception as error:
        print(f"[geo] zip lookup failed for '{zip_code}': {error}")
        return None, None

    if result is None:
        return None, None

    import math

    if math.isnan(result.latitude):
        return None, None

    return result.latitude, result.longitude