"""Scarica i livelli vettoriali di Natural Earth (pubblico dominio).

Tre scale, tre usi:
  110m  -> il mondo intero sullo schermo (anno 4, e il 5 se la mappa e' il mondo)
  50m   -> i continenti (anno 3, Europa)
  10m   -> i paesi (anno 2, la penisola; anno 3, le frontiere interne)

Non si tiene nessun file che il progetto non userà: la lista sotto e' gia' stata
ridotta ai livelli che servono a una mappa di gioco (contorni, acque, rilievo,
citta', vie).
"""
import os, sys, zipfile, urllib.request, io, json

BASE = "https://naciscdn.org/naturalearth/{scale}m/{kind}/{name}.zip"
RADICE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(os.environ.get("MAPPE_LAVORO", "/tmp/ne-mappe"), "ne")

# (scala, tipo, nome shapefile)
LAYERS = [
    # --- 110m: il mondo intero
    ("110", "cultural", "ne_110m_admin_0_countries"),
    ("110", "cultural", "ne_110m_admin_0_boundary_lines_land"),
    ("110", "physical", "ne_110m_coastline"),
    ("110", "physical", "ne_110m_rivers_lake_centerlines"),
    ("110", "physical", "ne_110m_lakes"),
    ("110", "physical", "ne_110m_land"),
    ("110", "physical", "ne_110m_ocean"),
    ("110", "physical", "ne_110m_geography_regions_polys"),
    ("110", "physical", "ne_110m_geography_regions_elevation_points"),
    ("110", "physical", "ne_110m_graticules_10"),
    ("110", "cultural", "ne_110m_populated_places_simple"),
    ("110", "cultural", "ne_110m_urban_areas"),
    # --- 50m: i continenti
    ("50", "cultural", "ne_50m_admin_0_countries"),
    ("50", "cultural", "ne_50m_admin_0_boundary_lines_land"),
    ("50", "cultural", "ne_50m_admin_1_states_provinces_lines"),
    ("50", "physical", "ne_50m_coastline"),
    ("50", "physical", "ne_50m_rivers_lake_centerlines"),
    ("50", "physical", "ne_50m_lakes"),
    ("50", "physical", "ne_50m_land"),
    ("50", "physical", "ne_50m_geography_regions_polys"),
    ("50", "physical", "ne_50m_geography_marine_polys"),
    ("50", "physical", "ne_50m_geography_regions_elevation_points"),
    ("50", "cultural", "ne_50m_populated_places"),
    ("50", "cultural", "ne_50m_urban_areas"),
    ("50", "cultural", "ne_50m_roads"),
    # --- 10m: i paesi
    ("10", "cultural", "ne_10m_admin_0_countries"),
    ("10", "cultural", "ne_10m_admin_0_boundary_lines_land"),
    ("10", "cultural", "ne_10m_admin_1_states_provinces_lines"),
    ("10", "cultural", "ne_10m_admin_1_states_provinces"),
    ("10", "cultural", "ne_10m_admin_0_map_units"),
    ("10", "cultural", "ne_10m_populated_places"),
    ("10", "cultural", "ne_10m_urban_areas"),
    ("10", "cultural", "ne_10m_roads"),
    ("10", "physical", "ne_10m_coastline"),
    ("10", "physical", "ne_10m_rivers_lake_centerlines_scale_rank"),
    ("10", "physical", "ne_10m_rivers"),
    ("10", "physical", "ne_10m_lakes"),
    ("10", "physical", "ne_10m_land"),
    ("10", "physical", "ne_10m_ocean"),
    ("10", "physical", "ne_10m_geography_regions_polys"),
    ("10", "physical", "ne_10m_geography_regions_elevation_points"),
    ("10", "physical", "ne_10m_geography_marine_polys"),
    ("10", "physical", "ne_10m_glaciated_areas"),
    ("10", "physical", "ne_10m_playas"),
    ("10", "physical", "ne_10m_graticules_10"),
]

manifest = {"source": "Natural Earth", "licence": "public domain",
            "url": "https://www.naturalearthdata.com/", "layers": []}

for scale, kind, name in LAYERS:
    url = BASE.format(scale=scale, kind=kind, name=name)
    dest = os.path.join(OUT, f"{scale}m", kind)
    os.makedirs(dest, exist_ok=True)
    try:
        with urllib.request.urlopen(url, timeout=90) as r:
            data = r.read()
        z = zipfile.ZipFile(io.BytesIO(data))
        shp = name + ".shp"
        if shp in z.namelist():
            for ext in (".shp", ".shx", ".dbf", ".prj"):
                if name + ext in z.namelist():
                    with open(os.path.join(dest, name + ext), "wb") as f:
                        f.write(z.read(name + ext))
            kb = os.path.getsize(os.path.join(dest, shp)) // 1024
            manifest["layers"].append({"scale": scale, "kind": kind, "name": name,
                                       "shp_kb": kb, "bytes": len(data)})
            print(f"OK  {scale:>3}m {name:<48} {kb:>7} kB")
        else:
            print(f"??  {name}: shapefile non trovato nello zip")
    except Exception as e:
        print(f"ERR {scale:>3}m {name:<48} {e}")

with open(os.path.join(OUT, "manifest.json"), "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)
print("\nlivelli scaricati:", len(manifest["layers"]))