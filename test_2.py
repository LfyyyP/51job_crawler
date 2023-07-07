import urllib3
from urllib3.util.ssl_ import create_urllib3_context

ctx = create_urllib3_context()
ctx.load_default_certs()
ctx.options |= 0x4  # ssl.OP_LEGACY_SERVER_CONNECT

with urllib3.PoolManager(ssl_context=ctx) as http:
    r = http.request("GET", "https://www.51job.com/")
    print(r.status)
    data = r.data
    print(data)