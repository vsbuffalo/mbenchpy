# mbenchpy - a tiny command timer written in Python

`mbenchpy` is a simple command line timer written in Python. It's goal is to
be similar to R's [microbench
package](http://cran.r-project.org/web/packages/microbenchmark/index.html). It
can do things like:

    python benchmark.py -n 10 grep='grep AGATGCATG maiza.fa' \
                              awk="awk '/AGATGCATG/' maize.fa" \
                              sed="sed -n /AGATGCATG/p  maize.fa" | column -t
    command  min       lq        median    up        max       mean
    grep     0.00627   0.00628   0.00628   0.00628   0.00688   0.00661
    sed      35.54765  35.54818  35.54870  35.54922  36.66781  35.95596
    awk      14.18893  14.18996  14.19099  14.19202  14.41605  14.33322

`mbenchpy` is still quite rough around the edges; send me a pull request!

## Todo

- Pretty print columns (so we don't have to use `column -t`.
- Make quoting safer.
- Tabular output to file, graphics creation (should be separate script).
- Report times in units of fastest.
