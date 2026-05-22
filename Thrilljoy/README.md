# Thrilljoy PIX! image catalog

Image hosting for the [Thrilljoy PIX!](https://thrilljoy.com/) collectible line, paired with the `Full PIX Catalog` tab of the Google Sheet that drives the AppSheet collection-tracking app.

## Structure

```
Thrilljoy/
  {Franchise_Slug}/
    {Set_Slug}/
      {Figure_Slug}_{Variant_Slug}.png
```

Examples:
- `Thrilljoy/Lisa_Frankenstein/Lisa_Frankenstein/Lisa_Hero.png`
- `Thrilljoy/Lisa_Frankenstein/Lisa_Frankenstein/The_Creature_Ultra_Chase.png`
- `Thrilljoy/The_Boys/Billy_Butcher/Billy_Butcher_Hero.png`
- `Thrilljoy/Superbad/Seth/Evan_Chase.png`

Slug rule: spaces → `_`, drop non-`[A-Za-z0-9_]`, collapse multiple `_`. Apostrophes, ampersands, periods all become `_`.

## Variants (column F of `Full PIX Catalog`)

`Hero`, `Chase`, `Super Chase`, `Ultra Chase`, `Hyper Chase` — in slugs these become `Hero`, `Chase`, `Super_Chase`, `Ultra_Chase`, `Hyper_Chase`.

## Image semantics (when downloading from Shopify)

For each Thrilljoy Shopify product (`https://thrilljoy.com/products/{handle}.json`), `images[]` contains:

| Filename pattern                            | What it is                                           | Use it? |
| ------------------------------------------- | ---------------------------------------------------- | ------- |
| `{dropId}-{Brand}-{Franchise}-{Figure}_{Variant}.png`     | Canonical product shot: closed box + standalone figure composite | ✅ Yes — this is what we ingest |
| `{dropId}-{Brand}-{Franchise}-{Figure}_{Variant}_-{N}.png` | Alternate angle (open-window box variant)            | ⚠️ Only if canonical missing |
| `{dropId}-{Brand}-{Franchise}-{Figure}-O-Card.png`        | Certificate-of-Authenticity collector's card (front+back showing full set lineup) | ❌ Skip — not a per-figure image |

`{dropId}` = Shopify product release ID (stable per-product). Used as the join key for sheet ↔ Shopify delta detection.

## Onboarding a new drop

See [`.github/copilot-instructions.md`](../.github/copilot-instructions.md) — the "Thrilljoy ingest" section has the full runbook.

Short version: fetch `https://thrilljoy.com/products.json?limit=250`, find products whose `dropId` isn't in sheet column H yet, parse their `body_html` for edition size + chase odds, append rows, download images here, push, update sheet URLs.

## Out of scope

- `MEGA PIX!` and `PIXL` product types (different lines, sheet doesn't track them)
- 39 webstore-exclusive variants (Bloo crossovers, GitD recolors, Hot Topic exclusives, etc.) that have no Shopify product entry — these need manual sourcing

## Source

- All images downloaded from `cdn.shopify.com/s/files/1/0672/1096/9252/files/...` (Thrilljoy's Shopify store)
- Ingested via the runbook in `.github/copilot-instructions.md`
- Initial ingest: 416 images across 108 franchises (Pop Mart Phase 7 close-out → Thrilljoy migration, 2026-05-22)
