# 1. osm-data-montenegro-explore
Exploration of OpenStreetData for Montenegro

Jupiter Notebook on Google Colab:
https://colab.research.google.com/github/dinorastoder/osm-data-montenegro-explore/blob/osm-data-load-podgorica/osm-podgorica-explore.ipynb

Output of Jupiter Notebook on Google Colab:
https://colab.research.google.com/gist/dinorastoder/984d1112584eaba80d8223b0ff98ac2d/osm-podgorica-explore.ipynb


| Institution Type | Name | OsmFeatureId | OsmGeometry | Centroid |
| ---------------- | ---- | ------------ | ----------- | -------- |
|  kindergarten | Vrtic taj i taj | way/3242342422 | POLIGON() | POINT() |
|  school | Osnovna skola "Vuk Karadzic" | way/4564656132 | POLIGON() | POINT() |
|  university | Univerzite Crne Gore | way/3432155488 | POLIGON() | POINT() |

| Bus Stop Name | Bus Lines | OsmFeatureId | OsmGeometry | Centroid | Buffer100 | Buffer250 | Buffer500 | Buffer1000 |
| ---------------- | ---- | ------------ | ----------- | -------- | -------- | -------- | -------- | -------- |
|  Hotel Hilton | Vrtic taj i taj | way/3242342422 | POLIGON() | POINT() | POLIGON() | POLIGON() | POLIGON() | POLIGON() |
|  Zgrada Vektre | Osnovna skola "Vuk Karadzic" | way/4564656132 | POLIGON() | POINT() | POLIGON() | POLIGON() | POLIGON() | POLIGON() |
|  Klinicki centar | Univerzite Crne Gore | way/3432155488 | POLIGON() | POINT() | POLIGON() | POLIGON() | POLIGON() | POLIGON() |

TODO:
1. Extract bus line from OSM
2. Display it in public transportation page
3. Display it on main page
4. Work on buttons that can control map layers
5. Describe basic text about data extractions and data used for analysis
6. Analysis of data and display
