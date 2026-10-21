#!/usr/bin/env python3
"""
LeadStackCost — B2B Lead Scraping & Enrichment Cost Calculator — Command-Line Cost Calculator
Live Web Calculator: https://sectoroneventures.github.io/leadstack-cost/
"""
import argparse

PROVIDERS = [
  {
    "name": "Apify Google Maps + Contact Details Actor",
    "cost_per_unit": 0.55,
    "min_monthly": 0.0,
    "speed_note": "Live phone, email, website & rating extraction ($5 free credit)",
    "cta_label": "Run Apify Lead Scraper Free \u2192",
    "cta_url": "https://apify.com?fpr=infrabench7552",
    "highlight": true
  },
  {
    "name": "ScrapingBee Custom Domain & Directory Scraper",
    "cost_per_unit": 0.68,
    "min_monthly": 0.0,
    "speed_note": "Stealth Chrome rendering for protected directories (1,000 free calls)",
    "cta_label": "Try ScrapingBee Free \u2192",
    "cta_url": "https://www.scrapingbee.com?fpr=infrabench7552",
    "highlight": false
  },
  {
    "name": "Traditional Per-Credit B2B Lead SaaS",
    "cost_per_unit": 18.0,
    "min_monthly": 149.0,
    "speed_note": "Expensive per-credit lock-in with stale cached emails",
    "cta_label": "Switch to Live Apify Scraping \u2192",
    "cta_url": "https://apify.com?fpr=infrabench7552",
    "highlight": false
  }
]

def main() -> None:
    parser = argparse.ArgumentParser(description="Compare monthly B2B lead database subscriptions ($499-$1,500/mo) against scraping live Google Maps & directory leads with Apify + ScrapingBee.")
    parser.add_argument("--volume", type=float, default=25, help="Monthly Verified Local / B2B Leads Needed (in Thousands)")
    args = parser.parse_args()
    print(f"=== {args.volume:g} k leads/mo Cost Comparison ===")
    for p in PROVIDERS:
        cost = max(float(p["min_monthly"]), args.volume * float(p["cost_per_unit"]))
        print(f"* {p['name']}: ${cost:,.2f}/mo ({p['speed_note']})")
        print(f"  -> {p['cta_url']}")
    print(f"\nInteractive web calculator: https://sectoroneventures.github.io/leadstack-cost/")

if __name__ == "__main__":
    main()
