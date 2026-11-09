"""Draw the 12 schematic districts of Meridia (matplotlib only)."""
import json

import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon


def load_districts(path="districts.geojson"):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def plot_district_map(gj, values=None, title="", cmap="Blues", legend_label="",
                      show_names=True, ax=None, vmin=None, vmax=None):
    """values: a pandas Series indexed by district_id (D01 ... D12)."""
    if ax is None:
        _, ax = plt.subplots(figsize=(7, 5.5))
    patches, colours = [], []
    for feat in gj["features"]:
        ring = feat["geometry"]["coordinates"][0]
        patches.append(Polygon(ring, closed=True))
        did = feat["properties"]["district_id"]
        colours.append(values.get(did, np.nan) if values is not None else np.nan)
    coll = PatchCollection(patches, edgecolor="white", linewidth=1.5)
    colours = np.array(colours, dtype=float)
    if values is not None:
        coll.set_array(np.ma.masked_invalid(colours))
        coll.set_cmap(cmap)
        coll.get_cmap().set_bad("#dddddd")
        coll.set_clim(vmin if vmin is not None else np.nanmin(colours), vmax if vmax is not None else np.nanmax(colours))
        plt.colorbar(coll, ax=ax, shrink=0.8, label=legend_label)
    else:
        coll.set_facecolor("#cfd8e3")
    ax.add_collection(coll)
    if show_names:
        for feat in gj["features"]:
            ring = np.array(feat["geometry"]["coordinates"][0][:-1])
            ax.text(ring[:, 0].mean(), ring[:, 1].mean(), feat["properties"]["district_name"],
                    ha="center", va="center", fontsize=7,
                    path_effects=[pe.withStroke(linewidth=2.5, foreground="white")])
    ax.autoscale_view()
    ax.set_aspect(1 / np.cos(np.radians(31.07)))  # keeps shapes undistorted at Meridia's latitude
    ax.set_axis_off()
    ax.set_title(title)
    return ax
