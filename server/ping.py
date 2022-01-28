from aiohttp.client_exceptions import ClientConnectorCertificateError, ClientConnectorError, InvalidURL


# Outputs
async def ping_url(url, session):
    try:
        async with session.get(url) as resp:
            return {"message": resp.status}
# Handling Errors
    except ClientConnectorCertificateError:
        return {"error": "SSLError"}
    except InvalidURL:
        return {"error": "InvalidURL"}
    except ClientConnectorError:
        return {"error": "ClientConnectorError"}
    except TypeError:
        return {"error": "NoInput"}
