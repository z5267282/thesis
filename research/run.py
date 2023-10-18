from subprocess import run

with open("temp", "w") as f:
    print("fishing", file=f)
    run(["dash", "read-write.sh"])
