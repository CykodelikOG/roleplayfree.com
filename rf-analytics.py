#!/usr/bin/env python3
"""
roleplayfree.com -- Google Analytics 4 report.
Uses the same OAuth credentials as yt-analytics.py (claude-youtube-488012 project).
First run opens a browser for GA4 consent. Token cached separately from YouTube token.

Usage:
    python rf-analytics.py             # last 28 days
    python rf-analytics.py --days 90   # custom range
    python rf-analytics.py --save      # also write report to rf-report.txt

If you see "API not enabled": go to console.cloud.google.com, project claude-youtube-488012,
enable "Google Analytics Data API", then re-run.
"""

import argparse
import sys
from datetime import datetime, timedelta
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    RunReportRequest, DateRange, Metric, Dimension, OrderBy, FilterExpression,
    Filter, NumericValue
)

# -- Config -------------------------------------------------------------------
CREDENTIALS  = Path(r"G:\AI\Claude\ClaudeAssets\YouTube Analytics\credentials.json")
TOKEN        = Path(r"G:\AI\Claude\ClaudeAssets\YouTube Analytics\token-ga4.json")
REPORT_OUT   = Path(r"G:\AI\Claude\Projects\Roleplayfree\rf-report.txt")
PROPERTY_ID  = "properties/538764501"

SCOPES = ["https://www.googleapis.com/auth/analytics.readonly"]

# -- Auth ---------------------------------------------------------------------
def get_credentials():
    creds = None
    if TOKEN.exists():
        creds = Credentials.from_authorized_user_file(str(TOKEN), SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(str(CREDENTIALS), SCOPES)
            creds = flow.run_local_server(port=0)
        TOKEN.write_text(creds.to_json())
    return creds

def build_client():
    creds = get_credentials()
    return BetaAnalyticsDataClient(credentials=creds)

# -- Helpers ------------------------------------------------------------------
def date_range(days: int):
    end   = datetime.utcnow().date()
    start = end - timedelta(days=days)
    return str(start), str(end)

def fmt_num(n) -> str:
    try:
        v = float(n)
        if v >= 1_000_000: return f"{v/1_000_000:.1f}M"
        if v >= 1_000:     return f"{v/1_000:.1f}K"
        return f"{v:.0f}"
    except Exception:
        return str(n)

def fmt_pct(n) -> str:
    try:    return f"{float(n)*100:.1f}%"
    except: return str(n)

def fmt_dur(seconds) -> str:
    try:
        s = int(float(seconds))
        return f"{s//60}m {s%60:02d}s"
    except: return str(seconds)

def run_report(client, metrics: list, dimensions: list = None,
               start: str = None, end: str = None,
               order_by_metric: str = None, limit: int = 10) -> list:
    """Run a GA4 report, return list of row dicts."""
    req = RunReportRequest(
        property=PROPERTY_ID,
        date_ranges=[DateRange(start_date=start, end_date=end)],
        metrics=[Metric(name=m) for m in metrics],
        dimensions=[Dimension(name=d) for d in (dimensions or [])],
        limit=limit,
    )
    if order_by_metric:
        req.order_bys = [OrderBy(
            metric=OrderBy.MetricOrderBy(metric_name=order_by_metric),
            desc=True
        )]
    resp = client.run_report(req)
    rows = []
    dim_headers  = [h.name for h in resp.dimension_headers]
    met_headers  = [h.name for h in resp.metric_headers]
    for row in resp.rows:
        r = {}
        for i, v in enumerate(row.dimension_values):
            r[dim_headers[i]] = v.value
        for i, v in enumerate(row.metric_values):
            r[met_headers[i]] = v.value
        rows.append(r)
    return rows

# -- Report builder -----------------------------------------------------------
def build_report(days: int) -> str:
    start, end = date_range(days)
    client = build_client()

    lines = []
    def pr(s=""):
        lines.append(s)
        print(s)

    pr("=" * 60)
    pr("  roleplayfree.com -- Google Analytics 4 Report")
    pr(f"  Period: {start} to {end}  ({days} days)")
    pr(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    pr("=" * 60)
    pr()

    # -- Overview --
    pr("OVERVIEW")
    pr("-" * 40)
    try:
        overview = run_report(client,
            metrics=["sessions", "totalUsers", "newUsers", "screenPageViews",
                     "engagementRate", "averageSessionDuration", "bounceRate"],
            start=start, end=end)
        if overview:
            r = overview[0]
            new_pct = float(r.get("newUsers", 0)) / max(float(r.get("totalUsers", 1)), 1) * 100
            pr(f"  Sessions:            {fmt_num(r.get('sessions'))}")
            pr(f"  Users:               {fmt_num(r.get('totalUsers'))}  ({new_pct:.0f}% new)")
            pr(f"  Page views:          {fmt_num(r.get('screenPageViews'))}")
            pr(f"  Engagement rate:     {fmt_pct(r.get('engagementRate'))}")
            pr(f"  Avg session:         {fmt_dur(r.get('averageSessionDuration'))}")
            pr(f"  Bounce rate:         {fmt_pct(r.get('bounceRate'))}")
    except Exception as e:
        pr(f"  [Error fetching overview: {e}]")
    pr()

    # -- Top pages --
    pr("TOP PAGES")
    pr("-" * 40)
    try:
        pages = run_report(client,
            metrics=["screenPageViews", "sessions", "averageSessionDuration", "engagementRate"],
            dimensions=["pagePath"],
            order_by_metric="screenPageViews",
            start=start, end=end, limit=15)
        for r in pages:
            path = r.get("pagePath", "?")[:45]
            views = fmt_num(r.get("screenPageViews"))
            eng   = fmt_pct(r.get("engagementRate"))
            dur   = fmt_dur(r.get("averageSessionDuration"))
            pr(f"  {views:>6} views  {eng:>7} engaged  {dur:>7}  {path}")
    except Exception as e:
        pr(f"  [Error: {e}]")
    pr()

    # -- Traffic sources --
    pr("TRAFFIC SOURCES")
    pr("-" * 40)
    try:
        sources = run_report(client,
            metrics=["sessions", "totalUsers"],
            dimensions=["sessionDefaultChannelGroup"],
            order_by_metric="sessions",
            start=start, end=end, limit=10)
        total_sessions = sum(float(r.get("sessions", 0)) for r in sources) or 1
        for r in sources:
            channel  = r.get("sessionDefaultChannelGroup", "?")
            sessions = float(r.get("sessions", 0))
            pct      = sessions / total_sessions * 100
            pr(f"  {channel:<28} {fmt_num(sessions):>6} sessions  ({pct:.1f}%)")
    except Exception as e:
        pr(f"  [Error: {e}]")
    pr()

    # -- Search queries (if Search Console linked) --
    pr("TOP SEARCH QUERIES (organic)")
    pr("-" * 40)
    try:
        queries = run_report(client,
            metrics=["sessions"],
            dimensions=["searchTerm"],
            order_by_metric="sessions",
            start=start, end=end, limit=10)
        if queries and queries[0].get("searchTerm") not in ("(not set)", "(not provided)", None):
            for r in queries:
                term = r.get("searchTerm", "?")[:45]
                pr(f"  {fmt_num(r.get('sessions')):>6}  {term}")
        else:
            pr("  (Search Console not linked or no organic search data yet)")
    except Exception as e:
        pr(f"  [{e}]")
    pr()

    # -- Countries --
    pr("TOP COUNTRIES")
    pr("-" * 40)
    try:
        countries = run_report(client,
            metrics=["sessions", "totalUsers"],
            dimensions=["country"],
            order_by_metric="sessions",
            start=start, end=end, limit=8)
        for r in countries:
            pr(f"  {r.get('country', '?'):<25} {fmt_num(r.get('sessions'))} sessions  {fmt_num(r.get('totalUsers'))} users")
    except Exception as e:
        pr(f"  [Error: {e}]")
    pr()

    # -- Devices --
    pr("DEVICES")
    pr("-" * 40)
    try:
        devices = run_report(client,
            metrics=["sessions"],
            dimensions=["deviceCategory"],
            order_by_metric="sessions",
            start=start, end=end)
        total = sum(float(r.get("sessions", 0)) for r in devices) or 1
        for r in devices:
            s = float(r.get("sessions", 0))
            pr(f"  {r.get('deviceCategory', '?'):<12} {fmt_num(s):>6} ({s/total*100:.0f}%)")
    except Exception as e:
        pr(f"  [Error: {e}]")
    pr()

    # -- Events (affiliate clicks, quiz completions, etc.) --
    pr("TOP EVENTS")
    pr("-" * 40)
    try:
        events = run_report(client,
            metrics=["eventCount", "totalUsers"],
            dimensions=["eventName"],
            order_by_metric="eventCount",
            start=start, end=end, limit=15)
        # Filter out auto-generated page view events, focus on meaningful ones
        skip = {"page_view", "session_start", "first_visit", "user_engagement", "scroll"}
        meaningful = [r for r in events if r.get("eventName") not in skip]
        if meaningful:
            for r in meaningful:
                pr(f"  {fmt_num(r.get('eventCount')):>6}x  {r.get('eventName', '?')}")
        else:
            pr("  (No custom events beyond standard page tracking)")
    except Exception as e:
        pr(f"  [Error: {e}]")
    pr()

    # -- Daily sessions (last 28 days, sparkline) --
    pr("DAILY SESSIONS")
    pr("-" * 40)
    try:
        daily = run_report(client,
            metrics=["sessions"],
            dimensions=["date"],
            order_by_metric=None,
            start=start, end=end, limit=90)
        # Sort by date
        daily.sort(key=lambda x: x.get("date", ""))
        max_s = max(float(r.get("sessions", 0)) for r in daily) if daily else 1
        for r in daily[-28:]:
            date_str = r.get("date", "?")
            # Format YYYYMMDD -> YYYY-MM-DD
            if len(date_str) == 8:
                date_str = f"{date_str[:4]}-{date_str[4:6]}-{date_str[6:]}"
            s = float(r.get("sessions", 0))
            bar_len = int(s / max(max_s, 1) * 25)
            bar = "█" * bar_len
            pr(f"  {date_str}  {fmt_num(s):>5}  {bar}")
    except Exception as e:
        pr(f"  [Error: {e}]")
    pr()

    pr("=" * 60)
    return "\n".join(lines)

# -- Entry point --------------------------------------------------------------
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="roleplayfree.com GA4 Analytics")
    parser.add_argument("--days", type=int, default=28)
    parser.add_argument("--save", action="store_true", help="Save report to rf-report.txt")
    args = parser.parse_args()

    report = build_report(args.days)

    if args.save:
        REPORT_OUT.write_text(report, encoding="utf-8")
        print(f"\nReport saved to: {REPORT_OUT}")
