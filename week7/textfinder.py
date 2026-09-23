import re

print('''enter the text below that you want to search''')

while True:
    val=re.compile(input('\n>>'),re.IGNORECASE)
    fin=r'''qpwokfmpqwe90u23r-0sdjcmkld
    fjranveer!@#$!@#f90wejfp90s
    djc-023i4-0fksdlcmxlkcvjoiwej
    r9023u4r0jsdlfkcvjlxzkcjv09weur
    90234u-0jsdklfmcxklzjvweuir092
    3u4-0jsdklfcvmxzkljcvoiwer90u2
    3-049iusdflkmcxvjwe09riwerjMarlina!@#)(*!@#&*(\%^#$!@#sdlk
    fmpweoiru90234i
    -0sdkflmcvxkjwoeir09u23-049usd
    kflmcvxkjwe09ri2340-9sdklf
    mxcvjwe09ri23-094iusdfklmxvc
    kjw09erij23-094iusdflkmxcvjwe
    09ri234-09isdflmxcvkw09eirj23
    -094idfsklmxvckjw09eijr23-

    lkjxcwe09r-23490sdflkxcjw09er
    -23490sdflkxcjw09er-23490sdf
    lkxjcwe09r-23490sdfkljxcwe09
    -r23409sdfkljxcwe09r-23409sd
    fkljxcwe09r-23409sdfkljxcwe0
    9r-23409sdfkljxcwe09r-23409s
    dfkljxcwe09r-23409sdfkljxcwe
    09r-23409sdfkljxcwe09r-23409s
    dfkljxcwe09r-23409sdfkljxcwe0
    9r-23409sdfkljxcwe09r-23409sd
    fkljxcwe09r-23409sdfkljxcwe09
    r-23409sdfkljxcwe09r-23409sdf
    kljxcwe09r-23409sdfkljxcwe09r
    -23409sdfkljxcwe09r-23409sdfk
    ljxcwe09r-23409sdfkljxcwe09r-
    -23409sdfkljxcwe09r-23409sdfkl
    jxcwe09r-23409sdfkljxcwe09r-23
    409sdfkljxcwe09r-23409sdf
    kljxcwe09r-23409sdfkljxcwe09r
    -23409sdfkljxcwe09r-23409sdfklj
    xcwe09r-23409sdfkljxcwe09r-234
    09sdfkljxcwe09r-23409sdfkljxcwe
    09r-23409sdfkljxcwe09r-23409sdf
    kljxcwe09r-23409sdfkljxcwe09r-2
    3409sdfkljxcwe09r-23409sdfkljxcw
    e09r-23409sdfkljxcwe09r-23409sdf
    kljxcwe09r-23409sdfkljxcwe09r-23
    409sdfkljxcwe09r-23409sdfkljxcwe
    09r-23409sdfkljxcwe09r-23409sdfk
    ljxcwe09r-23409sdfkljxcwe09r-234
    09sdfkljxcwe09r-23409sdfkljxcwe0
    9r-23409sdfkljxcwe09r-23409sdfkl
    jxcwe09r-23409sdfkljxcwe09r-2340
    9sdfkljxcwe09r-23409sdfkljxcwe09
    r-23409sdfkljxcwe09r-23409sdf
    kljxcwe09r-23409sdfkljxcwe09
    r-23409sdfkljxcwe09r-23409sdfk
    ljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfk
    ljxcwe09r-23409sdfkljxcwe09
    r-23409sdfkljxcwe09r-23409sdfk
    ljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfkljxcwe09r-23409sdfk
    ljxcwe09r-23409sdfkljxcwe
    09r-23409sdfkljxcwe09r-23409sd
    fkljxcwe09r-23409sdfkljxcwe09r-
    23409sdfkljxcwe09r-23409sdfkljx
    cwe09r-2ranveer3409sdfkljxcwe09r-23409
    sdfkljxcwe09r-'''

    for i in val.finditer(fin):
        print(i.group(), i.span())
