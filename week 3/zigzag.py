import time, sys
indent = 0
indenting = True
try:
    while True:
        print(' '*indent,end='')
        print('*+*+*+*+*')
        time.sleep(0.1)
        if indenting:
            indent = 1 +indent
            if indent == 5:
                indenting = False

        else:
            indent = indent - 1
            if indent == 0:
                indenting = True

except KeyboardInterrupt:
    sys.exit()
