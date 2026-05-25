# Popmart/

All Pop Mart figure images for the `Popmart Raw Data` tab of the tracking spreadsheet live here.

## Path scheme

```
Popmart/{IP}/{Series_Name}/{Character_Name}.{jpg|png}
```

The sheet's `Image URL` column (`Popmart Raw Data` → column K) points at:

```
https://raw.githubusercontent.com/Bulbasaurr/popmart-images/main/Popmart/{IP}/{Series_Name}/{Character_Name}.{jpg|png}
```

Sheet column → path segment mapping:

| Sheet column      | Path segment    | Example            |
| ----------------- | --------------- | ------------------ |
| (constant)        | brand parent    | `Popmart`          |
| `IP`              | IP directory    | `The_Monsters`     |
| `Series Name`     | series dir      | `Exciting_Macaron` |
| `Character Name`  | file basename   | `Chestnut_Cocoa.png` |

## Slug rule

`PascalCase_With_Underscores` — spaces → `_`, drop non-`[A-Za-z0-9_]`, collapse repeats. Same rule applied to IP, Series Name, and Character Name.

## IPs present

23 top-level IP directories (some currently sheet-tracked, some staged for future cataloging):

Chaka, Crybaby, Dimoo, Duckoo, Hacipupu, Hirono, Instinctoy, KUBO, Molly, Nyota, Peach_Riot, Pino_Jelly, Polar, POP_BEAN, Popmart_Collab, Popmart_Mixed_IP, Popmart_Other, Pucky, Skullpanda, Sweet_Bean, The_Monsters, Twinkle_Twinkle, Zsiga.

`Popmart_Collab` (IP × external licensors like Disney, Star Wars, SpongeBob) and `Popmart_Mixed_IP` (multi-IP sets like the Coffee Factory series) are "umbrella" buckets for sets that span multiple characters.

## Adding a new series

1. Identify the `IP` directory under `Popmart/` (create it if it's a brand-new IP).
2. Create the `Series_Name` subdirectory.
3. Add one image file per figure as `Character_Name.png` (or `.jpg` if the source is JPG).
4. Update the sheet's `Image URL` column (K) with the new raw GitHub URL for each row.
5. Commit + push with a descriptive message (e.g., `Add Skullpanda Petals in Four Acts (13 figures)`).

See `.github/copilot-instructions.md` for full conventions.
