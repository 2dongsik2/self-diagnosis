import os
with open("private.pem", "wb") as file:
  file.write(os.environ["PRIVATE_KEY"].encode("utf8"))
