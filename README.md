# mbenchpy - a tiny command timer


`mbenchpy` is a simple command line timer written in Python. It's goal is to
be similar to R's [microbenchmark
package](http://cran.r-project.org/web/packages/microbenchmark/index.html). It
can do things like:

    $ mbench.py -n 20 grep='grep AGATGCATG maiza.fa' \
                      awk="awk '/AGATGCATG/' maize.fa" \
                      sed="sed -n /AGATGCATG/p  maize.fa" | column -t
    command  min       lq        median    up        max       mean
    grep     2.65371   2.65372   2.65372   2.65373   2.67171   2.66002
    sed      21.02044  21.02154  21.02265  21.02376  21.76965  21.34398
    awk      14.76936  14.77334  14.77732  14.78129  20.71750  17.01729

`mbenchpy` is still quite rough around the edges; send me a pull request!

## Todo

- Pretty print columns (so we don't have to use `column -t`).
- Make quoting safer.
- Tabular output to file, graphics creation (should be separate script).
- Report times in units of fastest.
- Add user time, wall clock time, % CPU use, pages, page faults.
- Remove first iteration (since this is before disk caching).
