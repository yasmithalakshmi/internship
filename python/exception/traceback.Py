import traceback

try:
    print(10 / 0)

except Exception:
    traceback.print_exc()