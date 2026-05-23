# Thrilljoy PIX! image catalog

Image hosting for the [Thrilljoy PIX!](https://thrilljoy.com/) collectible line, paired with the `Full PIX Catalog` tab of the Google Sheet that drives the AppSheet collection-tracking app.

## Structure

```
Thrilljoy/
  {Folder}/
    {Set_Slug}/
      {Figure_Slug}_{Variant_Slug}.png
  _franchise_map.json    ← sheet Franchise → folder lookup
```

`{Folder}` is **either** the franchise's umbrella folder (when its IP is grouped with related franchises) **or** the slugified franchise name itself. The mapping lives in [`_franchise_map.json`](./_franchise_map.json) — consult it first; if a franchise isn't listed there, default to slugifying the `Franchise` column value.

**Disk paths are decoupled from the sheet.** The sheet's `Franchise` column keeps the canonical franchise names (Annabelle, The Conjuring 2, Batman, etc.) — only the on-disk folder structure groups them under umbrellas. AppSheet reads column H (Image URL) and the franchise text labels independently, so the umbrella grouping is invisible to the app.

### Umbrella folders (current)

| Umbrella `{Folder}`            | Franchises folded in                                                                 |
| ------------------------------ | ------------------------------------------------------------------------------------ |
| `Conjuring_Universe`           | Annabelle, The Conjuring, The Conjuring 2, The Nun                                   |
| `DC`                           | Batman, Batman 1966, Batman: The Animated Series, The Dark Knight Trilogy, Superman, Peacemaker, Teen Titans Go |
| `Teenage_Mutant_Ninja_Turtles` | TMNT (and any future TMNT sub-lines)                                                 |
| `Chucky`                       | Child's Play, Chucky 2                                                               |
| `Universal_Monsters`           | Bram Stoker's Dracula, Creature from the Black Lagoon, The Mummy                     |
| `Stephen_King`                 | Welcome to Derry (and other King-IP drops)                                           |

Everything else lives under its own slugified franchise folder.

### Examples

- `Thrilljoy/Lisa_Frankenstein/Lisa_Frankenstein/Lisa_Hero.png` (standalone franchise)
- `Thrilljoy/The_Boys/Billy_Butcher/Billy_Butcher_Hero.png` (standalone franchise)
- `Thrilljoy/Conjuring_Universe/Annabelle/Annabelle_Hero.png` (sheet Franchise = "Annabelle")
- `Thrilljoy/Conjuring_Universe/The_Nun/The_Nun_Super_Chase.png` (sheet Franchise = "The Nun")
- `Thrilljoy/DC/Batman_Comics/Batman_Hero.png` (sheet Franchise = "Batman")
- `Thrilljoy/Universal_Monsters/Count_Dracula/Count_Dracula_Hero.png` (sheet Franchise = "Bram Stoker's Dracula")
- `Thrilljoy/Superbad/Seth/Evan_Chase.png` (standalone franchise)

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

- `MEGA PIX!`, `PIXL`, and `PIX! PANORAMIX` product types (different lines, sheet doesn't track them)
- Some products are listed as `PIX!` on the Shopify API but rebadged from Panoramix — the live product page will say `PLEASE NOTE- THIS PRODUCT WILL BE BRANDED "PIX!", NOT "PIX! PANORAMIX"`. Skip those too (known case: `pix-aang`).
- 39 webstore-exclusive variants (Bloo crossovers, GitD recolors, Hot Topic exclusives, etc.) that have no Shopify product entry — these need manual sourcing

## Source

- All images downloaded from `cdn.shopify.com/s/files/1/0672/1096/9252/files/...` (Thrilljoy's Shopify store)
- Ingested via the runbook in `.github/copilot-instructions.md`
- Initial ingest: 416 images across 108 franchises (Pop Mart Phase 7 close-out → Thrilljoy migration, 2026-05-22)
- 2026-05-23: Reorganized into 6 IP umbrellas (Conjuring_Universe, DC, Chucky, Universal_Monsters, Stephen_King, Teenage_Mutant_Ninja_Turtles) to reduce single-set franchise dirs. 91 top-level folders post-reorg. `_franchise_map.json` added as the sheet→folder bridge.
