# GIS Software Development with Python

《GIS软件开发——基于Python编程语言》 · **吴健平 (Professor Jianping Wu from East China Normal University)** · ISBN `978-7-03-084099-8`

A hands-on textbook for learning GIS development with Python — **176 worked examples** across 14 chapters, covering spatial data formats, coordinate systems, web services, vector and raster analysis, and mapping on the web and on the desktop.

> **English edition — work in progress.**
> Translated from the upstream repository
> [`EcnuGISChaser/gis_develop_with_python`](https://github.com/EcnuGISChaser/gis_develop_with_python) — the companion code for the book
> **_GIS Software Development — Based on the Python Programming Language_** (《GIS软件开发——基于Python编程语言》)
> by **吴健平 (Wu Jianping), professor, School of Geographic Sciences, East China Normal University, Shanghai, CHN**, ISBN `978-7-03-084099-8`.
> The Chinese original is  here at [EcnuGISChaser/gis_develop_with_python](https://github.com/EcnuGISChaser/gis_develop_with_python).

[简体中文](README.zh-CN.md)

---

## How to use the code

| Folder | Contents |
| --- | --- |
| `示例代码/` | All examples — `chapter-2.ipynb` … `chapter-14.ipynb`, plus the `.py` and `.html` files for chapter 1 |
| `data/` | Sample datasets used by the notebooks |
| `demo/` | Standalone HTML / Leaflet demo pages |
| `photo/` | Images used by the examples |

**1. Install Python 3 and Jupyter**, plus the packages the examples use:

```powershell
pip install jupyter geopandas shapely fiona pyproj folium branca geojson pandas numpy matplotlib
```

Some chapters need extra packages: `opencv-python` (2, 8), `owslib` (3), `beautifulsoup4` and `selenium` (4),
`scikit-learn` (8, 12, 13), `PyQt5` (10, 11), `pyexiv2` (14), and GDAL/`osgeo` (8, 13) — install GDAL with
`conda install -c conda-forge gdal`.

**2. Open a notebook and run the cells in order:**

```powershell
jupyter notebook 示例代码/chapter-9.ipynb
```

**A note on the data.** The notebooks were written for a local data root such as `C:\data\china\city3.json`
or `C:\data\USA\STATES.shp`. Part of that data ships with this repository in `data/` (some as ZIP archives to
unzip first) — point the examples at those copies. The Landsat scene `20180523.img` (chapters 8, 13) and the
photos (chapter 14) are not included, so those examples need your own data.

**Notes.** Example headings and code comments are still in Chinese — translating them is the point of this
fork. Chapter 1 examples use `arcpy` and require an ArcGIS Pro installation. The `示例代码/` folder keeps its
Chinese name so this fork stays mergeable with upstream.

---

Original book: 《GIS软件开发——基于Python编程语言》 by **吴健平 (Jianping Wu)**, ISBN `978-7-03-084099-8` —
original code at [EcnuGISChaser/gis_develop_with_python](https://github.com/EcnuGISChaser/gis_develop_with_python).


