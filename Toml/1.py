import tomllib as tl
f1=open("1.toml","rb")
data=tl.load(f1)
print(data["age"])
