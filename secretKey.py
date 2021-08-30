import os
with open("public.pem", "wb") as file:
  file.write(os.environ["PUBLIC_KEY"].encode("utf8"))