Benchmark
=========

* Ran on a Macbook Pro 2019 (2,6 GHz 6-Core Intel Core i7, 16 GB 2400 MHz DDR4)
* Published best of 5 runs.

# Simple text (aka helloworld)

* **Fastify** (Node.JS 12.5.0):
```shell
$ wrk -t12 -c400 -d30s http://localhost:3000
Running 30s test @ http://localhost:3000
  12 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    25.25ms   11.52ms 161.31ms   92.81%
    Req/Sec     1.32k   267.81     2.65k    81.69%
  473056 requests in 30.07s, 73.99MB read
  Socket errors: connect 0, read 250, write 0, timeout 0
Requests/sec:  15732.10
Transfer/sec:      2.46MB
```

* **FastAPI** (Python 3.7.4):
```shell
$ wrk -t12 -c400 -d30s http://localhost:8000
Running 30s test @ http://localhost:8000
  12 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    70.80ms   20.41ms 213.47ms   76.47%
    Req/Sec   283.43     89.52   660.00     68.11%
  101701 requests in 30.08s, 13.77MB read
  Socket errors: connect 0, read 82375, write 0, timeout 0
Requests/sec:   3381.53
Transfer/sec:    468.92KB
```

# Async delay (200ms)

* **Fastify** (Node.JS 12.5.0):
```shell
$ wrk -t12 -c400 -d30s http://localhost:3000
Running 30s test @ http://localhost:3000
  12 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   207.16ms    7.55ms 294.43ms   89.58%
    Req/Sec   156.57     77.20   330.00     57.86%
  56178 requests in 30.13s, 5.30MB read
  Socket errors: connect 0, read 273, write 0, timeout 0
Requests/sec:   1864.49
Transfer/sec:    180.26KB
```

* **FastAPI** (Python 3.7.4):
```shell
$ wrk -t12 -c400 -d30s http://localhost:8000
Running 30s test @ http://localhost:8000
  12 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   220.76ms   61.91ms 921.93ms   96.08%
    Req/Sec    91.13     53.54   250.00     65.27%
  31561 requests in 30.09s, 3.85MB read
  Socket errors: connect 39, read 24526, write 0, timeout 0
Requests/sec:   1048.85
Transfer/sec:    131.11KB
```

# External API invocation

* **Fastify** (Node.JS 12.5.0):
```shell
$ wrk -t2 -c40 -d30s http://localhost:3000
Running 30s test @ http://localhost:3000
  2 threads and 40 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   378.42ms   43.40ms   1.60s    92.05%
    Req/Sec    53.25     22.08   171.00     65.29%
  3165 requests in 30.07s, 1.02MB read
Requests/sec:    105.26
Transfer/sec:     34.64KB
```

* **FastAPI** (Python 3.7.4):
```shell
$ wrk -t2 -c40 -d30s http://localhost:8000
Running 30s test @ http://localhost:8000
  2 threads and 40 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency   515.50ms  120.40ms   1.90s    97.13%
    Req/Sec    40.03     18.99   150.00     68.78%
  2338 requests in 30.10s, 0.99MB read
Requests/sec:     77.66
Transfer/sec:     33.60KB
```