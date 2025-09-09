#!/usr/bin/env python3
# main.py
import argparse
import sys
import traceback

import request  # ใช้ request.py ของคุณ (มี fetch_headers(url))


def parse_args(argv=None):
    p = argparse.ArgumentParser(
        description="Scan URLs and print HTTP response headers (sequential)."
    )
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--url", help="Single URL to scan")
    src.add_argument("--url-file", help="Path to a file with one URL per line")
    return p.parse_args(argv)


def iter_targets(args):
    if args.url:
        u = args.url.strip()
        if u:
            yield u
        return
    with open(args.url_file, "r", encoding="utf-8") as f:
        for line in f:
            u = line.strip()
            if not u or u.startswith("#"):
                continue
            yield u


def scan_one(url):
    try:
        headers = request.fetch_headers(url)
        if headers is None:
            return {"url": url, "ok": False, "error": "No headers (request failed)"}
        return {"url": url, "ok": True, "headers": headers}
    except Exception as e:
        return {"url": url, "ok": False, "error": "%s: %s" % (e.__class__.__name__, e)}


def main(argv=None):
    args = parse_args(argv)
    urls = list(iter_targets(args))
    if not urls:
        print("No targets.", file=sys.stderr)
        return 2

    print("Total targets: %d" % len(urls))
    exit_code = 0

    for u in urls:
        res = scan_one(u)

        print("--- %s ---" % res["url"])
        if not res["ok"]:
            exit_code = 2
            print("ERROR: %s" % res["error"])
            print()
            continue

        headers = res["headers"]
        print("Headers: %d" % len(headers))
        for k, v in headers.items():
            print("%-28s : %s" % (k, v))
        print()

    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
